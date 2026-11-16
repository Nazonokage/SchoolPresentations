# ANSWER KEY: Periodical Examination in React Web Systems

**Coverage:** Modules 6 to 15 | **Total Items:** 48 | *For instructor use only*

---

## Part I: Multiple Choice (Items 1–15)

| # | Ans | Why |
|---|-----|-----|
| 1 | **B** | The Virtual DOM diffs in-memory representations to minimize real DOM updates. |
| 2 | **A** | React relies on reference checks (`Object.is`) to decide when to re-render. |
| 3 | **B** | An empty dependency array runs the effect once after the initial mount. |
| 4 | **A** | `staleTime` is how long data counts as fresh before a background refetch. |
| 5 | **B** | Axios rejects on 4xx/5xx; `fetch` resolves unless the network fails. |
| 6 | **B** | Reducers must be pure: `(state, action) => newState`. |
| 7 | **B** | Changing `ref.current` persists the value without a re-render. |
| 8 | **B** | `<Outlet />` is the placeholder where matched child routes render. |
| 9 | **Easter egg item** | See note below. |
| 10 | **B** | `replace: true` swaps the history entry, so "Back" skips the login screen. |
| 11 | **A** | Users can bypass client-side guards and hit backend APIs directly. |
| 12 | **B** | `useCallback` memoizes function references for stable child props. |
| 13 | **B** | `invalidateQueries()` marks queries stale and triggers a background refetch. |
| 14 | **A** | Context prevents prop drilling through intermediate components. |
| 15 | **B** | `useParams()` reads dynamic URL segments. |

### Item 9 special credit rule

- **Technical answer:** `user?.account?.status ?? "Inactive"`. Optional chaining (`?.`) safely handles the missing `user.account` without a `TypeError` (it short-circuits to `undefined`), and nullish coalescing (`??`) falls back to `"Inactive"`. Result: `res === "Inactive"`.
- **Written on paper:** any choice (A–D) earns the standard **1 point**.
- **Bonus:** a student who orally explains to the instructor how `?.` and `??` work in this snippet earns **3 points**.

---

## Part II: Identification (Items 16–25)

| # | Answer |
|---|--------|
| 16 | **JSX** (JavaScript XML) |
| 17 | **CORS** (Cross-Origin Resource Sharing) |
| 18 | **useParams** |
| 19 | **AbortController** (accept `AbortSignal`) |
| 20 | **useMemo** |
| 21 | **`<Link>`** (accept `<NavLink>`) |
| 22 | **useMutation** |
| 23 | **Controlled component** (controlled input) |
| 24 | **useRef** |
| 25 | **invalidateQueries** |

---

## Part III: Guess the Output (Items 26–40)

| # | Answer | Explanation |
|---|--------|-------------|
| 26 | `A-B-C` | The spread creates a new array reference, so React re-renders. |
| 27 | `Product: 105` | `useParams` returns strings: `"10" + 5` concatenates to `"105"`. |
| 28 | `C-0` then `E-1` | Cleanup for the old value runs before the new effect. (On initial mount only `E-0` logs.) |
| 29 | `{ count: 15 }` | `10 + 5`. |
| 30 | **No** | Mutating `ref.current` does not trigger a re-render. |
| 31 | Nothing (`<div></div>`) | `false && ...` evaluates to `false`, which React renders as nothing. |
| 32 | `NO` | `fetch` resolves on 404, so `res.ok` is `false` and `.catch()` is not hit. |
| 33 | `"light"` | The nearest Provider wins. |
| 34 | `<Navigate to="/login" replace />` | Redirects to the login route. |
| 35 | Marked stale and refetched in the background | Applies to active (currently rendered) queries. |
| 36 | `1` | Both calls close over the same snapshot `val = 0`, so both set `1`. |
| 37 | `false` | Arrays are compared by reference, not by contents. |
| 38 | `null` | Returns the default value passed to `createContext`. |
| 39 | `Hello Guest` | `""` is falsy, so `||` returns `"Guest"`. |
| 40 | `undefined` | With no `default: return state;`, the reducer returns nothing, which breaks state. |

---

## Part IV: Fill in the Code (Items 41–48)

### Question A: Axios instance with JWT interceptor

| # | Answer |
|---|--------|
| 41 | `create` |
| 42 | `request` |
| 43 | `Authorization` |
| 44 | `reject` |

### Question B: Protected route component

| # | Answer |
|---|--------|
| 45 | `Navigate` *(45 and 46 may be in either order)* |
| 46 | `Outlet` |
| 47 | `Outlet` |
| 48 | `replace` |

---

## Scoring Summary

| Part | Items | Points each | Total |
|------|-------|-------------|-------|
| I. Multiple Choice | 15 | 1 | 15 |
| II. Identification | 10 | 1 | 10 |
| III. Guess the Output | 15 | 1 | 15 |
| IV. Fill in the Code | 8 | 1 | 8 |
| **Total** | **48** | | **48** (+2 bonus possible on Item 9) |
