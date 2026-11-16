from pathlib import Path
import json, re, textwrap

ROOT = Path('Application Development and Emerging Technologies (Inluding event Driven programming)/Modern_2026_Course_Pack')
ROOT.mkdir(parents=True, exist_ok=True)
MODULES = {'ADET': [], 'EDP': []}
SOURCES = {
 'expo': ('Expo project templates', 'https://docs.expo.dev/more/create-expo/'),
 'go': ('Start developing with Expo', 'https://docs.expo.dev/get-started/start-developing/'),
 'build': ('Development builds', 'https://docs.expo.dev/develop/development-builds/introduction/'),
 'react': ('React Quick Start', 'https://react.dev/learn'),
 'ts': ('TypeScript everyday types', 'https://www.typescriptlang.org/docs/handbook/2/everyday-types.html'),
 'narrow': ('TypeScript narrowing', 'https://www.typescriptlang.org/docs/handbook/2/narrowing.html'),
 'effect': ('React effects and cleanup', 'https://react.dev/learn/synchronizing-with-effects'),
 'reducer': ('React reducers', 'https://react.dev/learn/extracting-state-logic-into-a-reducer'),
 'list': ('React Native FlatList', 'https://reactnative.dev/docs/flatlist'),
 'access': ('React Native accessibility', 'https://reactnative.dev/docs/accessibility'),
 'security': ('React Native security', 'https://reactnative.dev/docs/security'),
 'storage': ('Expo AsyncStorage reference', 'https://docs.expo.dev/versions/latest/sdk/async-storage/'),
 'image': ('Expo ImagePicker', 'https://docs.expo.dev/versions/latest/sdk/imagepicker/'),
 'location': ('Expo Location', 'https://docs.expo.dev/versions/latest/sdk/location/'),
 'sensor': ('Expo Sensors', 'https://docs.expo.dev/versions/latest/sdk/sensors/'),
 'flutter': ('Flutter installation', 'https://docs.flutter.dev/install'),
 'deploy': ('Build an Expo app', 'https://docs.expo.dev/deploy/build-project/'),
 'events': ('MDN introduction to events', 'https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events'),
 'promise': ('MDN using promises', 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises'),
 'await': ('MDN await', 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await'),
 'abort': ('MDN AbortController', 'https://developer.mozilla.org/en-US/docs/Web/API/AbortController'),
 'fetch': ('MDN using Fetch', 'https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch'),
 'loop': ('Node.js event loop', 'https://nodejs.org/learn/asynchronous-work/event-loop-timers-and-nexttick'),
 'node': ('Node.js TypeScript execution', 'https://nodejs.org/api/typescript.html'),
 'emitter': ('Node.js EventEmitter', 'https://nodejs.org/api/events.html'),
 'test': ('Node.js test runner', 'https://nodejs.org/api/test.html'),
 'worker': ('MDN Web Workers', 'https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers'),
 'sse': ('MDN server-sent events', 'https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events'),
 'ws': ('MDN WebSocket API', 'https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API'),
 'local': ('MDN localStorage', 'https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage'),
}

def clean(s): return textwrap.dedent(s).strip() + '\n'
def write(path, text):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(clean(text), encoding='utf-8')

def add(course, title, hook, targets, lesson, analogy, code, expected, walkthrough, challenge, bugs, refs, mode='rn', extra='', files=None):
    n=len(MODULES[course])+1
    slug=re.sub(r'[^a-z0-9]+','-',title.lower()).strip('-')
    filename=f'{course}_M{n:02d}_{slug}.md'
    if files is None:
        files={'App.tsx' if mode=='rn' else 'index.html' if mode=='html' else 'main.ts' if mode=='ts' else 'main.mjs':clean(code)}
    lab=f'examples/{course}/M{n:02d}'
    for name, content in files.items(): write(f'{lab}/{name}', content)
    if mode=='rn':
        instructions='Use the Expo project from [SETUP](../SETUP.md#adet-react-native-and-expo-go). Save your previous App.tsx, then replace the **entire** App.tsx with the code below. Do not paste it into a Router screen. Run `npx expo start`, open Expo Go, and scan the QR code. All unlisted project files stay as generated.'
    elif mode=='html':
        instructions=f'Create a new folder `edp-m{n:02d}` and save the complete file(s) below there. In that folder run `python -m http.server 8000 --bind 127.0.0.1`, then open http://127.0.0.1:8000 in your browser. Keep the terminal open; stop with Ctrl+C. See [SETUP](../SETUP.md#edp-browser-and-nodejs) if Python is unavailable. Use browser DevTools Console for logs.'
    elif mode=='ts':
        instructions=f'Create a new folder `edp-m{n:02d}` and save the file(s) below there. Use Node.js 24.18.1 or a compatible newer LTS release. Run `node main.ts` in that folder. Native type stripping runs code but does not check types; use the type-check command in [SETUP](../SETUP.md#edp-browser-and-nodejs) too.'
    else:
        instructions=f'Create a new folder `edp-m{n:02d}` and save the complete file(s) below there. Run `node main.mjs` in that folder, using Node.js 24.18.1 or a compatible newer LTS release. No third-party packages are required unless stated below.'
    blocks='\n\n'.join(f'### `{name}`\n\n```{ {".tsx":"tsx",".ts":"ts",".html":"html",".mjs":"js",".js":"js",".json":"json"}.get(Path(name).suffix, "text")}\n{clean(content).rstrip()}\n```' for name,content in files.items())
    sources='\n'.join(f'- [{SOURCES[r][0]}]({SOURCES[r][1]})' for r in refs)
    targetlist='\n'.join(f'{i+1}. {x}' for i,x in enumerate(targets.split('|')))
    prerequisites='Complete setup; variables, conditions, and functions from introductory programming.' if n==1 else f'Modules 01–{n-1:02d}; the starter below is independent, so a previous activity does not have to be perfect.'
    content=f'''# {course} Module {n:02d}: {title}

[Course index](README.md) | [Setup](../SETUP.md) | [Teaching guide](../TEACHING_GUIDE.md)

## A. Lesson Preview & Review

{hook}

**Prerequisites:** {prerequisites}

**Time:** About 3 hours: 25 minutes explanation, 50 minutes guided coding, 15 minutes code tracing, 60 minutes remix/testing, 30 minutes demo and feedback. The semester guide includes additional integration time.

**Learning targets**

{targetlist}

## B. Main Lesson

{clean(lesson)}
## C. Analogy & Real-World Use

{analogy}

## D. Guided Coding: Copy → Run → Explain

{instructions}

{extra}

{blocks}

### Expected result and quick verification

{expected}

### Read the code with your partner

{walkthrough}

## E. Gawin Mong Sarili: Coding Challenge

{challenge}

**Submit:** Your changed source file(s), one screenshot or a short output log, and 3–5 sentences explaining the event/input, the important state/data, and the change you made. Tagalog, English, or Taglish is welcome. Include one normal case and one edge case you tested. Copying the guided starter is allowed; explain and personalize the extension.

## F. Troubleshooting & Lesson Wrap-Up

{bugs}

**Exit demo, not a quiz:** Run the starter or your remix, point to the line responsible for its main behavior, and explain one failure you prevented. Partner asks “Bakit gumagana?” and you answer using the actual code.

## G. Instructor Notes & References

Use the learning targets as the demonstration checklist. Let pairs switch driver and navigator halfway through; individually ask each student to trace one changed value. Assess the extension using the common rubric in the teaching guide. Suggested instructor verification: reproduce the expected result first, then try the edge case in section E.

Technical references checked 2 November 2026. These are API references; the scenarios and teaching exercises are original classroom designs.

{sources}

The same starter files are available in [examples/{course}/M{n:02d}](../{lab}/).
'''
    write(f'{course}/{filename}',content)
    MODULES[course].append({'n':n,'title':title,'file':filename,'mode':mode,'files':list(files)})

def rn(title,hook,targets,lesson,analogy,code,expected,walkthrough,challenge,bugs,refs,extra=''):
    add('ADET',title,hook,targets,lesson,analogy,code,expected,walkthrough,challenge,bugs,refs,extra=extra)

# Each activity is deliberately complete and independently replaceable.
rn('From Campus Problem to First App',
 'Build a tiny campus helper before memorizing a long list of terms. Sino ang user, at anong problema ang gusto niyang matapos?',
 'Describe one user need and an acceptance criterion|Run a React Native screen through Expo Go|Identify a component, a prop, and an event handler',
 '''An application helps someone complete a task. Start with a user story: “As a student, I want to see where to ask for enrollment help so I can avoid the wrong queue.” An acceptance criterion is observable: tapping Help displays the correct office name.

React Native provides mobile UI components. React describes a screen using components and data. TypeScript adds checks while writing JavaScript. Expo supplies project tooling and compatible native libraries; Expo Go is an installed learning client that opens your project. The JavaScript code is served by the development server; this is not yet a standalone store app.

JSX looks like markup but lives inside JavaScript. A component is a function returning JSX. A prop configures a component, such as a button title. A handler is the function called after an interaction. Follow a small development cycle: need → sketch → implement → test → improve. Do not start by adding every possible feature.''',
 'Parang school information desk: the screen is the signboard, the button is the request, and the handler gives the response. A beautiful signboard still fails if it sends the student to the wrong office.',
 '''import { useState } from 'react';
import { View, Text, Button } from 'react-native';

export default function App() {
  const [message, setMessage] = useState('Saan ako pupunta?');
  return (
    <View style={{ flex: 1, padding: 28, paddingTop: 60, gap: 16 }}>
      <Text style={{ fontSize: 28 }}>Campus Buddy</Text>
      <Text>{message}</Text>
      <Button title="Enrollment help" onPress={() => setMessage('Visit the registrar.')} />
      <Button title="Reset" onPress={() => setMessage('Saan ako pupunta?')} />
    </View>
  );
}''',
 'The phone shows Campus Buddy. Tap Enrollment help: the message becomes “Visit the registrar.” Tap Reset: the original question returns. No network request is made by either button.',
 '`useState` stores the message between renders. `onPress` receives a function, not the result of calling a function. `setMessage` requests a new render; the Text reads the latest state. Identify which text is constant and which is state.',
 'Add Library help and Clinic help buttons with fictional office information. Before coding, write one user story and three pass/fail acceptance criteria. Ask a partner to find the library without your spoken instructions.',
 'Blank screen: look for the first error in the terminal. JSX text must be inside Text. If you see the template screen, confirm you used the blank TypeScript template and edited its root App.tsx. An Expo Go QR code is a development preview, not a permanent deployment.', ['expo','go','react'])

rn('TypeScript with a Baon Calculator',
 'Can your baon survive lunch and pamasahe? Use a small calculation to discover why numbers and strings should not be mixed.',
 'Declare number and object types|Write a typed function with a return value|Explain the difference between type checks and input validation',
 '''A variable names a value. Use `const` when the binding will not be reassigned. A `number` supports arithmetic; a string such as "100" is text. TypeScript can catch accidental misuse before execution, but its types do not validate data arriving from forms or a server.

An object groups related facts. A type alias describes its shape. Function parameters are the inputs; the return value is the result. Keep calculations separate from the screen so the same logic can be tested or reused. For this starter, the budget is fixed data; a later module will read and validate user input.

Read arithmetic aloud: remaining equals allowance minus the sum of lunch and fare. Parentheses make that grouping explicit. A negative answer is meaningful data, not automatically a runtime error; the interface should explain it.''',
 'A type is like a labeled envelope: pamasahe goes in the number envelope. Pero kailangan mo pa ring bilangin ang laman; the label alone cannot prove that a stranger supplied a valid amount.',
 '''import { View, Text } from 'react-native';
type Budget = { allowance: number; lunch: number; fare: number };
function remaining(budget: Budget): number {
  return budget.allowance - (budget.lunch + budget.fare);
}
export default function App() {
  const budget: Budget = { allowance: 150, lunch: 65, fare: 40 };
  const balance = remaining(budget);
  return <View style={{ padding: 28, paddingTop: 60, gap: 12 }}>
    <Text style={{ fontSize: 26 }}>Baon Check</Text>
    <Text>Allowance: PHP {budget.allowance}</Text>
    <Text>Remaining: PHP {balance.toFixed(2)}</Text>
    <Text>{balance >= 0 ? 'Kasya!' : 'Adjust muna ang gastos.'}</Text>
  </View>;
}''',
 'The initial remaining amount is PHP 45.00 and the message is Kasya! Change allowance to 90: the result becomes -15.00 and the advice changes.',
 '`Budget` describes three required properties. `remaining` returns a number without changing its argument. The conditional expression chooses a message. `toFixed(2)` formats a number as display text; do not use that text for further arithmetic.',
 'Add a savings amount and subtract it too. Test allowance 150, 105, and 90 with the original expenses before adding savings. Deliberately assign a string to lunch, observe the editor error, then fix it.',
 'If numbers concatenate, inspect whether an input is a string. Run `npx tsc --noEmit` in the Expo project: running the app alone is not proof that TypeScript checks passed. Avoid `any` as a way to hide the error.', ['ts'])

rn('Arrays and Functions: Canteen Menu',
 'Make a menu that can answer “Ano ang kasya sa PHP 50?” without repeating the same code for every food.',
 'Model a collection with an array|Use filter and map|Separate data selection from presentation',
 '''An array is an ordered collection. Each menu item has a stable ID, a name, and a price. `filter` returns only entries that satisfy a condition; `map` transforms every selected entry. Neither needs to change the original list.

Arrow functions are compact function expressions. In `item => item.price <= limit`, item is the current entry and the expression is the returned result. React can render an array of elements. The `key` identifies an item across renders; choose a stable ID rather than a changing list position.

When the collection is small, mapping into a View is a good learning step. For large or scrollable lists, we will use FlatList. Practice tracing data before JSX: original menu → affordable items → Text elements. This separation makes an empty result easier to handle.''',
 'Parang pagpili sa turo-turo: filter selects the dishes within budget; map writes a label for each selected dish. Hindi nito binubura ang ibang pagkain sa tunay na menu.',
 '''import { View, Text } from 'react-native';
type Food = { id: string; name: string; price: number };
const menu: Food[] = [
  { id: 'a', name: 'Lugaw', price: 25 },
  { id: 'b', name: 'Siomai rice', price: 45 },
  { id: 'c', name: 'Chicken meal', price: 85 },
];
export default function App() {
  const limit = 50;
  const affordable = menu.filter(food => food.price <= limit);
  return <View style={{ padding: 28, paddingTop: 60, gap: 12 }}>
    <Text style={{ fontSize: 26 }}>Budget Menu: PHP {limit}</Text>
    {affordable.map(food => <Text key={food.id}>{food.name}: PHP {food.price}</Text>)}
    {affordable.length === 0 && <Text>Walang kasya. Try another budget.</Text>}
  </View>;
}''',
 'With limit 50, Lugaw and Siomai rice appear. With limit 10, only the heading and empty-state message appear. With limit 100, all three meals appear.',
 'Read the Food type before the data. Trace the condition for each price: 25, 45, 85. The array remains unchanged even when the displayed subset changes. Explain why the key is food.id.',
 'Add two snacks with unique IDs. Show the number of affordable items and their total price using reduce. Test an empty selection; its total should be zero.',
 'A map callback with braces needs an explicit return. Duplicate key warnings mean IDs are not unique. Calling sort directly changes an array: use a copy if you add sorting.', ['ts','react'])

rn('Reusable Components and Props',
 'Build a student ID wall without copy-pasting an entire card for every student.',
 'Create a reusable component|Pass typed props|Distinguish parent data from child display',
 '''A component packages a piece of interface. Props are inputs supplied by its parent. A child should treat its props as read-only. Reuse works best when the component has one understandable job, such as displaying a student card.

Destructuring takes named values from an object: `{name, course}` means the function receives props and reads those two properties. A typed props object makes required information visible to the caller. Capitalize component names so JSX recognizes them as custom components.

Do not make a separate component for every single line immediately. Extract one when it is repeated or has a meaningful purpose. Shared styling helps visual consistency; shared data is still owned by the parent. Later, state will make these components interactive.''',
 'The component is an ID-card template; props are the student details printed on it. Iisang template, iba-ibang laman. Changing the template improves every card.',
 '''import { View, Text } from 'react-native';
type CardProps = { name: string; course: string; year: number };
function StudentCard({ name, course, year }: CardProps) {
  return <View style={{ padding: 16, backgroundColor: '#dbeafe', borderRadius: 12 }}>
    <Text style={{ fontSize: 22, color: '#172554' }}>{name}</Text>
    <Text>{course} • Year {year}</Text>
  </View>;
}
export default function App() {
  return <View style={{ padding: 28, paddingTop: 60, gap: 16 }}>
    <StudentCard name="Mika" course="BSIT" year={3} />
    <StudentCard name="Paolo" course="BSIS" year={2} />
  </View>;
}''',
 'Two cards use the same layout but display different names, courses, and years. Changing the component background changes both cards.',
 'The App function is the parent. StudentCard receives three props. `year={3}` passes a number; `year="3"` would pass a string and fail the declared type.',
 'Add an optional hobby prop and a default display of “Still exploring.” Add a third student without a hobby. Explain why a missing optional prop is allowed but a missing name is not.',
 'A lowercase custom tag will not behave as your component. If a prop seems missing, compare spelling at the call site and in the props type. Do not assign a new value directly to a prop.', ['react','ts'])

rn('Layouts and Accessible Campus Cards',
 'A screen should still be useful on a small phone, with larger text, and when a student uses a screen reader.',
 'Arrange a layout with Flexbox|Use readable contrast and descriptive labels|Test a layout with large text',
 '''React Native uses Flexbox for layout. A View normally stacks children vertically; `flexDirection: "row"` places them side by side. `flex: 1` lets an element use available space. Padding gives content breathing room. Avoid assuming every phone has the same width.

Accessibility means students can understand and operate the interface in different ways. Use meaningful labels, readable text, and controls that are easy to hit. Do not communicate a state with color alone: add a word or symbol with text. Large system fonts can reveal clipping that ordinary screenshots miss.

A ScrollView supports overflow when content grows, but it renders all its children. It is appropriate for this short information page. A layout test is an actual behavior check: increase text size, rotate where supported, and read content in order.''',
 'Think of classroom signage: magandang kulay is not enough if the room number is tiny or the directions only say “follow the red sign.” Labels and spacing help everyone.',
 '''import { ScrollView, View, Text, Button } from 'react-native';
import { useState } from 'react';
export default function App() {
  const [status, setStatus] = useState('Not requested');
  return <ScrollView contentContainerStyle={{ padding: 28, paddingTop: 60, gap: 20 }}>
    <Text accessibilityRole="header" style={{ fontSize: 28 }}>Library Help</Text>
    <View style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 12 }}>
      <Text style={{ padding: 16, backgroundColor: '#e2e8f0', color: '#0f172a' }}>Floor: 2</Text>
      <Text style={{ padding: 16, backgroundColor: '#e2e8f0', color: '#0f172a' }}>Open: 8 AM–5 PM</Text>
    </View>
    <Text>Demo schedule only. Ask staff for actual opening hours.</Text>
    <Button title="Request library assistance" accessibilityLabel="Request help from library staff"
      onPress={() => setStatus('Request recorded in this demo')} />
    <Text accessibilityLiveRegion="polite">Status: {status}</Text>
  </ScrollView>;
}''',
 'Information cards wrap when necessary. Tapping the button changes the textual status. With large system text, the content remains scrollable. Announcement behavior varies by platform; test with the actual screen reader.',
 'The scroll container controls padding; the inner View controls wrapping. The status is written as text rather than represented by a green dot. Accessibility labels describe the action.',
 'Create a clinic information card. Run three checks: largest practical font size, small screen width, and a screen-reader pass on an available device. Record one improvement based on each test.',
 'Clipped content often comes from fixed heights. Tiny text is not a valid fix. `accessibilityLiveRegion` is primarily Android behavior; do not assume an identical iOS announcement.', ['access'])

rn('State and Events: Milk Tea Counter',
 'Tap to add cups, then ask: why does changing a normal variable fail to update the screen?',
 'Use useState|Update from the previous state safely|Keep a count within a valid range',
 '''State is data that React remembers between renders. Updating state requests a new render. A local variable inside the component is recreated when the function runs; changing it alone does not tell React to update the interface.

When the next value depends on the previous one, use an updater function: `setCups(current => current + 1)`. This matters when updates are batched. Keep derived values such as price totals calculated from state rather than storing duplicate state that can become inconsistent.

An event handler runs in response to an action. Pass the handler as a function. `onPress={add}` registers it; `onPress={add()}` calls it while rendering. A disabled button improves the experience, but also protect the state update itself from invalid values.''',
 'State is the order slip the cashier keeps updating. The screen is a fresh printout of that slip. Hindi kailangang manually palitan ang bawat text sa screen.',
 '''import { useState } from 'react';
import { View, Text, Button } from 'react-native';
export default function App() {
  const [cups, setCups] = useState(0);
  const total = cups * 39;
  return <View style={{ padding: 28, paddingTop: 60, gap: 16 }}>
    <Text style={{ fontSize: 26 }}>Milk Tea Counter</Text>
    <Text>Cups: {cups} | Total: PHP {total}</Text>
    <Button title="Add cup" onPress={() => setCups(current => current + 1)} />
    <Button title="Remove cup" disabled={cups === 0}
      onPress={() => setCups(current => Math.max(0, current - 1))} />
    <Button title="New order" onPress={() => setCups(0)} />
  </View>;
}''',
 'Three Add taps show 3 cups and PHP 117. Removing all cups stops at zero. New order returns both count and derived total to zero.',
 'Only cups is stored as state. total is recalculated during every render. Math.max provides a lower bound even if remove were triggered unexpectedly.',
 'Set a maximum of ten cups and disable Add when reached. Add a size selector with two prices and calculate total from cups and size. Test switching size after adding three cups.',
 'Do not write `cups++`; state must be updated with its setter. Do not store total separately unless there is a clear need. A render loop often means a setter was called directly in JSX.', ['react'])

rn('Forms and Validation: Split the Merienda Bill',
 'Friends split a snack bill. What happens when someone enters zero people or leaves the amount blank?',
 'Control text inputs with state|Validate numeric input|Display helpful errors before calculation',
 '''TextInput supplies strings, even if the keyboard looks numeric. Convert deliberately and validate the result. `Number("")` becomes zero, so check trimmed empty text before conversion. A keyboard hint is not a guarantee about pasted text.

Validation protects meaning: the amount must be finite and positive; the people count must be a positive integer. A useful error explains how to recover. Show the result only after all checks pass. In a real payment system, use an appropriate money representation and rounding policy; this is a display-only classroom splitter.

A controlled input gets its value from state and sends changes back through a callback. This gives the program one reliable place to read the current form. Keep labels visible instead of relying only on placeholders.''',
 'A form is like an order slip checked by the cashier. Kung “zero friends” ang nakasulat, ask for correction before dividing the bill.',
 '''import { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
export default function App() {
  const [amount, setAmount] = useState('120');
  const [people, setPeople] = useState('3');
  const [message, setMessage] = useState('Ready to split');
  function split() {
    const total = Number(amount), count = Number(people);
    if (!amount.trim() || !people.trim() || !Number.isFinite(total) || total <= 0 ||
        !Number.isInteger(count) || count <= 0) {
      setMessage('Enter a positive amount and a whole number of people.');
      return;
    }
    setMessage(`Each pays about PHP ${(total / count).toFixed(2)}`);
  }
  return <View style={{ padding: 28, paddingTop: 60, gap: 12 }}>
    <Text>Bill amount (PHP)</Text>
    <TextInput accessibilityLabel="Bill amount" value={amount} onChangeText={setAmount}
      keyboardType="decimal-pad" style={{ borderWidth: 1, padding: 12 }} />
    <Text>Number of people</Text>
    <TextInput accessibilityLabel="Number of people" value={people} onChangeText={setPeople}
      keyboardType="number-pad" style={{ borderWidth: 1, padding: 12 }} />
    <Button title="Split bill" onPress={split} />
    <Text>{message}</Text>
  </View>;
}''',
 '120 split among 3 shows PHP 40.00. Zero people, blank fields, negative amount, and 2.5 people each produce the corrective message.',
 'Trace strings → numeric conversion → validation → result. The early return prevents invalid division. Number.isFinite rejects Infinity and NaN.',
 'Add an optional service charge percentage from 0 to 20. Reject values outside the range. Try amount 100 and three people; explain why a real collection needs a policy for the extra cent.',
 'If an empty input becomes zero unexpectedly, check it before Number conversion. `parseInt("3abc")` accepts a partial number; Number plus explicit validation is clearer here.', ['ts','narrow'])

rn('Lists and CRUD: Campus Errands',
 'Make a small to-do list that can add, finish, and delete errands without losing track of which row is which.',
 'Render items with FlatList|Use immutable array updates|Implement create, read, update, and delete',
 '''CRUD means create, read, update, and delete. In this activity the data lives only in memory. A stable ID identifies a task even when its text changes or another row is removed.

State updates should produce a new array. Add with spread, update with map, delete with filter. Mutating an existing object can make updates hard to follow and interfere with components that compare references. Keep text and ID separate: two errands may share the same title.

FlatList receives data and a renderItem function. It renders a window of items rather than eagerly drawing a huge list. The empty component gives the user a useful first-run message. Persistence comes later; reloading this activity intentionally resets the tasks.''',
 'Use a claim stub number, not the position in the queue. Kapag umalis ang unang tao, hindi nagiging ibang tao ang may stub number 8.',
 '''import { useRef, useState } from 'react';
import { View, Text, TextInput, Button, FlatList } from 'react-native';
type Task = { id: string; title: string; done: boolean };
export default function App() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [title, setTitle] = useState('');
  const nextId = useRef(1);
  function add() {
    if (!title.trim()) return;
    const task = { id: String(nextId.current++), title: title.trim(), done: false };
    setTasks(current => [...current, task]); setTitle('');
  }
  return <View style={{ flex: 1, padding: 28, paddingTop: 60, gap: 12 }}>
    <TextInput accessibilityLabel="New errand" placeholder="Print handout" value={title}
      onChangeText={setTitle} style={{ borderWidth: 1, padding: 12 }} />
    <Button title="Add errand" onPress={add} />
    <FlatList data={tasks} keyExtractor={item => item.id}
      ListEmptyComponent={<Text>No errands yet.</Text>}
      renderItem={({ item }) => <View style={{ paddingVertical: 12, gap: 8 }}>
        <Text>{item.done ? 'Done' : 'To do'}: {item.title}</Text>
        <Button title="Toggle done" onPress={() => setTasks(current => current.map(t =>
          t.id === item.id ? { ...t, done: !t.done } : t))} />
        <Button title="Delete" onPress={() => setTasks(current => current.filter(t => t.id !== item.id))} />
      </View>} />
  </View>;
}''',
 'Add two errands, mark one done, then delete the other. The remaining row keeps its own title and done state. Empty submissions do nothing.',
 'The ref stores a counter without needing a screen update for that counter. The functional setters read the latest task array. The map changes only the matching ID.',
 'Add an unfinished count and a Show unfinished filter. Add two tasks with identical titles, then delete only one. Explain why title is not a suitable ID.',
 'Do not call tasks.push and reuse the same array. Keep FlatList inside a container with available height. IDs in this demo are local to one app session; a server-backed app needs a broader ID strategy.', ['list'])

rn('Screen Flow and Navigation Concepts',
 'Move from a campus directory to a selected office and back without showing every detail on the first screen.',
 'Represent a screen as state|Pass an item ID between views|Explain when a navigation library is needed',
 '''Navigation connects user tasks across screens. This small starter uses a discriminated union: either the list is active, or a detail screen has an office ID. The `kind` field narrows the type so TypeScript knows which data exists.

Pass the smallest useful route data, often an ID, then look up the current record. Copying an entire record into route state can become stale when the original data changes. Include a visible Back action and a fallback when an ID cannot be found.

This is a screen-flow prototype, not a complete mobile navigator. It has no native history stack, deep links, or Android hardware-back integration. Production-sized projects usually adopt Expo Router or React Navigation; the separate navigation bridge guide shows the next step without mixing Router setup into these App.tsx labs.''',
 'Think of a school map: you pick an office number, then view its details. The number is the route parameter; the office directory is the source of truth.',
 '''import { useState } from 'react';
import { View, Text, Button } from 'react-native';
const offices = [{ id: 'lib', name: 'Library', floor: 2 }, { id: 'reg', name: 'Registrar', floor: 1 }];
type Screen = { kind: 'list' } | { kind: 'detail'; id: string };
export default function App() {
  const [screen, setScreen] = useState<Screen>({ kind: 'list' });
  const office = screen.kind === 'detail' ? offices.find(o => o.id === screen.id) : undefined;
  return <View style={{ padding: 28, paddingTop: 60, gap: 16 }}>
    {screen.kind === 'list' ? <>
      <Text style={{ fontSize: 26 }}>Office Directory</Text>
      {offices.map(o => <Button key={o.id} title={o.name}
        onPress={() => setScreen({ kind: 'detail', id: o.id })} />)}
    </> : <>
      <Text>{office ? `${office.name}, floor ${office.floor}` : 'Office not found'}</Text>
      <Button title="Back to directory" onPress={() => setScreen({ kind: 'list' })} />
    </>}
  </View>;
}''',
 'Selecting Library shows floor 2. Back returns to the directory. Selecting Registrar shows floor 1. This demo uses its visible Back button.',
 'Check how kind changes the JSX branch. The ID connects screen state to the data array. An unknown ID produces a helpful fallback instead of a crash.',
 'Add a third office and a Settings screen with its own union case. Draw the screen-flow diagram before coding. Advanced extension: complete the Expo Router bridge in the supplementary guide.',
 'If TypeScript says id does not exist, narrow the union with screen.kind first. Conditional rendering is not a replacement for deep-link handling or native navigation history.', ['narrow','expo'])

rn('Effects and Lifecycle: Focus Timer',
 'Create a study timer, then discover why an uncleaned timer can keep working after its screen is gone.',
 'Use an effect for a timer|Clean up a subscription|Distinguish user actions from synchronization',
 '''Rendering describes the interface. An effect connects that interface to an external process such as a timer or subscription. The effect can return a cleanup function that stops the process when dependencies change or the component leaves the screen.

The dependency array tells React which values the effect relies on. Here the interval exists only while running is true. The callback uses a functional update so it does not depend on a stale seconds value. Setting up timers directly during rendering would create new timers repeatedly.

A one-second interval is an educational approximation, not a precise background alarm. Mobile operating systems may suspend JavaScript while the app is backgrounded. A robust elapsed-time display compares timestamps when resumed. Development checks can also run an effect setup and cleanup more than once; correct cleanup makes that safe.''',
 'Starting a study timer is like borrowing a classroom key. Cleanup is returning the key when finished. Kung hindi mo ibabalik, may resource na naiwan kahit tapos na ang activity.',
 '''import { useEffect, useState } from 'react';
import { View, Text, Button } from 'react-native';
export default function App() {
  const [seconds, setSeconds] = useState(0);
  const [running, setRunning] = useState(false);
  useEffect(() => {
    if (!running) return;
    const id = setInterval(() => setSeconds(value => value + 1), 1000);
    return () => clearInterval(id);
  }, [running]);
  return <View style={{ padding: 28, paddingTop: 60, gap: 16 }}>
    <Text style={{ fontSize: 28 }}>Focus: {seconds} seconds</Text>
    <Button title={running ? 'Pause' : 'Start'} onPress={() => setRunning(value => !value)} />
    <Button title="Reset" onPress={() => { setRunning(false); setSeconds(0); }} />
  </View>;
}''',
 'Start increases the count roughly once per second. Pause freezes it. Reset stops it and returns zero. Repeated Start/Pause cycles should not make counting accelerate.',
 'The handler changes running. React then synchronizes the interval through the effect. Cleanup receives the interval ID captured by that effect execution.',
 'Add a target duration and a “Break time!” message. Keep the phone foregrounded during the basic test. Stretch: replace interval counting with Date.now elapsed-time calculation and compare after backgrounding.',
 'If the timer accelerates, look for missing cleanup or duplicate intervals. An empty dependency array with a stale running value is another common error. A timer is not a guaranteed OS background service.', ['effect'])
