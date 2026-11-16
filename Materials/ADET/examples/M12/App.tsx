import { useState } from "react";
import { View, Text, Button, Image } from "react-native";
import * as Picker from "expo-image-picker";
export default function App() {
  const [uri, set] = useState("");
  const [msg, say] = useState("");
  async function camera() {
    try {
      const p = await Picker.requestCameraPermissionsAsync();
      if (!p.granted) {
        say("Camera denied. Continue without a photo.");
        return;
      }
      const result = await Picker.launchCameraAsync({ quality: 0.5 });
      if (!result.canceled) set(result.assets[0].uri);
    } catch (e) {
      say(String(e));
    }
  }
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Button title="Take campus photo" onPress={camera} />
      {uri !== "" && (
        <Image
          source={{ uri }}
          accessibilityLabel="Selected photo"
          style={{ width: 180, height: 180 }}
        />
      )}
      <Button title="Remove" onPress={() => set("")} />
      <Text>{msg}</Text>
    </View>
  );
}
