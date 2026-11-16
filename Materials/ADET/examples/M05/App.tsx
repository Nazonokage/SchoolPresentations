import { useState } from "react";
import { View, Text, Button } from "react-native";

export default function App() {
  // A teaching model of a stack; this is NOT Expo Router.
  const [routes, setRoutes] = useState<string[]>(["home"]);
  const currentRoute = routes[routes.length - 1];
  const officeName = currentRoute === "library" ? "Library — Open 8 AM" : "Office not found";
  function pushOffice(id: string) {
    setRoutes((currentRoutes) => [...currentRoutes, id]);
  }
  function goBack() {
    // Keep the home route when there is no previous screen.
    setRoutes((currentRoutes) => currentRoutes.length > 1 ? currentRoutes.slice(0, -1) : currentRoutes);
  }
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 16 }}>
      <Text>Navigation paper-model companion</Text>
      <Text>Stack: {routes.join(" → ")}</Text>
      {currentRoute === "home" ? (
        <View style={{ gap: 12 }}>
          <Button title="Visit library" onPress={() => pushOffice("library")} />
          <Button title="Try unknown office" onPress={() => pushOffice("unknown")} />
        </View>
      ) : <Text>{officeName}</Text>}
      <Button title="Back" disabled={routes.length === 1} onPress={goBack} />
    </View>
  );
}
