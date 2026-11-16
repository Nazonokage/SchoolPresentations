# Android Networking & Modern Data Parsing

---

## A. Lesson Preview & Review

Android apps rarely function in isolation. Whether your app needs to fetch weather data, sync a user's profile, or load a feed of posts, it must connect to the internet. 

This module covers how to check network connectivity, perform network operations safely, and parse the data returned by servers.

> **Important Paradigm Shift:** The original course material relied on older technologies like `HttpURLConnection` for raw networking, `Gson` for JSON, and `XmlPullParser` for XML. While these still exist, modern Android development uses **Retrofit**, **OkHttp**, and **Kotlin Serialization** to make networking safe, fast, and declarative.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Monitor device connectivity using `ConnectivityManager` and `NetworkCallback`.
2.  Understand why you must never perform network operations on the main thread.
3.  Understand the XML and JSON data formats.
4.  Use **Kotlin Serialization** to parse JSON into Kotlin data classes.

![Global network connectivity concept](https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=1000)

---

## B. Main Lesson

### Part 1: Checking Network Connection
Before performing network operations, you must check if the device is connected to the internet. The modern approach uses `ConnectivityManager`.

*   **Legacy approach:** Checking `NetworkInfo` (Deprecated) or `getAllNetworkInfo()` (Deprecated).
*   **Modern approach:** Use `ConnectivityManager` with `NetworkCapabilities` to check if the current active network has the `NET_CAPABILITY_INTERNET` and `NET_CAPABILITY_VALIDATED` capabilities.

```kotlin
fun isNetworkAvailable(context: Context): Boolean {
    val cm = context.getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
    val network = cm.activeNetwork ?: return false
    val capabilities = cm.getNetworkCapabilities(network) ?: return false
    return capabilities.hasCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET) &&
           capabilities.hasCapability(NetworkCapabilities.NET_CAPABILITY_VALIDATED)
}
```

> **Pro Tip:** For real-time monitoring, use `ConnectivityManager.NetworkCallback` to listen for `onAvailable` and `onLost` events instead of polling `isNetworkAvailable()` repeatedly.

---

### Part 2: Performing Network Operations (The Modern Stack)
Performing network operations manually with `HttpURLConnection` is error-prone. Modern Android development uses **Retrofit** (a type-safe HTTP client) and **OkHttp** (the underlying HTTP engine) for all backend communication.

1.  **Never call the network on the main thread:** Doing so causes `NetworkOnMainThreadException` and freezes the UI. Use Kotlin Coroutines and `suspend` functions to run network requests on a background thread.
2.  **Retrofit** allows you to declare an interface for your API. Retrofit handles the threading, request creation, and response parsing.

```kotlin
// 1. Define the API interface
interface WeatherApiService {
    @GET("data/2.5/weather")
    suspend fun getCurrentWeather(
        @Query("q") cityName: String,
        @Query("appid") apiKey: String
    ): WeatherResponse
}

// 2. Build Retrofit
val retrofit = Retrofit.Builder()
    .baseUrl("https://api.openweathermap.org/")
    .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
    .build()

val apiService = retrofit.create(WeatherApiService::class.java)
```

---

### Part 3: Modern JSON Parsing with Kotlin Serialization
The original module teaches `JSONObject` and `Gson`. Both are now legacy:
*   **Gson** relies on reflection, which is slow, and it silently ignores Kotlin nullability rules, leading to crashes.
*   **Modern Standard:** Use **Kotlin Serialization** (`kotlinx.serialization`). It is official, compile-time based, fast, and null-safe.

#### JSON Structure Review
JSON consists of:
*   **Objects:** `{}` (key-value pairs)
*   **Arrays:** `[]` (lists of values)
*   **Keys & Values:** Strings, numbers, booleans, or nested objects/arrays.

**Example JSON:**
```json
{
  "main": {
    "temp": 304.15,
    "pressure": 1009
  },
  "weather": [
    { "description": "smoke", "icon": "50n" }
  ]
}
```

**Modern Kotlin Data Class:**
Annotate your class with `@Serializable` and map fields using `@SerialName`.

```kotlin
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class WeatherResponse(
    val main: Main,
    val weather: List<Weather>
)

@Serializable
data class Main(
    @SerialName("temp") val temperature: Double,
    val pressure: Int
)

@Serializable
data class Weather(
    val description: String,
    val icon: String
)
```

> **Note:** In Kotlin Serialization, fields must match the JSON keys exactly, or you must explicitly map them using `@SerialName`. Unlike Gson, it will throw an exception if a required field is missing, which is safer for debugging.

---

### Part 4: XML Parsing (Legacy and Modern)
XML is a markup language similar to HTML. While JSON is the dominant format for modern APIs, you may still encounter XML in legacy systems, SOAP APIs, or RSS feeds.

*   **Legacy:** `XmlPullParser` is an event-based parser. You iterate through events (`START_TAG`, `END_TAG`) and read attributes manually. It is efficient but verbose.
*   **Modern:** For simple XML, use `Simple XML` or `TikXml` libraries to map XML directly to Kotlin objects (similar to how Retrofit maps JSON). For new projects, **if you have a choice, prefer JSON**, as the tooling is much better.

---

## C. Analogies and Use Cases

### Analogy: The Restaurant Order
*   **Connectivity Check:** Looking out the window to see if the delivery truck is outside.
*   **Retrofit:** The waiter. You give the waiter your order (API interface), and they go to the kitchen (server) to get your food. You don't need to know how the kitchen works.
*   **Kotlin Serialization:** The interpreter. The kitchen sends food in a specific format (JSON). The interpreter converts the raw JSON into a delicious, usable Kotlin object (the meal) that you can consume.

### Real-World Use Case: The Weather App
1.  **Connectivity:** The app uses `ConnectivityManager` to ensure the user is online.
2.  **Network Call:** The app uses Retrofit to call a weather API.
3.  **Parsing:** The API returns JSON. Retrofit automatically uses Kotlin Serialization to convert the JSON into a `WeatherResponse` data class.
4.  **UI Update:** The app displays the temperature in a Compose `Text` component.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   **Connectivity:** Always check network availability using `ConnectivityManager` before making a request.
*   **Networking Stack:** Use **Retrofit** and **OkHttp** for all API calls. Use Kotlin Coroutines (`suspend` functions) to avoid blocking the main thread.
*   **JSON Parsing:** Use **Kotlin Serialization** (`@Serializable`). It is null-safe, fast, and the modern standard. Avoid `Gson` for new projects.
*   **XML Parsing:** `XmlPullParser` is the legacy standard for XML. Use it only if your API requires XML.
*   **Cleartext Traffic:** Since Android 9 (API 28), HTTP (cleartext) traffic is disabled by default. You must use HTTPS or configure `NetworkSecurityConfig`.

### Frequently Asked Questions

**1. Why can't I perform network operations on the main thread?**
The main thread handles UI updates. If you block it with a network call, the UI will freeze, and the app will crash with a `NetworkOnMainThreadException`.

**2. What is the difference between `HttpURLConnection` and Retrofit?**
`HttpURLConnection` is a low-level Java API for raw HTTP requests. Retrofit is a high-level, type-safe wrapper that handles threading, request building, and response parsing automatically.

**3. Is Gson still okay to use?**
Gson still works, but it is not recommended for new Kotlin projects. It uses reflection and does not enforce Kotlin's null safety. Kotlin Serialization is the official, modern replacement.

**4. How do I handle network errors in Compose?**
Use a `sealed class` or `StateFlow` to represent UI state. The UI should react to three states: `Loading`, `Success` (with data), and `Error` (with a message).

**5. What happens if I try to access an HTTP URL on modern Android?**
The system will block the request and throw a `java.net.UnknownServiceException: CLEARTEXT communication to ... not permitted by network security policy`. Always use HTTPS.

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Fetching and Parsing JSON

**The Task:** Implement a simple ViewModel that uses Retrofit and Kotlin Serialization to fetch a todo item from a public API and exposes the result to the UI.

**Step 1: Add Dependencies** to `build.gradle.kts`.
```kotlin
// Retrofit & OkHttp
implementation("com.squareup.retrofit2:retrofit:2.11.0")
implementation("com.squareup.retrofit2:converter-kotlinx-serialization:2.11.0")
implementation("com.squareup.okhttp3:logging-interceptor:4.12.0")

// Kotlin Serialization
implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.3")
```
Apply the serialization plugin: `plugins { kotlin("plugin.serialization") }`.

**Step 2: Create Data Classes**
```kotlin
@Serializable
data class Todo(
    val userId: Int,
    val id: Int,
    val title: String,
    val completed: Boolean
)
```

**Step 3: Create the API Interface**
```kotlin
interface TodoApi {
    @GET("todos/1")
    suspend fun getTodo(): Todo
}
```

**Step 4: Create the ViewModel**
```kotlin
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

sealed interface UiState {
    data object Loading : UiState
    data class Success(val todo: Todo) : UiState
    data class Error(val message: String) : UiState
}

class TodoViewModel : ViewModel() {
    private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()

    private val api = Retrofit.Builder()
        .baseUrl("https://jsonplaceholder.typicode.com/")
        .addConverterFactory(Json.asConverterFactory("application/json".toMediaType()))
        .build()
        .create(TodoApi::class.java)

    init {
        fetchTodo()
    }

    private fun fetchTodo() {
        viewModelScope.launch {
            _uiState.value = UiState.Loading
            try {
                val todo = api.getTodo()
                _uiState.value = UiState.Success(todo)
            } catch (e: Exception) {
                _uiState.value = UiState.Error(e.message ?: "Unknown error")
            }
        }
    }
}
```

**Step 5: Compose UI**
```kotlin
@Composable
fun TodoScreen(viewModel: TodoViewModel = viewModel()) {
    val state by viewModel.uiState.collectAsState()

    when (val currentState = state) {
        is UiState.Loading -> CircularProgressIndicator()
        is UiState.Success -> Text(text = currentState.todo.title)
        is UiState.Error -> Text(text = "Error: ${currentState.message}")
    }
}
```

---

## F. Skill-Building Check

**1. What is the modern, recommended library for type-safe HTTP requests in Android?**
A) `HttpURLConnection`
B) `Retrofit`
C) `Volley`
D) `OkHttp` alone
> **Correct Answer: B** (Retrofit is the industry standard for type-safe HTTP clients.)

**2. True or False: You should perform network operations on the main thread.**
A) True
B) False
> **Correct Answer: B (False)** (This causes a `NetworkOnMainThreadException` and freezes the UI.)

**3. What is the modern, recommended library for JSON parsing in Kotlin?**
A) `Gson`
B) `JSONObject`
C) `Kotlin Serialization`
D) `Moshi`
> **Correct Answer: C** (Kotlin Serialization is the official, compile-time, null-safe standard.)

**4. In Kotlin Serialization, which annotation is used to map a JSON key to a differently named Kotlin property?**
A) `@Json`
B) `@SerializedName`
C) `@SerialName`
D) `@JsonProperty`
> **Correct Answer: C** (`@SerialName` is used for field mapping.)

**5. What class is used to check the device's current network connectivity?**
A) `NetworkInfo`
B) `ConnectivityManager`
C) `WifiManager`
D) `TelephonyManager`
> **Correct Answer: B** (`ConnectivityManager` is the modern API for network state.)

**6. True or False: HTTP (cleartext) traffic is enabled by default on modern Android.**
A) True
B) False
> **Correct Answer: B (False)** (It is disabled by default starting from Android 9 (API 28).)

**7. Which coroutine builder is used to launch a network call in a ViewModel without blocking the UI?**
A) `runBlocking`
B) `viewModelScope.launch`
C) `GlobalScope.launch`
D) `CoroutineScope(Dispatchers.Main).launch`
> **Correct Answer: B** (`viewModelScope.launch` is the standard way to launch coroutines in a ViewModel.)

**8. What format does a JSON object use to enclose its key-value pairs?**
A) Square brackets `[]`
B) Curly braces `{}`
C) Parentheses `()`
D) Angle brackets `<>`
> **Correct Answer: B** (Curly braces represent JSON objects.)