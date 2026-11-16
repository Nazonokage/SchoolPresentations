import { useState } from "react";
import { View, Text, Button } from "react-native";
import * as Notifications from "expo-notifications";
export default function App() {
  const [msg, say] = useState("");
  async function remind() {
    try {
      await Notifications.setNotificationChannelAsync("study", {
        name: "Study",
        importance: Notifications.AndroidImportance.DEFAULT,
      });
      const p = await Notifications.requestPermissionsAsync();
      if (!p.granted) {
        say("Reminders disabled");
        return;
      }
      await Notifications.scheduleNotificationAsync({
        content: { title: "Study break", body: "Review one campus task." },
        trigger: {
          type: Notifications.SchedulableTriggerInputTypes.TIME_INTERVAL,
          seconds: 10,
          channelId: "study",
        },
      });
      say("Scheduled. Background the app to observe delivery.");
    } catch (e) {
      say(String(e));
    }
  }
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Button title="Schedule local reminder" onPress={remind} />
      <Text>{msg}</Text>
    </View>
  );
}
