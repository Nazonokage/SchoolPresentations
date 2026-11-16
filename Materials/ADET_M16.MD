Here is the updated and modernized version of Module 16, revised to align with current Android development standards.

---

# Android Location-Based Services: Modern Google Maps Integration

---

## A. Lesson Preview & Review

Google Maps is a one-of-a-kind web-based mapping capability. It offers almost all mapping features, including satellite imagery, aerial photography, street maps, 360° panoramic views of streets, real-time traffic conditions, and route planning.

Historically, integrating Maps into Android required embedding a `MapFragment` directly into an XML layout. Today, the modern standard is to use the **Maps Compose library**, which provides native Kotlin composables for map rendering, allowing you to build map UIs declaratively.

> **Quick Recap:** In previous modules, you learned about Intents, Layouts, and modern UI with Jetpack Compose. This module combines those skills to integrate a complex third-party SDK into a Compose-first application.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Secure your Google Maps API key using the **Secrets Gradle plugin**.
2.  Integrate the **Maps Compose** library into your project.
3.  Display a map, add markers, and control the camera using Composable functions.
4.  Understand modern location permission requirements.

![Google Maps on a smartphone screen](https://images.unsplash.com/photo-1524661135-423995f22d0b?auto=format&fit=crop&q=80&w=800)

---

## B. Main Lesson

### Under the Hood: How Google Maps Works
Google Maps uses a combination of GPS data, user input, and real-time traffic data to provide accurate information. Behind the scenes, it relies on several advanced algorithms:
*   **Image Recognition & Machine Learning:** Extracts useful information from satellite and street view images to identify roads, buildings, and landmarks.
*   **Geospatial Data Analysis:** Uses GIS techniques to analyze the earth's surface.
*   **Dijkstra's Algorithm & A* Search:** Classic graph algorithms used to determine the shortest path between two points.

### Key Components and Features
*   **Base Partner Data:** Partners provide up-to-date business info and points of interest.
*   **Satellites & Street View:** High-resolution imagery and 360° panoramic views.
*   **Live Crowd Data:** Real-time traffic conditions from users with location tracking enabled.
*   **Map Types:** Standard, Satellite, Terrain, and Hybrid views.

### Setting Up Google Maps in a Compose Project

#### Step 1: Get an API Key
You need a Google Maps API key. Go to the Google Cloud Console, create a project, and enable the **Maps SDK for Android**. Generate an API key and restrict it to your app's package name and SHA-1 fingerprint for security.

#### Step 2: Secure the API Key (Modern Best Practice)
**Never hardcode your API key in `AndroidManifest.xml`.** Google strongly recommends using the **Secrets Gradle plugin** to read the key from a local file.

1.  **Add the plugin** to your root `build.gradle.kts`:
    ```kotlin
    plugins {
        id("com.google.android.libraries.mapsplatform.secrets-gradle-plugin") version "2.0.1" apply false
    }
    ```
2.  **Apply the plugin** in your app-level `build.gradle.kts`:
    ```kotlin
    plugins {
        id("com.google.android.libraries.mapsplatform.secrets-gradle-plugin")
    }
    ```
3.  **Store the key** in `local.properties` (which is not checked into version control):
    ```properties
    MAPS_API_KEY=YOUR_API_KEY_HERE
    ```
4.  **Reference the key** in `AndroidManifest.xml` inside the `<application>` tag:
    ```xml
    <meta-data
        android:name="com.google.android.geo.API_KEY"
        android:value="${MAPS_API_KEY}" />
    ```

#### Step 3: Add Dependencies
Add the Maps Compose library to your app-level `build.gradle.kts`:
```kotlin
dependencies {
    implementation("com.google.maps.android:maps-compose:6.2.1")
    implementation("com.google.android.gms:play-services-maps:19.0.0")
}
```

### Implementing the Map in Compose
The **`GoogleMap`** composable is the core entry point. It automatically manages the map lifecycle, so you don't need to manually handle `onCreate`, `onResume`, etc.

**Key Concepts:**
*   **`CameraPositionState`:** Controls the camera (center coordinate and zoom level). Created using `rememberCameraPositionState`.
*   **`Marker`:** A composable to place a pin on the map.
*   **`MapUiSettings`:** Configures UI elements like zoom controls and compass visibility.

```kotlin
import androidx.compose.runtime.*
import com.google.android.gms.maps.model.CameraPosition
import com.google.android.gms.maps.model.LatLng
import com.google.maps.android.compose.*

@Composable
fun SimpleMap() {
    // 1. Define the camera position
    val sydney = LatLng(-33.8688, 151.2093)
    val cameraPositionState = rememberCameraPositionState {
        position = CameraPosition.fromLatLngZoom(sydney, 10f)
    }

    // 2. Render the Map
    GoogleMap(
        modifier = Modifier.fillMaxSize(),
        cameraPositionState = cameraPositionState,
        properties = MapProperties(isBuildingEnabled = true),
        uiSettings = MapUiSettings(zoomControlsEnabled = true)
    ) {
        // 3. Add a Marker
        Marker(
            state = rememberMarkerState(position = sydney),
            title = "Sydney",
            snippet = "A beautiful city"
        )
    }
}
```

### Location Permissions
If you need the user's current location (not just a static map), you must request runtime permissions:
*   **`ACCESS_COARSE_LOCATION`:** For approximate location.
*   **`ACCESS_FINE_LOCATION`:** For precise GPS location.

> **Best Practice:** Request permissions contextually. Use the **Accompanist Permissions** library (or modern `rememberLauncherForActivityResult`) to request location access only when the user interacts with a "Find Me" button, rather than on app launch.

---

## C. Analogies and Use Cases

### Analogy: The Digital Canvas
Think of the `GoogleMap` composable as a blank digital canvas. The `CameraPositionState` is your viewport (where you are looking). The `Marker` composables are stickers you place on the canvas. Just as you would compose a painting with different elements, you compose your map with markers, circles, and UI controls.

### Real-World Use Case: Real Estate App
A real estate app uses Maps Compose to display property listings. When a user taps a property, a Marker is placed on the map. The app uses `cameraPositionState.animate()` to smoothly pan and zoom to the selected property. It also uses `Circle` composables to show the "walkability score" radius around each listing.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   **Maps Compose** is the modern, declarative way to integrate Google Maps.
*   **API Key Security:** Never hardcode your API key; use the Secrets Gradle plugin and `local.properties`.
*   **Camera Control:** Use `rememberCameraPositionState` to control the map's center and zoom.
*   **Markers & Shapes:** Use `Marker`, `Circle`, `Polygon`, and `Polyline` composables to add overlays.
*   **Lifecycle:** The `GoogleMap` composable handles its own lifecycle automatically.

### Frequently Asked Questions

**1. Do I need a billing account to use Google Maps?**
Yes, Google Maps Platform requires a billing account. However, you get a $200 monthly credit, which is typically sufficient for development and small apps.

**2. Can I use Google Maps without an API key?**
No. The Maps SDK requires a valid API key to render the map tiles and fetch data.

**3. What is the difference between `MapProperties` and `MapUiSettings`?**
`MapProperties` configures the map's data and appearance (e.g., `isBuildingEnabled`, `mapType`). `MapUiSettings` configures the interactive UI elements (e.g., `zoomControlsEnabled`, `compassEnabled`).

**4. How do I get the user's current location?**
You need to request the `ACCESS_FINE_LOCATION` permission. Once granted, use the `FusedLocationProviderClient` (from Google Play Services Location) to get the last known location, then animate the camera to that position.

**5. Does Maps Compose work with XML layouts?**
The Maps Compose library is designed for Jetpack Compose. However, you can use `AndroidView` in Compose to wrap the traditional `MapFragment` if you are migrating incrementally.

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Multi-Marker Map

**The Task:** Create a Compose map that displays three markers for different landmarks and provides a button to zoom to fit all markers.

**Implementation:**

```kotlin
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.google.android.gms.maps.model.CameraPosition
import com.google.android.gms.maps.model.LatLng
import com.google.maps.android.compose.*

@Composable
fun MultiMarkerMap() {
    val landmarks = listOf(
        LatLng(40.7128, -74.0060), // New York
        LatLng(34.0522, -118.2437), // Los Angeles
        LatLng(41.8781, -87.6298)  // Chicago
    )

    val cameraPositionState = rememberCameraPositionState {
        position = CameraPosition.fromLatLngZoom(landmarks[0], 5f)
    }
    val scope = rememberCoroutineScope()

    Column {
        Button(
            onClick = {
                // Animate camera to fit all markers
                scope.launch {
                    cameraPositionState.animate(
                        update = CameraUpdateFactory.newLatLngZoom(landmarks[0], 4f),
                        durationMs = 1000
                    )
                }
            },
            modifier = Modifier.padding(16.dp)
        ) {
            Text("Zoom to View All")
        }

        GoogleMap(
            modifier = Modifier.fillMaxSize(),
            cameraPositionState = cameraPositionState
        ) {
            landmarks.forEachIndexed { index, latLng ->
                Marker(
                    state = rememberMarkerState(position = latLng),
                    title = "Landmark ${index + 1}"
                )
            }
        }
    }
}
```

---

## F. Skill-Building Check

**1. What is the modern, recommended library for integrating Google Maps into a Compose app?**
A) `MapFragment` XML
B) Maps Compose library
C) Google Maps JavaScript API
D) Android Maps SDK v1
> **Correct Answer: B** (Maps Compose provides native composable functions for map UI.)

**2. Where should you store your Google Maps API key for security?**
A) Directly in `AndroidManifest.xml`
B) In a public GitHub repository
C) In `local.properties` and referenced via the Secrets Gradle plugin
D) In `strings.xml`
> **Correct Answer: C** (The Secrets Gradle plugin reads the key from `local.properties`, keeping it out of version control.)

**3. Which composable is used to control the map's center and zoom level?**
A) `rememberCameraPositionState`
B) `Marker`
C) `GoogleMap`
D) `MapProperties`
> **Correct Answer: A** (`rememberCameraPositionState` creates and remembers the camera state.)

**4. What does `MapUiSettings` control?**
A) The map's data source
B) The map's color scheme
C) UI elements like zoom controls and compass
D) The map's lifecycle
> **Correct Answer: C** (`MapUiSettings` configures interactive UI elements.)

**5. Which permission is required for precise GPS location?**
A) `ACCESS_COARSE_LOCATION`
B) `ACCESS_FINE_LOCATION`
C) `INTERNET`
D) `ACCESS_NETWORK_STATE`
> **Correct Answer: B** (`ACCESS_FINE_LOCATION` is needed for precise GPS.)

**6. True or False: The `GoogleMap` composable automatically manages the map's lifecycle.**
A) True
B) False
> **Correct Answer: A (True)** (The Maps Compose library handles `onCreate`, `onResume`, etc., automatically.)

**7. What algorithm is classically used to determine the shortest path between two points on a graph?**
A) Bubble Sort
B) Dijkstra's Algorithm
C) Binary Search
D) K-Means Clustering
> **Correct Answer: B** (Dijkstra's algorithm is a classic shortest-path algorithm.)

**8. How do you add a marker to a `GoogleMap` composable?**
A) By calling `map.addMarker()`
B) By using the `Marker` composable inside the `GoogleMap` content block
C) By editing the XML layout
D) By using `MapProperties`
> **Correct Answer: B** (The `Marker` composable is placed inside the `GoogleMap` block to define markers declaratively.)