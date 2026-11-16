import { useState } from "react";
import { View, Text, Button } from "react-native";
type Props = { name: string };
function Card({ name }: Props) {
  const [visits, set] = useState(0);
  return (
    <View>
      <Text>
        {name}: {visits} visits
      </Text>
      <Button title="Visit" onPress={() => set((n) => n + 1)} />
    </View>
  );
}
export default function App() {
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Card name="Library" />
      <Card name="Clinic" />
    </View>
  );
}
