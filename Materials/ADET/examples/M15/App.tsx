import { View, Text, Button } from "react-native";
import { useAudioPlayer, useAudioPlayerStatus } from "expo-audio";
export default function App() {
  const player = useAudioPlayer(require("./tone.wav"));
  const status = useAudioPlayerStatus(player);
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Text>Study timer sound • {status.playing ? "playing" : "idle"}</Text>
      <Button
        title="Play cue"
        onPress={async () => {
          await player.seekTo(0);
          player.play();
        }}
      />
      <Button title="Pause" onPress={() => player.pause()} />
    </View>
  );
}
