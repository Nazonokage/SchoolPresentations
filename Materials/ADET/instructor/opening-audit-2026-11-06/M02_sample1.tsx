import { useEffect, useState } from "react";
import { AppState, View, Text, Button } from "react-native";

// A component that counts seconds while it is on screen
function Timer() {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    console.log("Timer mounted");
    // Add one second every 1000 ms
    const id = setInterval(() => setSeconds((current) => current + 1), 1000);
    // Cleanup: runs when Timer is removed
    return () => {
      clearInterval(id);
      console.log("Timer unmounted");
    };
  }, []);

  return <Text>Seconds: {seconds}</Text>;
}

export default function App() {
  const [visible, setVisible] = useState(true);
  const [appState, setAppState] = useState(AppState.currentState);

  useEffect(() => {
    // Listen for the whole app going active or to the background
    const subscription = AppState.addEventListener("change", (next) => {
      setAppState(next);
      console.log("App state:", next);
    });
    return () => subscription.remove();
  }, []);

  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Text>App state: {appState}</Text>
      {visible && <Timer />}
      <Button
        title={visible ? "Hide timer" : "Show timer"}
        onPress={() => setVisible(!visible)}
      />
    </View>
  );
}
