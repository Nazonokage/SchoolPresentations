Here is the modernized, 2026-ready version of Module 21. The content has been updated to reflect current best practices, shifting from manual SQLite database management toward modern Jetpack architecture (Room) while retaining the essential concepts of Inter-Process Communication (IPC) that Content Providers enable.

---

# Android Content Providers: Sharing Data Securely Across Apps

---

## A. Lesson Preview & Review

Welcome to our lesson on **Content Providers**! 

Some applications contain a huge amount of records. Managing many records using just SharedPreferences or simple files is impractical. Furthermore, what if another app needs to access your data—like a calendar app reading your contacts, or a photo editor accessing your gallery?

This is where **Content Providers** come in. They act as a central repository for your app's data (stored in an SQLite database, files, or even over a network) and provide a secure mechanism for other applications to query, insert, update, or delete that data based on user permissions.

> **Quick Recap:** You've learned how to build UIs, handle events, and manage local data. Content Providers are the bridge that securely exposes your app's data to the *rest of the Android ecosystem*.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Understand the core concepts of Content Providers, Resolvers, and URIs.
2.  Perform Create, Read, Update, and Delete (CRUD) operations using `ContentResolver`.
3.  Understand how to secure your data using provider permissions.
4.  Recognize how modern tools like **Room** simplify Content Provider creation.

![Data sharing concept](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&q=80&w=1000)

---

## B. Main Lesson

### Content Provider Concepts
A **Content Provider** manages access to a structured set of data. It encapsulates the data and provides mechanisms for defining data security. 

*   **ContentProvider (The Server):** Your app implements this class to expose its data.
*   **ContentResolver (The Client):** Another app uses this class to query or modify the data exposed by your provider.

### The Content URI (Uniform Resource Identifier)
To access data from a Content Provider, the client uses a **Content URI** as a query string. It uniquely identifies the dataset and the specific record you want to access.

**Anatomy of a Content URI:**
Let's look at a standard URI: `content://com.example.app.provider/users/5`

| Component | Example | Description |
| :--- | :--- | :--- |
| **Scheme** | `content://` | Mandatory prefix indicating it's a Content URI. |
| **Authority** | `com.example.app.provider` | The unique identifier for the provider (usually the package name). |
| **Path** | `users` | The type of data (the table or directory). |
| **ID** | `5` | (Optional) The specific record. If omitted, it's a directory-based URI (returns all users). If included, it's an ID-based URI (returns only user #5). |

### CRUD Operations via ContentResolver
Applications interact with a Content Provider using the `ContentResolver` object, which is accessed via `context.contentResolver`. It handles the Inter-Process Communication (IPC) for you.

*   **Create (Insert):** `insert()` - Adds a new record. Returns the URI of the new item.
*   **Read (Query):** `query()` - Retrieves data. Returns a `Cursor` object.
*   **Update:** `update()` - Modifies existing records. Returns the number of rows updated.
*   **Delete:** `delete()` - Removes records. Returns the number of rows deleted.

#### Modern Example: Reading Contacts (The most common use of Content Providers)
Most developers don't write their own ContentProviders; they *consume* system ones. Here is how you query the device's Contacts database using Compose and Coroutines.

```kotlin
// Request READ_CONTACTS permission first!
val contentResolver = LocalContext.current.contentResolver

LaunchedEffect(Unit) {
    // 1. Define the URI (System Contacts provider)
    val uri = ContactsContract.Contacts.CONTENT_URI
    
    // 2. Define the columns you want to retrieve
    val projection = arrayOf(
        ContactsContract.Contacts._ID,
        ContactsContract.Contacts.DISPLAY_NAME
    )

    // 3. Query the provider
    val cursor = contentResolver.query(
        uri, projection, null, null, null
    )

    // 4. Parse the Cursor
    cursor?.use {
        val nameIndex = it.getColumnIndex(ContactsContract.Contacts.DISPLAY_NAME)
        while (it.moveToNext()) {
            val name = it.getString(nameIndex)
            Log.d("Contacts", "Name: $name")
        }
    }
}
```

### Creating Your Own Content Provider (The Modern Way)
Historically, creating a provider meant extending `ContentProvider` and manually managing an `SQLiteOpenHelper`, writing raw SQL, and parsing `Uris` with a `UriMatcher`.

**The Modern Approach:** While you still need a `ContentProvider` if you want to expose data to *other* apps, you no longer need to write raw SQL. You should use **Room**, Jetpack's modern SQLite Object Relational Mapper (ORM). 

If you need to share your Room database with other apps, Room provides a built-in annotation to generate the ContentProvider for you:

```kotlin
// Room automatically generates the ContentProvider implementation
@Database(entities = [User::class], version = 1)
@ProvideContentProvider(authority = "com.example.app.provider")
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}
```

### Content Provider Permissions
By default, a Content Provider is private to your app. To allow other apps to access it, you must declare it in your `AndroidManifest.xml` and specify permissions.

Since **Android 12 (API 31)**, you must explicitly declare whether the provider is `exported`.

```xml
<provider
    android:name=".MyContentProvider"
    android:authorities="com.example.app.provider"
    android:exported="true"
    android:readPermission="com.example.app.READ_DATA"
    android:writePermission="com.example.app.WRITE_DATA" />
```
*   `readPermission`: Other apps must request this permission to read your data.
*   `writePermission`: Other apps must request this permission to modify your data.

> **Security Alert:** Never set `android:exported="true"` without defining `readPermission` or `writePermission`. Doing so exposes your database to any malicious app on the device.

---

## C. Analogies and Use Cases

### Analogy: The Bank Vault
Think of your app's database as a bank vault. 
*   **You (The App):** Have the keys to the vault and can go in and out freely.
*   **ContentProvider:** The bank teller. The teller is the only person who interacts with the vault.
*   **ContentResolver:** A customer (another app) filling out a deposit/withdrawal slip.
*   **Content URI:** The account number on the slip.
*   **Permissions:** The customer must present an ID (runtime permission) before the teller will process the slip.

### Real-World Use Case: Custom Keyboard
A custom keyboard app needs to learn the names you type frequently to suggest them. The keyboard app queries the `ContactsContract` Content Provider to fetch your contact names securely, without ever having direct access to the raw database file.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   **Content Providers** manage access to a structured set of data and allow inter-process communication (IPC).
*   **Content URIs** act as the address for the data (`content://authority/path/id`).
*   **ContentResolver** is used by clients to perform CRUD operations.
*   **Room Database** is the modern standard for local storage and can automatically generate the underlying `ContentProvider` if you need to share data.
*   **Security** is paramount; always use `readPermission`/`writePermission` and `android:exported`.

### Frequently Asked Questions

**1. Is the adapter a required component?**
*(Wait, this is from Module 20!)* 
For this module: Is a Content Provider required? **No.** Only use a Content Provider if you need to share data with *other applications* (like sharing data with a Wear OS watch or a widget). For storing data privately inside your own app, use **Room** or **DataStore** directly without a Content Provider.

**2. Why does `query()` return a `Cursor` instead of a List?**
A `Cursor` is a pointer to the result set. It is designed to be memory-efficient by loading rows one by one as you iterate through them, rather than loading the entire database table into memory at once.

**3. What is the difference between `getContentResolver().insert()` and a Room `@Insert`?**
`ContentResolver` is used to communicate across app boundaries (IPC). Room `@Insert` is used for fast, local database operations within your own app.

**4. Do I need to write SQL to create a Content Provider?**
No. If you use Room to manage your database, Room can generate the boilerplate `ContentProvider` code for you using the `@ProvideContentProvider` annotation.

**5. How do I parse a `Cursor` safely?**
Always use the `.use { }` block (as shown in the Kotlin example above). This ensures the Cursor is closed automatically after you are done reading from it, preventing memory leaks.

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Consuming the Contacts Provider

**The Task:** Build a Compose screen that requests Contacts permission and displays the first 10 contacts in a list.

**Step 1: Update `AndroidManifest.xml`**
```xml
<uses-permission android:name="android.permission.READ_CONTACTS" />
```

**Step 2: Create the Compose UI**
```kotlin
import android.Manifest
import android.content.pm.PackageManager
import android.provider.ContactsContract
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.core.content.ContextCompat
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

@Composable
fun ContactsScreen() {
    val context = LocalContext.current
    var contacts by remember { mutableStateOf(listOf<String>()) }
    var hasPermission by remember {
        mutableStateOf(
            ContextCompat.checkSelfPermission(context, Manifest.permission.READ_CONTACTS) 
            == PackageManager.PERMISSION_GRANTED
        )
    }

    val permissionLauncher = rememberLauncherForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { isGranted ->
        hasPermission = isGranted
    }

    LaunchedEffect(hasPermission) {
        if (hasPermission) {
            // Fetch contacts off the main thread
            contacts = withContext(Dispatchers.IO) {
                val contactList = mutableListOf<String>()
                val cursor = context.contentResolver.query(
                    ContactsContract.Contacts.CONTENT_URI,
                    arrayOf(ContactsContract.Contacts.DISPLAY_NAME),
                    null, null, null
                )
                cursor?.use {
                    while (it.moveToNext() && contactList.size < 10) {
                        contactList.add(it.getString(0) ?: "Unknown")
                    }
                }
                contactList
            }
        }
    }

    if (!hasPermission) {
        Column(
            modifier = Modifier.fillMaxSize(),
            verticalArrangement = Arrangement.Center
        ) {
            Button(
                onClick = { permissionLauncher.launch(Manifest.permission.READ_CONTACTS) },
                modifier = Modifier.padding(16.dp)
            ) {
                Text("Grant Contacts Permission")
            }
        }
    } else {
        LazyColumn {
            items(contacts) { contact ->
                Text(
                    text = contact,
                    modifier = Modifier.padding(16.dp)
                )
                HorizontalDivider()
            }
        }
    }
}
```

---

## F. Skill-Building Check

**1. What is the primary purpose of a Content Provider?**
A) To style the UI.
B) To manage and share structured data across different applications securely.
C) To handle network requests.
D) To schedule background tasks.
> **Correct Answer: B** (Content Providers manage access to a structured set of data and facilitate Inter-Process Communication.)

**2. Which component is used by a client app to access data from a Content Provider?**
A) `ContentProvider`
B) `ContentResolver`
C) `SQLiteDatabase`
D) `CursorLoader`
> **Correct Answer: B** (`ContentResolver` is used by the client to query or modify data.)

**3. In the URI `content://com.example.provider/users/5`, what does `users` represent?**
A) The Authority
B) The Scheme
C) The Path (Directory)
D) The specific ID
> **Correct Answer: C** (`users` is the optional path indicating the type of data.)

**4. Which method is used to add a new record using a `ContentResolver`?**
A) `add()`
B) `insert()`
C) `create()`
D) `put()`
> **Correct Answer: B** (`insert()` adds a new row to the provider.)

**5. True or False: By default, a Content Provider is accessible by any app on the device.**
A) True
B) False
> **Correct Answer: B (False)** (By default, providers are private. You must explicitly export them and define permissions.)

**6. What modern Jetpack library can automatically generate a Content Provider for your SQLite database?**
A) DataStore
B) Room
C) WorkManager
D) Navigation
> **Correct Answer: B** (Room can generate a ContentProvider using the `@ProvideContentProvider` annotation.)

**7. What is a `Cursor` in the context of Content Providers?**
A) A UI element.
B) A pointer that allows efficient iteration over a result set from a database query.
C) A network request.
D) A permission level.
> **Correct Answer: B** (A Cursor points to the results of a query, allowing you to read rows one by one.)

**8. Since Android 12 (API 31), what attribute must be explicitly declared for all providers in the manifest?**
A) `android:authorities`
B) `android:exported`
C) `android:permission`
D) `android:name`
> **Correct Answer: B** (`android:exported` must be explicitly set to `true` or `false` to declare if the provider can be accessed by other apps.)