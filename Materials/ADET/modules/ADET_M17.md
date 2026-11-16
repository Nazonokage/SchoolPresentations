# ADET M17 · Testing, security and release planning

[Module index](README.md) · Pre-final · 60–90 minutes · 10-item quiz

## A. Lesson Preview & Review

**Would a last-minute fix accept an empty task?** Recall M16: failure paths matter. Today we write checks that catch defects before a release.

**Learning targets:** state a validation rule as a sentence, choose boundary test cases, see why passing tests prove only what they test, and match a change to the right delivery method.

**Trace:** Requirement → Test case → Build → Release check. Explain in your own words: the three supplied cases pass; adding the exact 80-character case exposes a boundary the starter does not test.

## B. Detailed Main Lesson

### In plain words

A test is an input plus the answer you expect. You run the code, compare, and report PASS or FAIL. A green result only means the cases you wrote passed. Good test cases sit at the edges of the rule.

| Concept | Why it exists / how it works | If misunderstood |
|---|---|---|
| Rule as a sentence | A title is valid if, after trimming, it has 1 to 80 characters | Code and expectations drift apart |
| Boundary cases | Test just below, at and just above each limit: 79, 80, 81 | Only testing the middle |
| Mutation check | Change `<= 80` to `< 80`; a good suite should fail | A suite that cannot detect a defect |
| Failure matrix | Offline, denied permission, expired session, empty database, malformed input | Only testing the happy path |
| Secrets | Keep them server-side; an `EXPO_PUBLIC_` variable is readable in the app | Leaking a private key |
| Delivery method | JS and asset changes can ship by update; native code needs a new build | Waiting for an update to fix a native change |

```text
rule -> cases: " " false | "Book" true | 81 x false  (missing: exactly 80 -> true)
mutate <=80 to <80  -> 81 still false (passes!)  -> add the 80 case -> now it FAILS, so it catches the defect
```

**Predict first:** change `<= 80` to `< 80`. Do the three supplied cases still pass?

| Input | Expected | With `<= 80` | With `< 80` |
|---|---|---|---|
| `" "` | false | pass | pass |
| `"Book"` | true | pass | pass |
| 81 characters | false | pass | pass |
| exactly 80 characters | true | pass | **fail** |

**Release rehearsal.** List which changes touch only JavaScript and which add a native permission or library. EAS Update can deliver compatible JS and assets; a native dependency needs a new binary with a matching runtime version. Review store rules and privacy disclosures before publishing. Subscriptions and ads need a separate design; they are research comparisons here.

**Misconception:** "all green means it works." It means these cases passed. Reproduce a reported defect before changing code.

### Common mistakes

- No test at the exact boundary.
- Letting an always-true function pass most cases.
- Shipping a native change as a JS update.

## C. Analogy, Guided Program & Practice

**Analogy.** Kapag green lahat, tingnan pa rin kung anong input ang hindi nasubukan. Parang pagsusuri ng timbangan: sinubukan mo ang 1 kilo at 10 kilos, pero paano kapag eksaktong 5?

**Use case:** a release checklist for a small campus app.

**Install first.** None.

**Run it.** Copy this lesson's complete `App.tsx` into your prepared project from M01 (replace the whole file). Run `npx tsc --noEmit`, then `npx expo start --offline` in the prepared lab or `npx expo start` while online. Metro transpiles; it does not type-check. Course versions are recorded in M01.

**Lab note.** Quiz modules do not need a delivery mode. The checks run with no network.

**App.tsx — complete checkpoint** · [Copyable file](../examples/M17/App.tsx)

```tsx
import { View, Text } from "react-native";

// The rule as a sentence: a title is valid if, after trimming, it has 1 to 80 characters.
function isValidTitle(text: string) {
  const trimmed = text.trim();
  return trimmed.length > 0 && trimmed.length <= 80;
}

type TestCase = { name: string; input: string; expected: boolean };

const testCases: TestCase[] = [
  { name: "whitespace only", input: " ", expected: false },
  { name: "normal title", input: "Book", expected: true },
  { name: "81 characters", input: "x".repeat(81), expected: false },
];

export default function App() {
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      {testCases.map((testCase, index) => (
        <Text key={testCase.name}>
          Case {index + 1} ({testCase.name}):{" "}
          {isValidTitle(testCase.input) === testCase.expected ? "PASS" : "FAIL"}
        </Text>
      ))}
    </View>
  );
}
```

**Breakdown.** `isValidTitle` trims, then checks the length. `testCases` is a list of named inputs with their expected answers. The screen compares the real result with the expectation and shows PASS or FAIL.

**Expected behavior.** The three supplied cases show PASS. Add the exact 80-character case (`"x".repeat(80)`, expected true) before the deliberate mutation.

**Ungraded practice.** Add the 80-character case, then mutate `<=` to `<` and watch it fail. Restore the sample.

**Troubleshooting.** A passing suite covers only the supplied cases. Reproduce a reported defect before optimizing.

## D. Assessment, Wrap-Up & References

### 10-item quiz

Give a short answer for each item. The guided change above is ungraded.

1. What is a boundary test?
2. What does a release candidate represent?
3. What is a runtime version used for?
4. Should a whitespace-only title pass?
5. Should "Book" pass?
6. Should 81 characters pass?
7. Why might a JavaScript update fail to supply a new native library?
8. Why is a private key in an `EXPO_PUBLIC_` variable unsafe?
9. What should precede store submission?
10. When is a new binary needed?

**Answer key (instructor).**
1. A test at the edge of a rule, such as the exact limit.
2. A build believed ready to ship, pending the final checks.
3. To decide which JavaScript updates are compatible with which native build.
4. No; it trims to empty.
5. Yes.
6. No; it is over 80.
7. Native code is inside the installed binary, which a JS update cannot change.
8. It is bundled into the app and readable by anyone.
9. A release rehearsal, tests, and a review of store rules and privacy disclosures.
10. When a native dependency, permission or runtime version changes.

**Wrap-up.** Explain how a requirement becomes a test case and why the 80-character case matters. Name the layer you would inspect first if the checks all passed but a user reported a bug.

[Runtime versions](https://docs.expo.dev/eas-update/runtime-versions/)

### Instructor notes

Pacing: 5 review, 15 explanation, 10 guided code, 25 quiz, 5 wrap-up. Unit-test libraries, EAS and store publishing are discussion only; no paid publishing or subscription integration is required. Device behavior is not yet recorded on the course baseline.
