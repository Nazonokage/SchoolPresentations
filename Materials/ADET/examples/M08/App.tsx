import { useState } from "react";
import { View, Text, Button, TextInput, FlatList } from "react-native";
type Row = { id: string; title: string; done: boolean };
export default function App() {
  const [rows, set] = useState<Row[]>([]);
  const [name, edit] = useState("");
  const [msg, say] = useState("");
  const [busy, lock] = useState(false);
  const url =
    (process.env.EXPO_PUBLIC_API_URL ?? "http://localhost:8000") + "/tasks";
  async function act(method: string, id = "") {
    lock(true);
    try {
      if (method !== "GET") {
        const res = await fetch(url + (id ? "/" + id : ""), {
          method,
          headers: { "Content-Type": "application/json" },
          body:
            method === "DELETE"
              ? undefined
              : JSON.stringify(
                  method === "POST" ? { title: name } : { done: true },
                ),
        });
        if (!res.ok) throw Error("HTTP " + res.status);
      }
      const res = await fetch(url);
      if (!res.ok) throw Error("Reload failed");
      const list = await res.json();
      if (
        !Array.isArray(list) ||
        !list.every(
          (x) =>
            typeof x?.id === "string" &&
            typeof x.title === "string" &&
            typeof x.done === "boolean",
        )
      )
        throw Error("Invalid record");
      set(list);
      say("Loaded " + list.length);
    } catch (e) {
      say(String(e));
    } finally {
      lock(false);
    }
  }
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <TextInput value={name} onChangeText={edit} placeholder="Task title" />
      <Button disabled={busy} title="Add" onPress={() => act("POST")} />
      <Button disabled={busy} title="Refresh" onPress={() => act("GET")} />
      <Text>{msg}</Text>
      <FlatList
        data={rows}
        keyExtractor={(x) => x.id}
        renderItem={({ item }) => (
          <View>
            <Text>
              {item.title} {item.done ? "✓" : ""}
            </Text>
            <Button
              disabled={busy}
              title="Finish"
              onPress={() => act("PATCH", item.id)}
            />
            <Button
              disabled={busy}
              title="Delete"
              onPress={() => act("DELETE", item.id)}
            />
          </View>
        )}
      />
    </View>
  );
}
