# ADET M15 · Audio, video and app performance

[Module index](README.md) · Pre-final · 60–90 minutes · 10-item quiz

## A. Lesson Preview & Review

**Can a study-timer cue still make sense on mute?** Recall M13: the system controls timing. Today the system also controls sound, volume and focus.

**Learning targets:** play a bundled sound, follow player status, give a visible cue for a sound, and diagnose slowness by measuring before optimizing.

**Trace:** Bundled WAV → Player → Status → Visible cue. Explain in your own words: Play makes the local cue and shows "playing" for a moment; pause or finishing returns the label to "idle".

## B. Detailed Main Lesson

### In plain words

An audio player loads a sound file and plays, pauses and rewinds it. The label on screen should follow what the player really reports, not the last button pressed. A sound alone is not enough: a student on mute still needs to see what happened.

| Concept | Why it exists / how it works | If misunderstood |
|---|---|---|
| Bundled asset | `require("./tone.wav")` ships with the app, so it works offline | A remote file that fails with no network |
| Player and status | `useAudioPlayer` manages the source; `useAudioPlayerStatus` reports `playing` | Guessing state from button presses |
| Rewind | `seekTo(0)` before `play()`, otherwise Play resumes after Pause | "Play" seems to do nothing at the end |
| Cleanup | The hook ties the player to the screen | Sounds that keep playing after leaving |
| Accessible cue | A visible status or transcript carries the same meaning | Sound-only information |
| Measure first | Compare dev and release on the same device; change one thing | Memoizing everything "to be fast" |

```text
Play -> seekTo(0) -> play() -> status.playing = true  -> label "playing"
Pause -> pause()              -> status.playing = false -> label "idle"
```

**Predict first:** press Play twice quickly. Where does the second press start?

| Action | Label | Reason |
|---|---|---|
| Play | playing | Started from 0 |
| Pause | idle | Suspended |
| Play | playing | Rewound, then started |
| Sound ends | idle | Status changed |

Video has its own player and view; a remote stream adds buffering, errors and data cost, and speech needs captions or a transcript. Use `expo-audio` and `expo-video`, not the deprecated `expo-av`. For performance, large images and needless list updates often cost more than the text around them.

**Misconception:** "if the label says playing, I should hear it." Silent mode, volume, audio focus and the output route can all mute playback.

### Common mistakes

- Showing state from the last tap instead of the player status.
- Optimizing without a measurement.
- Giving information by sound only.

## C. Analogy, Guided Program & Practice

**Analogy.** Puwedeng marinig o makita ang cue. Parang ilaw at kampana sa classroom: kung bingi ang kampana, ilaw ang nagsasabi na tapos na ang oras.

**Use case:** a study timer that must also work on mute.

**Install first (online):**

```powershell
npx expo install expo-audio
```

The sound file is [tone.wav](../examples/M15/tone.wav); put it next to `App.tsx`. This package is expected to work in Expo Go, but that has not yet been tested on the course baseline.

**Run it.** Copy this lesson's complete `App.tsx` into your prepared project from M01 (replace the whole file). Run `npx tsc --noEmit`, then `npx expo start --offline` in the prepared lab or `npx expo start` while online. Metro transpiles; it does not type-check. Course versions are recorded in M01.

**Lab note.** Quiz modules do not need a delivery mode. Demonstrate on one physical device, or trace the table above.

**App.tsx — complete checkpoint** · [Copyable file](../examples/M15/App.tsx)

```tsx
import { View, Text, Button } from "react-native";
import { useAudioPlayer, useAudioPlayerStatus } from "expo-audio";

export default function App() {
  const player = useAudioPlayer(require("./tone.wav"));
  const status = useAudioPlayerStatus(player);

  async function playCue() {
    await player.seekTo(0); // rewind first, otherwise Play would resume after Pause
    player.play();
  }

  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      {/* The label follows the player status, so it still helps when muted */}
      <Text>Study timer sound • {status.playing ? "playing" : "idle"}</Text>
      <Button title="Play cue" onPress={playCue} />
      <Button title="Pause" onPress={() => player.pause()} />
    </View>
  );
}
```

**Breakdown.** `useAudioPlayer` loads the bundled tone. `useAudioPlayerStatus` reports whether it is playing. `playCue` rewinds, then plays. The label reads `status.playing`.

**Expected behavior.** Play produces the local cue and a "playing" label. Pause or completion returns the label to "idle".

**Ungraded practice.** Add a clear accessible status and compare behavior when switching apps.

**Troubleshooting.** If playback succeeds but is inaudible, inspect silent mode, volume, audio focus and the output route.

## D. Assessment, Wrap-Up & References

### 10-item quiz

Give a short answer for each item. The guided change above is ungraded.

1. What does an audio player manage?
2. Why is the cue bundled locally?
3. What does `seekTo(0)` do?
4. What does pressing Play do after the rewind?
5. Which label shows active playback?
6. What does Pause request?
7. The label says "playing" but you hear nothing. What do you inspect?
8. Why can development timing misrepresent performance?
9. How should you evaluate a list optimization?
10. How can a sound-only cue be made more accessible?

**Answer key (instructor).**
1. Loading, playing, pausing and rewinding one audio source.
2. It works offline and needs no network.
3. Moves playback to the start.
4. Starts playing from the start.
5. "playing".
6. Suspend playback and keep the position.
7. Silent mode, volume, audio focus and output route.
8. Development mode adds extra checks; measure a release build.
9. Measure before and after on the same device and build.
10. Add a visible status and a transcript or captions.

**Wrap-up.** Explain how a tap becomes sound and a visible label, and why the label comes from the player status. Name the layer you would inspect first if it said "playing" with no sound.

[expo-audio](https://docs.expo.dev/versions/latest/sdk/audio/)

### Instructor notes

Pacing: 5 review, 15 explanation, 10 demo, 25 quiz, 5 wrap-up. Keep performance as measurement practice, not a package. Device behavior is not yet recorded on the course baseline.
