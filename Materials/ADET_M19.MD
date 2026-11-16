Here is the modernized, 2026-ready version of Module 19, updated to reflect the shift from legacy `MediaPlayer` to **Jetpack Media3 (ExoPlayer)** and **Jetpack Compose**.

---

# Android Multimedia: Modern Audio & Video Playback with Jetpack Media3

## A. Lesson Preview & Review

Multimedia captivates users, but how your app handles media dictates the experience. Historically, `MediaPlayer` and `VideoView` were the go-to classes. However, they are now legacy. Today, **Jetpack Media3** is the modern standard.

Media3 provides a consistent, cross-process architecture featuring **ExoPlayer** for playback, **MediaSession** for communicating with system components (like notifications and lockscreens), and **Compose UI modules** for building beautiful player interfaces.

> **Quick Recap:** We are moving from imperative `MediaPlayer` objects to a declarative, state-driven architecture using `ExoPlayer` and Jetpack Compose.

**Learning Targets:**
1.  Understand the shift from `MediaPlayer`/`VideoView` to **ExoPlayer**.
2.  Build a Compose-native video player using `media3-ui-compose-material3`.
3.  Implement proper lifecycle management using `DisposableEffect`.
4.  Understand the modern **MediaSessionService** architecture for background audio playback.

![Smartphone playing a video](https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?auto=format&fit=crop&q=80&w=1000)

---

## B. Main Lesson

### 1. The Modern Media Stack: Why Media3?
The standalone ExoPlayer library (`com.google.android.exoplayer2`) is discontinued, and the legacy `MediaPlayer` API lacks advanced features like adaptive streaming (DASH, HLS) and is not lifecycle-aware.

**Jetpack Media3** solves this:
*   **Consistent API:** Same ExoPlayer engine for local files and streaming.
*   **Compose First:** The `media3-ui-compose-material3` module provides pre-built Compose components (play/pause buttons, progress bars, shutter screens).
*   **Lifecycle-Aware:** Designed to be tied to Compose’s lifecycle using `remember` and `DisposableEffect`.

**Dependencies to add:**
```kotlin
implementation("androidx.media3:media3-exoplayer:1.10.0")
implementation("androidx.media3:media3-ui-compose-material3:1.10.0")
```

### 2. Building a Video Player in Compose
The modern approach uses the `Player` composable from the `media3-ui-compose` module. It handles state (playing, buffering, ended) automatically.

```kotlin
import android.net.Uri
import androidx.compose.runtime.*
import androidx.compose.ui.platform.LocalContext
import androidx.media3.common.MediaItem
import androidx.media3.exoplayer.ExoPlayer
import androidx.media3.ui.compose.material3.Player

@Composable
fun VideoPlayerScreen(videoUri: String) {
    val context = LocalContext.current
    
    // 1. Create and remember the ExoPlayer instance
    val exoPlayer = remember {
        ExoPlayer.Builder(context).build().apply {
            setMediaItem(MediaItem.fromUri(Uri.parse(videoUri)))
            prepare()
        }
    }

    // 2. Release the player when the composable leaves the screen
    DisposableEffect(Unit) {
        onDispose {
            exoPlayer.release()
        }
    }

    // 3. Render the Compose Player UI
    Player(
        player = exoPlayer,
        modifier = Modifier.fillMaxSize()
    )
}
```

### 3. Modern Background Audio & Audio Focus
To play audio in the background (e.g., a podcast or music app), you **must not** use a simple service. The modern standard is `MediaSessionService` from Media3.

This service automatically handles:
*   **MediaSession:** Allows system components (Bluetooth headsets, Android Auto, notifications) to control playback.
*   **Foreground Service:** Keeps playback alive when the app is minimized.
*   **Audio Focus:** Automatically pauses playback when a phone call comes in or another app plays audio, avoiding audio clashing.

### 4. The Deprecation of `AudioManager.setRingerMode`
The legacy material teaches `AudioManager.setRingerMode(AudioManager.RINGER_MODE_VIBRATE)`. **This is heavily restricted.**

Since Android 6.0 (API 23), toggling Silent or Vibrate modes requires the user to grant your app **Do Not Disturb Access** (a special permission in Settings). Without it, `setRingerMode` calls are **silently ignored**.

**Modern Approach:** Instead of changing the system ringer mode, use the **Audio Focus API** (`AudioFocusRequest`) to request temporary focus for your media playback. When you gain focus, you play your audio; when you lose focus, you pause or lower your volume.

---

## C. Analogies and Use Cases

### Analogy: The Modern Theater vs. The Old Projection Booth
*   **Legacy (`MediaPlayer` + `VideoView`):** You manually threaded the film, turned the projector crank, and handled every button yourself. If the power went out (backgrounded), the film stopped.
*   **Media3 (`ExoPlayer` + `Player` Composable):** You press "Play" on a smart TV. The TV automatically handles buffering, volume control, pausing when a phone call comes in, and displaying the remote control UI. You just supply the video link.

### Real-World Use Case: The Podcast App
When a user taps play on a podcast and locks their phone, the app uses `MediaSessionService`. The service keeps the audio playing. The user can pause the podcast directly from the lock screen using the `MediaSession` metadata. If the user receives a phone call, the service handles the audio focus loss and pauses the podcast automatically.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   **Jetpack Media3** is the current standard for audio and video playback, replacing `MediaPlayer` and legacy ExoPlayer.
*   **Compose UI:** Use `media3-ui-compose-material3` for a declarative player UI.
*   **Lifecycle:** Always release the `ExoPlayer` in a `DisposableEffect` to prevent memory leaks.
*   **Background Audio:** Use `MediaSessionService`, not a standard background service.
*   **Ringer Mode:** `setRingerMode` requires Do Not Disturb permission and is discouraged for general apps.

### Frequently Asked Questions

**1. Why can't I use `MediaPlayer` anymore?**
You *can* use it, but it is legacy. It lacks support for modern adaptive streaming and does not integrate well with Compose. Media3 is faster, more extensible, and actively maintained.

**2. Does `media3-ui-compose-material3` require the old `media3-ui` module?**
No. As of Media3 1.6.0, the Compose UI modules are decoupled and recommended for new Compose apps.

**3. How do I handle the media playback lifecycle in Compose?**
Use `remember` to create the `ExoPlayer` and `DisposableEffect(Unit) { onDispose { player.release() } }` to clean it up when the composable is destroyed.

**4. Can I still use `VideoView`?**
`VideoView` is a legacy View-based component. While you can host it in Compose using `AndroidView`, you miss out on the state-driven benefits of the `Player` composable.

**5. What is the difference between `ExoPlayer` and `MediaSessionService`?**
`ExoPlayer` is the engine that decodes and renders media. `MediaSessionService` is a wrapper that binds the `ExoPlayer` to a background service, exposing it to system-level controls (lockscreen, notifications, Bluetooth).

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Audio Player with Progress Bar

**The Task:** Create a simple audio player that displays a play/pause button and a progress bar using Media3 and Compose.

**Step 1: Add Dependencies**
```kotlin
implementation("androidx.media3:media3-exoplayer:1.10.0")
implementation("androidx.media3:media3-ui-compose-material3:1.10.0")
```

**Step 2: Create the Compose UI**
```kotlin
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.media3.common.MediaItem
import androidx.media3.exoplayer.ExoPlayer
import androidx.media3.ui.compose.material3.PlayPauseButton
import androidx.media3.ui.compose.material3.PositionAndDurationText

@Composable
fun AudioPlayerScreen(audioUri: String) {
    val context = LocalContext.current
    var isPlaying by remember { mutableStateOf(false) }

    val exoPlayer = remember {
        ExoPlayer.Builder(context).build().apply {
            setMediaItem(MediaItem.fromUri(audioUri))
            prepare()
            addListener(object : Player.Listener {
                override fun onIsPlayingChanged(playing: Boolean) {
                    isPlaying = playing
                }
            })
        }
    }

    DisposableEffect(Unit) {
        onDispose { exoPlayer.release() }
    }

    Column(
        modifier = Modifier.fillMaxSize(),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        // Pre-built Play/Pause button from Media3
        PlayPauseButton(
            player = exoPlayer,
            modifier = Modifier.size(64.dp)
        )
        
        Spacer(modifier = Modifier.height(16.dp))
        
        // Pre-built position and duration text
        PositionAndDurationText(player = exoPlayer)
    }
}
```

---

## F. Skill-Building Check

**1. What is the modern replacement for the standalone `MediaPlayer` and legacy ExoPlayer?**
A) `VideoView`
B) `AudioManager`
C) `Jetpack Media3`
D) `MediaController`
> **Correct Answer: C** (Jetpack Media3 is the current standard, providing a unified API for playback and UI.)

**2. Which module provides pre-built Material 3 Compose components for media playback?**
A) `media3-exoplayer`
B) `media3-ui-compose-material3`
C) `media3-session`
D) `compose-media`
> **Correct Answer: B** (`media3-ui-compose-material3` provides the `Player`, `PlayPauseButton`, and other Compose UI elements.)

**3. What is the correct way to handle `ExoPlayer` cleanup in Compose?**
A) Call `player.stop()` in `onDestroy()`.
B) Use `DisposableEffect` and call `player.release()` in `onDispose`.
C) Let the garbage collector handle it.
D) Use a `LaunchedEffect` to release the player.
> **Correct Answer: B** (Using `DisposableEffect` ensures the player is released when the composable leaves the screen.)

**4. True or False: You should use `AudioManager.setRingerMode` to toggle the device into silent mode from your media app.**
A) True
B) False
> **Correct Answer: B (False)** (This method requires Do Not Disturb access and is silently ignored for most apps. Use the Audio Focus API instead.)

**5. What is required to play audio in the background and display media controls on the lock screen?**
A) A simple background Service.
B) `MediaSessionService`.
C) A `BroadcastReceiver`.
D) `AsyncTask`.
> **Correct Answer: B** (`MediaSessionService` handles the media session, foreground service, and system-level controls.)

**6. Which of the following is NOT a feature supported by Media3's ExoPlayer?**
A) Adaptive streaming (DASH, HLS).
B) SmoothStreaming.
C) Common Encryption.
D) Modifying system ringtone settings.
> **Correct Answer: D** (ExoPlayer is for playback; modifying system ringtone settings is a separate API and heavily restricted.)

**7. What is the primary difference between `ExoPlayer` and `MediaSessionService`?**
A) `ExoPlayer` is for video, `MediaSessionService` is for audio.
B) `ExoPlayer` decodes media; `MediaSessionService` exposes playback to the system for background and lockscreen controls.
C) `ExoPlayer` is deprecated; `MediaSessionService` is the replacement.
D) There is no difference.
> **Correct Answer: B** (`ExoPlayer` is the engine, while `MediaSessionService` is the service wrapper for system integration.)

**8. Which API should you use to gracefully handle interruptions (like a phone call) during audio playback?**
A) `AudioManager.setRingerMode`
B) `AudioFocusRequest`
C) `MediaPlayer.pause()`
D) `BroadcastReceiver` for phone state
> **Correct Answer: B** (`AudioFocusRequest` is the modern API for requesting audio focus and handling interruptions.)