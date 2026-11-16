import { View, Text } from "react-native";

export default function App() {
  const greeting = "Hello, ADET!"; // Constant: a name for a value.
  const prices = [25, 35];
  function calculateBalance(budget: number) {
    let remaining = budget; // Variable: updated as each price is paid.
    for (const price of prices) {
      remaining -= price; // Loop: apply the same step to every price.
    }
    return remaining; // Function: return the result to its caller.
  }
  const balance = calculateBalance(50);
  let message: string;
  if (balance >= 0) {
    message = "Change: PHP " + balance;
  } else {
    message = "Kulang: PHP " + Math.abs(balance);
  }
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Text>{greeting}</Text>
      <Text>{message}</Text>
    </View>
  );
}
