interface Order { id: string; total: number }
function receipt(order: Order): string {
  return `${order.id}: PHP ${order.total}`;
}
console.log(receipt({ id: 'A1', total: 60 }));
// Change total to "60" to see a type error, then restore the number.
