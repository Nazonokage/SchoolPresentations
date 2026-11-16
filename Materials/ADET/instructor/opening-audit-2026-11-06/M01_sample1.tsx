import { View, Text } from "react-native";

export default function App() {
  // A constant holding the text we want to show
  const greeting = "Hello, ADET!";
  return (
    // View is a container, like a div on the web
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      {/* Text shows words on screen. The braces insert the constant. */}
      <Text>{greeting}</Text>
    </View>
  );
}
