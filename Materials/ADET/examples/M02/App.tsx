import { useEffect, useState } from "react";
import { AppState, View, Text, Button } from "react-native";

// Count delivered interval callbacks, not precise elapsed time.
function Timer() {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    console.log("Timer mounted");
    // Request a callback roughly every 1000 ms; the OS can delay it.
    const intervalId = setInterval(() => setSeconds((current) => current + 1), 1000);
    // Cleanup: runs when Timer is removed
    return () => {
      clearInterval(intervalId);
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
    const subscription = AppState.addEventListener("change", (nextAppState) => {
      setAppState(nextAppState);
      console.log("App state:", nextAppState);
    });
    return () => subscription.remove();
  }, []);

  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Text>App state: {appState}</Text>
      {visible && <Timer />}
      <Button
        title={visible ? "Hide timer" : "Show timer"}
        onPress={() => setVisible((currentVisible) => !currentVisible)}
      />
    </View>
  );
}
