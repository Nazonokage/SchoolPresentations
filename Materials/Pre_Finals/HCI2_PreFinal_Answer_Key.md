# ITE 380 Human Computer Interaction 2 | Pre-Final Periodical Exam: Answer Key

**Total:** 60 points | **Time:** 1.5 hours | *For instructor use only.*

| Part | Items | Points each | Total |
|---|---|---|---|
| I. Multiple Choice | 1–20 | 1 | 20 |
| II. Identification | 21–35 | 1 | 15 |
| III. Enumeration | 36–45 | 1 | 10 |
| IV. Fill in the Code | 46–48 (5 blanks each) | 1 per blank | 15 |
| **Total** | **48** | | **60** |

---

## I. Multiple Choice

| # | Ans | # | Ans |
|---|---|---|---|
| 1 | **C** | 11 | **B** |
| 2 | **B** | 12 | **D** |
| 3 | **C** | 13 | **D** |
| 4 | **A** | 14 | **B** |
| 5 | **B** | 15 | **A** |
| 6 | **B** | 16 | **D** |
| 7 | **B** | 17 | **C** |
| 8 | **C** | 18 | **B** |
| 9 | **C** | 19 | **A** |
| 10 | **C** | 20 | **A** |

---

## II. Identification

| # | Answer |
|---|---|
| 21 | **Location-Based AR** |
| 22 | **Overlay AR** |
| 23 | **pyttsx3** |
| 24 | **Geocoding** |
| 25 | **No-Code SaaS** (no-code / drag-and-drop WebAR platform) |
| 26 | **Marker-Based AR** |
| 27 | **mpg321** |
| 28 | **Reverse Geocoding** |
| 29 | **Accessibility & Usability** |
| 30 | **`<iframe>`** |
| 31 | **ARGO** |
| 32 | **pip** |
| 33 | **gTTS** |
| 34 | **Projector Mapping** (Projection-Based AR) |
| 35 | **`pyttsx3.init()`** |

---

## III. Enumeration

**Items 36–38: Core Features of AR** (any order)

- Combination of real and virtual worlds
- Real-time interaction
- Accurate 3D registration

**Items 39–41: Ways AR Enhances HCI** (any order)

- Immersive & Interactive Experience
- Accessibility & Usability
- Creativity & Learning

**Items 42–45: AR Display Hardware** (any 4 of the following)

- Head-Mounted Display (HMD)
- Eyeglasses
- Head-Up Display (HUD)
- Contact Lenses
- Virtual Retinal Display (VRD)
- Eyetap
- Handheld
- Projector Mapping

---

## IV. Fill in the Code (1 point per blank)

### 46. QR Code Bridge (5 pts)

| Blank | Answer |
|---|---|
| [1] | `add_data` |
| [2] | `make_image` |
| [3] | `back_color` |
| [4] | `save` |
| [5] | `print` |

```python
import qrcode
qr = qrcode.QRCode(
  version=1,
  error_correction=qrcode.constants.ERROR_CORRECT_L,
  box_size=10,
  border=4,
)
ar_experience_url = "https://www.example.com"
qr.add_data(ar_experience_url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr-code.png")
print("QR Code saved as qr-code.png!")
```

### 47. Offline TTS (5 pts)

| Blank | Answer |
|---|---|
| [1] | `import` |
| [2] | `init` |
| [3] | `input` |
| [4] | `say` |
| [5] | `runAndWait` |

```python
import pyttsx3
engine = pyttsx3.init()
text = input("Enter the text you want to hear: ")
engine.say(text)
engine.runAndWait()
print("Finished speaking!")
```

### 48. Interactive Map Prototype (5 pts)

| Blank | Answer |
|---|---|
| [1] | `onclick` |
| [2] | `prompt` |
| [3] | `==` (also accept `===`) |
| [4] | `open` |
| [5] | `innerHTML` (accept `.innerHTML`) |

```html
<button onclick="map_data()">Map it</button>
<p id="demo"></p>
<script>
function map_data() {
    let x = prompt("Enter location");
    if (x == "iloilo") {
        window.open(
  "https://www.google.com/maps/place/Iloilo+City");
    } else {
        document.getElementById("demo")
            .innerHTML = "404! Location not found.";
    }
}
</script>
```

**Grading notes:** Spelling and capitalization must be exact (`runAndWait`, `innerHTML`, `onclick`, `back_color`). The Q48 check is case-sensitive, as in the reviewer (typing "Iloilo" would not match).

---

## Source check (against hci2_pre_fi_reviewer.docx)

All 48 items trace back to the reviewer (Modules 16, 17, 19, 20, 22, 23).

- **Q46** follows the M22 QR script: same `QRCode(...)` settings, `fill_color="black"`, `back_color="white"`, `qr-code.png`.
- **Q47** follows the M19 pyttsx3 script: `init()`, `input()`, `say()`, `runAndWait()`, "Finished speaking!".
- **Q48** follows the M23 `map.html` prototype: `onclick`, `prompt("Enter location")`, `x == "iloilo"`, `window.open`, `innerHTML` error message.
- **Q7 and Q27:** M20 says Windows users must install `mpg321.exe` and add it to PATH, and plays audio with `os.system("mpg321 output.mp3")`.
- **Q33:** M19 describes gTTS as a "single end-to-end model" that generates speech directly from characters.
- **MC answer spread:** B is correct for 7 of 20 items, and D for only 3.
