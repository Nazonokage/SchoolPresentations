import { useState } from "react";
import { View, Text, Button, ScrollView, StyleSheet, useWindowDimensions } from "react-native";

type OfficeCardProps = { title: string; hours: string; capacity: number };

function OfficeCard({ title, hours, capacity }: OfficeCardProps) {
  const [visitors, setVisitors] = useState(0); // Each card owns separate state.
  const isFull = visitors >= capacity;
  return (
    <View style={styles.card}>
      <Text accessibilityRole="header" style={styles.heading}>{title}</Text>
      <Text style={styles.body}>{hours}</Text>
      <Text style={styles.body}>Visitors: {visitors} / {capacity}</Text>
      <Text style={styles.body}>{isFull ? "Full — please wait" : "Space available"}</Text>
      <Button title={`Join ${title}`} accessibilityLabel={`Join ${title} queue`}
        disabled={isFull}
        onPress={() => setVisitors((current) => Math.min(current + 1, capacity))} />
      <Button title={`Reset ${title}`} onPress={() => setVisitors(0)} />
    </View>
  );
}

export default function App() {
  const { width, fontScale } = useWindowDimensions();
  // Larger text gets a column even on a wider window.
  const useColumns = width >= 700 && fontScale <= 1.3;
  return (
    <ScrollView contentContainerStyle={styles.page}>
      <Text accessibilityRole="header" style={styles.heading}>Campus offices</Text>
      <Text style={styles.body}>Choose a queue. Full queues show a written reason.</Text>
      <View style={[styles.cards, { flexDirection: useColumns ? "row" : "column" }]}>
        <OfficeCard title="Library" hours="Open 8 AM" capacity={2} />
        <OfficeCard title="Clinic" hours="Open 9 AM" capacity={3} />
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  page: { flexGrow: 1, padding: 24, paddingTop: 60, paddingBottom: 48, gap: 16, backgroundColor: "#f1f5f9" },
  cards: { gap: 16 },
  card: { flex: 1, padding: 16, gap: 12, backgroundColor: "#ffffff", borderWidth: 1, borderColor: "#475569", borderRadius: 12 },
  heading: { color: "#0f172a", fontSize: 24, fontWeight: "bold" },
  body: { color: "#0f172a", fontSize: 18 },
});
