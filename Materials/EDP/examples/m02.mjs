console.log('A: synchronous start');
setTimeout(() => console.log('D: timer callback'), 0);
Promise.resolve().then(() => console.log('C: promise callback'));
console.log('B: synchronous end');
function prepare(id, fail = false) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (fail) reject(new Error(`Unavailable: ${id}`));
      else resolve(`Ready: ${id}`);
    }, 30);
  });
}
async function main() {
  try {
    console.log(await prepare('A1'));
    console.log(await prepare('A2', true));
  } catch (error) {
    console.log('Handled:', error.message);
  } finally {
    console.log('Preparation finished');
  }
}
await main();
