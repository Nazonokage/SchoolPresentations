import { useState } from "react";
import { View, Text, Button, TextInput, FlatList } from "react-native";
type Task = { id: number; title: string; done: boolean };
export default function App() {
  const [rows, set] = useState<Task[]>([
    { id: 1, title: "Library", done: false },
    { id: 2, title: "Clinic", done: false },
  ]);
  const [q, search] = useState("");
  const [draft, edit] = useState("");
  const [editingId, select] = useState<number | null>(null);
  function save() {
    const title = draft.trim();
    if (!title) return;
    set((old) => editingId === null
      ? [...old, { id: Math.max(0, ...old.map(row => row.id)) + 1, title, done: false }]
      : old.map(row => row.id === editingId ? { ...row, title } : row));
    select(null);
    edit("");
  }
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <TextInput
        placeholder="Filter campus tasks"
        value={q}
        onChangeText={search}
      />
      <TextInput accessibilityLabel="Task title" placeholder="New or edited title" value={draft} onChangeText={edit} />
      <Button title={editingId === null ? "Add task" : "Save edit"} disabled={!draft.trim()} onPress={save} />
      <FlatList
        data={rows.filter((x) =>
          x.title.toLowerCase().includes(q.toLowerCase()),
        )}
        keyExtractor={(x) => String(x.id)}
        ListEmptyComponent={<Text>No matches</Text>}
        renderItem={({ item }) => (
          <View>
          <Button
            title={item.title + (item.done ? " ✓" : "")}
            onPress={() =>
              set((old) =>
                old.map((x) =>
                  x.id === item.id ? { ...x, done: !x.done } : x,
                ),
              )
            }
          />
          <Button title={"Edit " + item.title} onPress={() => { select(item.id); edit(item.title); }} />
          </View>
        )}
      />
    </View>
  );
}
