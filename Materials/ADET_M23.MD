Here is the updated and modernized version of Module 23, revised to align with current Android and backend development standards.

---

# Android & PHP-MySQL: Modern Secure Integration

## A. Lesson Preview & Review

Welcome! In previous modules, you learned how to build the UI and handle local data. Now, we are connecting your app to a remote backend. 

Historically, developers used raw `HttpURLConnection` or the Apache HTTP client to send requests. Today, the standard is a secure **REST API** architecture. Your Android app (the client) will communicate with a PHP script (the middleman), which securely queries a MySQL database.

> **Quick Recap:** The old `Apache HTTP client` is deprecated. We will use **Retrofit** and **OkHttp** for networking, and **Kotlin Serialization** for parsing. On the backend, we will use **PHP Data Objects (PDO)** with prepared statements to prevent SQL injection.

**Learning Targets:**
1.  Understand the modern Client-Server architecture.
2.  Implement secure database operations using **PDO** and prepared statements.
3.  Build a type-safe Retrofit API service in Kotlin.
4.  Handle network requests asynchronously using **Kotlin Coroutines**.

![Client-Server Architecture](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&q=80&w=1000)

---

## B. Main Lesson

### 1. The Architecture: How it Works
Android apps **do not** connect directly to a MySQL database. The database is hidden behind a web server for security. The flow is:
1.  **Android App:** Sends an HTTP request (GET/POST) with JSON data.
2.  **PHP Script:** Receives the request, validates it, and connects to MySQL.
3.  **MySQL Database:** Executes the query.
4.  **PHP Script:** Formats the result as a JSON response and sends it back.
5.  **Android App:** Parses the JSON and updates the UI.

### 2. The Backend: Secure PHP & MySQL
The legacy approach uses `mysqli_query` with string concatenation, which is vulnerable to **SQL Injection**. The modern standard is **PDO** (PHP Data Objects) with **Prepared Statements**.

#### Creating the Database and Table
```sql
CREATE DATABASE IF NOT EXISTS app_db;
USE app_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'user'
);
```

#### Secure PHP Connection & Login Script (`login.php`)
This script prevents SQL injection and securely verifies passwords.

```php
<?php
// 1. Secure Database Connection using PDO
$host = 'localhost';
$db   = 'app_db';
$user = 'root'; // Replace with your DB user
$pass = '';     // Replace with your DB password
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    // Never expose raw error messages to the client
    http_response_code(500);
    echo json_encode(["error" => "Database connection failed"]);
    exit;
}

// 2. Receive JSON Input (Modern approach)
$input = json_decode(file_get_contents('php://input'), true);

if (!isset($input['username']) || !isset($input['password'])) {
    http_response_code(400);
    echo json_encode(["error" => "Missing credentials"]);
    exit;
}

$username = $input['username'];
$password = $input['password'];

// 3. Secure Query using Prepared Statements
$stmt = $pdo->prepare('SELECT id, username, password_hash, role FROM users WHERE username = ?');
$stmt->execute([$username]);
$user = $stmt->fetch();

// 4. Verify Password securely
if ($user && password_verify($password, $user['password_hash'])) {
    // In a real app, you should generate a JWT token here
    unset($user['password_hash']); // Do not send password hash back
    echo json_encode(["success" => true, "user" => $user]);
} else {
    http_response_code(401);
    echo json_encode(["error" => "Invalid credentials"]);
}
?>
```

### 3. The Android Client: Modern Networking Stack
We will use **Retrofit** (type-safe HTTP client) with **OkHttp** (efficient network engine) and **Kotlin Serialization** (fast JSON parsing).

**Step 1: Add Dependencies** (`build.gradle.kts`)
```kotlin
plugins {
    id("kotlinx-serialization")
}

dependencies {
    implementation("com.squareup.retrofit2:retrofit:2.11.0")
    implementation("com.squareup.retrofit2:converter-kotlinx-serialization:2.11.0")
    implementation("com.squareup.okhttp3:okhttp:4.12.0")
    implementation("com.squareup.okhttp3:logging-interceptor:4.12.0")
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.3")
}
```

**Step 2: Define Data Classes** (`@Serializable`)
```kotlin
import kotlinx.serialization.Serializable

@Serializable
data class LoginRequest(val username: String, val password: String)

@Serializable
data class LoginResponse(val success: Boolean, val user: User? = null, val error: String? = null)

@Serializable
data class User(val id: Int, val username: String, val role: String)
```

**Step 3: Define the Retrofit API Interface**
```kotlin
import retrofit2.http.Body
import retrofit2.http.POST

interface ApiService {
    @POST("login.php") // Path to your PHP script
    suspend fun login(@Body request: LoginRequest): LoginResponse
}
```

**Step 4: Build the Retrofit Instance**
```kotlin
import kotlinx.serialization.json.Json
import okhttp3.MediaType.Companion.toMediaType
import retrofit2.Retrofit
import retrofit2.converter.kotlinx.serialization.asConverterFactory

object RetrofitClient {
    private const val BASE_URL = "https://yourdomain.com/api/" // Must use HTTPS

    private val json = Json { ignoreUnknownKeys = true }

    val api: ApiService by lazy {
        Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
            .build()
            .create(ApiService::class.java)
    }
}
```

**Step 5: Call the API from a ViewModel (using Coroutines)**
```kotlin
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.launch

class LoginViewModel : ViewModel() {
    fun performLogin(username: String, password: String) {
        viewModelScope.launch {
            try {
                val response = RetrofitClient.api.login(LoginRequest(username, password))
                if (response.success) {
                    println("Login successful! Welcome ${response.user?.username}")
                } else {
                    println("Error: ${response.error}")
                }
            } catch (e: Exception) {
                println("Network Error: ${e.message}")
            }
        }
    }
}
```

---

## C. Analogies and Use Cases

### Analogy: The Restaurant Experience
*   **Android App:** You (the customer) reading the menu.
*   **PHP Script:** The waiter. You tell the waiter what you want (send a request). The waiter doesn't let you into the kitchen.
*   **MySQL Database:** The kitchen.
*   **Retrofit:** The menu and the waiter's notepad. It standardizes how you order.
*   **PDO (Prepared Statements):** The waiter writing your order on a clean, separate ticket. This prevents a malicious customer from writing "Give me all the food and burn the kitchen" (SQL Injection) on the order slip.

### Real-World Use Case: The E-Commerce App
When a user logs into a shopping app, the app sends their credentials via Retrofit. The PHP backend uses PDO to query the MySQL database. If successful, PHP returns a **JWT (JSON Web Token)**. The Android app stores this token securely and attaches it to future requests to authenticate the user.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   **Never connect Android directly to MySQL.** Always use a middle layer like PHP.
*   **Security First:** Use **PDO** with prepared statements in PHP to prevent SQL injection. Always hash passwords with `password_hash()`.
*   **Android Networking:** Use **Retrofit** + **OkHttp** + **Kotlin Serialization**.
*   **Asynchronous Execution:** Use Kotlin **Coroutines** (`suspend` functions) to keep network calls off the main thread.
*   **API Design:** Use JSON for data exchange and `HTTPS` for secure transmission.

### Frequently Asked Questions

**1. Is `HttpURLConnection` deprecated?**
No, it's not officially deprecated, but it's considered legacy. Google and the industry strongly recommend Retrofit for its type-safety, ease of use, and automatic parsing.

**2. Why use PHP instead of a modern backend like Node.js or Python?**
PHP is widely supported, free, and easy to deploy on shared hosting. It's a great choice for small to medium projects.

**3. What is the difference between `GET` and `POST`?**
`GET` is used to retrieve data (parameters are in the URL, less secure, visible). `POST` is used to send data (parameters are in the request body, more secure, used for login/creating data).

**4. How do I handle user sessions in a mobile app?**
The modern standard is to use **Tokens (JWT)**. After a successful login, the PHP script returns a token. The Android app stores it (using **EncryptedSharedPreferences**) and sends it in the `Authorization` header for subsequent requests.

**5. What happens if the user has no internet?**
You should check connectivity using `ConnectivityManager` before making a request, or catch the `IOException` in your coroutine and show a user-friendly error message.

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Secure Login UI

**The Task:** Create a Compose UI that accepts a username and password and calls the `LoginViewModel`.

```kotlin
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel

@Composable
fun LoginScreen(viewModel: LoginViewModel = viewModel()) {
    var username by remember { mutableStateOf("") }
    var password by remember { mutableStateOf("") }

    Column(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        verticalArrangement = Arrangement.Center
    ) {
        OutlinedTextField(
            value = username,
            onValueChange = { username = it },
            label = { Text("Username") },
            modifier = Modifier.fillMaxWidth()
        )
        Spacer(modifier = Modifier.height(8.dp))
        OutlinedTextField(
            value = password,
            onValueChange = { password = it },
            label = { Text("Password") },
            modifier = Modifier.fillMaxWidth()
        )
        Spacer(modifier = Modifier.height(16.dp))
        Button(
            onClick = { viewModel.performLogin(username, password) },
            modifier = Modifier.fillMaxWidth()
        ) {
            Text("Login")
        }
    }
}
```

---

## F. Skill-Building Check

**1. What is the recommended modern library for type-safe API calls in Android?**
A) `HttpURLConnection`
B) `Apache HTTP Client`
C) `Retrofit`
D) `Volley`
> **Correct Answer: C** (Retrofit is the standard for type-safe REST clients.)

**2. Which PHP extension is recommended for secure database connections to prevent SQL injection?**
A) `mysqli` with string concatenation
B) `mysql_` functions
C) `PDO` with prepared statements
D) Raw SQL files
> **Correct Answer: C** (PDO with prepared statements separates SQL logic from data, preventing injection.)

**3. How do you handle network requests in Android to avoid freezing the UI?**
A) Run them on the main thread.
B) Use Kotlin Coroutines (`suspend` functions) or RxJava.
C) Use `Thread.sleep()`.
D) Use `AsyncTask`.
> **Correct Answer: B** (Coroutines handle background threading efficiently.)

**4. True or False: It is safe to store user passwords using MD5 or SHA1 hashing in MySQL.**
A) True
B) False
> **Correct Answer: B (False)** (MD5/SHA1 are cryptographically broken. Use `password_hash()` with bcrypt or Argon2.)

**5. What is the role of Kotlin Serialization in this stack?**
A) To encrypt database connections.
B) To map JSON strings to Kotlin data classes.
C) To handle network timeouts.
D) To generate UI layouts.
> **Correct Answer: B** (It converts JSON data into strongly-typed Kotlin objects.)

**6. Which HTTP method is typically used to send login credentials?**
A) `GET`
B) `POST`
C) `HEAD`
D) `PUT`
> **Correct Answer: B** (POST sends data in the request body, which is more secure than the URL.)

**7. True or False: You should expose your MySQL database directly to the internet so Android can connect.**
A) True
B) False
> **Correct Answer: B (False)** (This is a massive security risk. Always use a middle layer like PHP.)

**8. Which OkHttp Interceptor is useful for debugging network requests?**
A) `AuthInterceptor`
B) `CacheInterceptor`
C) `HttpLoggingInterceptor`
D) `NetworkInterceptor`
> **Correct Answer: C** (`HttpLoggingInterceptor` logs request and response details.)