import { View, Text, Button } from "react-native";
import {
  QueryClient,
  QueryClientProvider,
  useQuery,
  useMutation,
  useQueryClient,
} from "@tanstack/react-query";
const client = new QueryClient();
const url =
  (process.env.EXPO_PUBLIC_API_URL ?? "http://localhost:8000") + "/tasks";
function List() {
  const cache = useQueryClient();
  const list = useQuery({
    queryKey: ["tasks"],
    queryFn: async () => {
      const r = await fetch(url);
      if (!r.ok) throw Error("Load failed");
      const rows = await r.json();
      if (!Array.isArray(rows)) throw Error("Expected list");
      return rows.length;
    },
  });
  const add = useMutation({
    mutationFn: async () => {
      const r = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: "Library visit" }),
      });
      if (!r.ok) throw Error("Save failed");
    },
    onSuccess: () => cache.invalidateQueries({ queryKey: ["tasks"] }),
  });
  return (
    <View>
      <Text>
        {list.isPending
          ? "Loading"
          : list.isError
            ? "Cannot load"
            : "Server count: " + list.data}
      </Text>
      <Button
        disabled={add.isPending}
        title="Add visit"
        onPress={() => add.mutate()}
      />
      {add.isError && <Text>Save failed. Check server before retry.</Text>}
    </View>
  );
}
export default function App() {
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <QueryClientProvider client={client}>
        <List />
      </QueryClientProvider>
    </View>
  );
}
