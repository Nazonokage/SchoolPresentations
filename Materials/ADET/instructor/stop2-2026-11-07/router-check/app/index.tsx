import { View, Button } from "react-native";
import { Stack, router } from "expo-router";

export default function HomeScreen() {
  return (
    <View style={{ flex: 1, padding: 24, gap: 16 }}>
      <Stack.Screen options={{ title: "Campus offices" }} />
      <Button title="Visit library" onPress={() => router.push("/office/library")} />
      <Button title="Try unknown office" onPress={() => router.push("/office/unknown")} />
    </View>
  );
}
