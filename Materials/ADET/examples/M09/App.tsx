import { useState } from "react";
import { View, Text, Button, TextInput } from "react-native";
import Storage from "@react-native-async-storage/async-storage";
export default function App() {
  const [draft, set] = useState("");
  const [msg, say] = useState("");
  async function store(save: boolean) {
    try {
      if (save) {
        await Storage.setItem("campus.draft", draft);
        say("Saved on device");
      } else {
        set((await Storage.getItem("campus.draft")) ?? "");
        say("Loaded");
      }
    } catch (e) {
      say(String(e));
    }
  }
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <TextInput placeholder="Draft" value={draft} onChangeText={set} />
      <Button title="Save draft" onPress={() => store(true)} />
      <Button title="Restore draft" onPress={() => store(false)} />
      <Text>{msg}</Text>
    </View>
  );
}
