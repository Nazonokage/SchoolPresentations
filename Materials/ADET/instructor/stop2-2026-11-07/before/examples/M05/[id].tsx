import { Text } from "react-native";
import { useLocalSearchParams } from "expo-router";
export default function Office() {
  const { id } = useLocalSearchParams();
  return (
    <Text style={{ padding: 30 }}>
      {id === "library" ? "Library • Open 8 AM" : "Office not found"}
    </Text>
  );
}
