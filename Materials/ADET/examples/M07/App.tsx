import { useState } from "react";
import { View, Text, Button } from "react-native";

export default function App() {
  const [msg, say] = useState("Tap Load");
  async function load() {
    say("Loading…");
    try {
      const res = await fetch(
        (process.env.EXPO_PUBLIC_API_URL ?? "http://localhost:8000") + "/tasks",
      );
      if (!res.ok) throw Error("HTTP " + res.status);
      const rows: unknown = await res.json();
      if (
        !Array.isArray(rows) ||
        !rows.every((x) => typeof x?.title === "string")
      )
        throw Error("Invalid list");
      say(rows.map((x) => x.title).join(", ") || "No tasks yet");
    } catch (e) {
      say(String(e));
    }
  }
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Button title="Load campus tasks" onPress={load} />
      <Text>{msg}</Text>
    </View>
  );
}
