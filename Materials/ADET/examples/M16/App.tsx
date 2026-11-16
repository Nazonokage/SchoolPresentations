import { useState } from "react";
import { View, Text, Button } from "react-native";

export default function App() {
  const [msg, say] = useState("");
  async function suggest() {
    try {
      const r = await fetch(
        (process.env.EXPO_PUBLIC_API_URL ?? "http://localhost:8000") +
          "/suggest",
      );
      if (!r.ok) throw Error();
      const value = await r.json();
      if (typeof value.tip !== "string") throw Error();
      say("Server: " + value.tip);
    } catch {
      say("Offline: review your first unfinished task.");
    }
  }
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Button title="Get a study suggestion" onPress={suggest} />
      <Text>{msg}</Text>
    </View>
  );
}
