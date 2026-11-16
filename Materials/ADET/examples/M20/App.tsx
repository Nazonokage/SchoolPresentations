import { useState } from "react";
import { View, Text, Button } from "react-native";

export default function App() {
  const [done, set] = useState<string[]>([]);
  const steps = [
    "Clean launch",
    "Valid save and reload",
    "Invalid input rejected",
    "Failure and recovery",
    "Explain personal change",
  ];
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      {steps.map((x) => (
        <Button
          key={x}
          title={(done.includes(x) ? "✓ " : "○ ") + x}
          onPress={() =>
            set(done.includes(x) ? done.filter((s) => s !== x) : [...done, x])
          }
        />
      ))}
      <Text>
        Rehearsed {done.length}/{steps.length}
      </Text>
    </View>
  );
}
