import { View, Text } from "react-native";
function valid(s: string) {
  return s.trim().length > 0 && s.trim().length <= 80;
}
export default function App() {
  const cases: [string, boolean][] = [
    [" ", false],
    ["Book", true],
    ["x".repeat(81), false],
  ];
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      {cases.map(([v, want], i) => (
        <Text key={i}>
          Case {i + 1}: {valid(v) === want ? "PASS" : "FAIL"}
        </Text>
      ))}
    </View>
  );
}
