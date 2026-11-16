import { View, Text } from "react-native";

export default function App() {
  const prices = [25, 35];
  function balance(budget: number) {
    let left = budget;
    for (const price of prices) left -= price;
    return left;
  }
  const left = balance(50);
  let message: string;
  if (left >= 0) {
    message = "Change: " + left;
  } else {
    message = "Kulang: " + Math.abs(left);
  }
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Text>
        Baon: PHP 50.{" "}
        {message}
      </Text>
    </View>
  );
}
