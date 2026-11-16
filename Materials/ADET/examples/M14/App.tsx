import { useState } from "react";
import { View, Text, Button } from "react-native";
import { Share, Linking } from "react-native";
export default function App() {
  const [msg, say] = useState("");
  async function handoff(map: boolean) {
    try {
      if (map)
        await Linking.openURL(
          "https://www.openstreetmap.org/?mlat=10.72&mlon=122.56",
        );
      else await Share.share({ message: "Meet at the library at 3 PM" });
      say("Returned to app");
    } catch (e) {
      say(String(e));
    }
  }
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Button title="Share study meetup" onPress={() => handoff(false)} />
      <Button title="Open Iloilo map" onPress={() => handoff(true)} />
      <Text>{msg}</Text>
    </View>
  );
}
