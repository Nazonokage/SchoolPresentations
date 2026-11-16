import { useState } from "react";
import { View, Text, Button } from "react-native";
import * as SecureStore from "expo-secure-store";
export default function App() {
  const [msg, say] = useState("Signed out");
  async function session(action: string) {
    try {
      if (action === "login")
        await SecureStore.setItemAsync("demoActor", "ana");
      if (action === "logout") await SecureStore.deleteItemAsync("demoActor");
      const actor = await SecureStore.getItemAsync("demoActor");
      say(
        action === "read"
          ? actor === "ben"
            ? "Record opened"
            : "Denied: Ben owns this record"
          : (actor ?? "Signed out"),
      );
    } catch (e) {
      say(String(e));
    }
  }
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Text>Local session model</Text>
      {["login", "read", "logout"].map((x) => (
        <Button key={x} title={x} onPress={() => session(x)} />
      ))}
      <Text>{msg}</Text>
    </View>
  );
}
