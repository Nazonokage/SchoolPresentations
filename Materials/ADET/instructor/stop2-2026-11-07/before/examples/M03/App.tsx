import { View, Text } from "react-native";
import { useColorScheme, useWindowDimensions } from "react-native";
export default function App() {
  const dark = useColorScheme() === "dark";
  const { width } = useWindowDimensions();
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <View style={{ flexDirection: width > 540 ? "row" : "column", gap: 12 }}>
        {["Registrar", "Library"].map((name) => (
          <View
            key={name}
            style={{
              padding: 20,
              backgroundColor: dark ? "#163043" : "#e3f3fc",
            }}
          >
            <Text
              accessibilityRole="header"
              style={{ color: dark ? "white" : "#102030", fontSize: 22 }}
            >
              {name}
            </Text>
          </View>
        ))}
      </View>
    </View>
  );
}
