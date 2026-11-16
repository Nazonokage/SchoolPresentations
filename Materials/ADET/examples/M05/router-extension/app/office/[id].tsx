import { View, Text, Button } from "react-native";
import { Stack, router, useLocalSearchParams } from "expo-router";

const offices: Record<string, { title: string; hours: string }> = {
  library: { title: "Library", hours: "Open 8 AM" },
};

export default function OfficeScreen() {
  const parameters = useLocalSearchParams<{ id?: string | string[] }>();
  // Normalize, then check existence. Types alone do not validate an incoming URL.
  const officeId = Array.isArray(parameters.id) ? parameters.id[0] : parameters.id;
  const office = officeId && Object.hasOwn(offices, officeId) ? offices[officeId] : undefined;
  return (
    <View style={{ flex: 1, padding: 24, gap: 16 }}>
      <Stack.Screen options={{ title: office?.title ?? "Missing office" }} />
      <Text>{office ? `${office.title} — ${office.hours}` : "Office not found"}</Text>
      <Button title={router.canGoBack() ? "Back" : "Home"}
        onPress={() => router.canGoBack() ? router.back() : router.replace("/")} />
    </View>
  );
}
