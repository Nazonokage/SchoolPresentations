import { useEffect, useState } from "react";
import { View, Text, Button, TextInput } from "react-native";

export default function App() {
  const [title, set] = useState("");
  const [msg, say] = useState("");
  useEffect(() => {
    if (!msg) return;
    const timer = setTimeout(() => say(""), 4000);
    return () => clearTimeout(timer);
  }, [msg]);
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <TextInput
        accessibilityLabel="Task title"
        placeholder="Task title"
        value={title}
        onChangeText={set}
      />
      <Text>{title.length} characters</Text>
      <Button
        title="Save"
        onPress={() =>
          say(title.trim() ? "Saved: " + title.trim() : "Enter a title")
        }
      />
      <Text accessibilityLiveRegion="polite">{msg}</Text>
    </View>
  );
}
