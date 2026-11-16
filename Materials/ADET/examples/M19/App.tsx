import { useState } from "react";
import { View, Text, Button, TextInput } from "react-native";

export default function App() {
  const [input, edit] = useState("");
  const [msg, say] = useState("");
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <TextInput placeholder="Task" value={input} onChangeText={edit} />
      <Button
        title="Check"
        onPress={() => say(input.trim() ? "Accepted" : "Rejected")}
      />
      <Text>{msg}</Text>
    </View>
  );
}
