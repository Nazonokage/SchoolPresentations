import { View, Button } from "react-native";
import { Stack, router } from "expo-router";
export default function App() {
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Stack.Screen options={{ title: "Campus offices" }} />
      <Button
        title="Visit library"
        onPress={() => router.push("/office/library")}
      />
    </View>
  );
}
