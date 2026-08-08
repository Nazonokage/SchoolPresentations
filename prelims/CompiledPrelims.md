# HCI 2 - Comprehensive Reviewer
## Modules 2-7: Handheld Devices, Touch Interfaces, Auditory Systems, Visual Perception, QR Codes & Itertools

---

# MODULE 2: HANDHELD & WEARABLE DEVICES

## Core Concepts

### Technological Device Definition
> A technological device encompasses any computing system, cellular phone, smartphone, digital camera, video camera, audio recording instrument, or specialized electronic architecture engineered to create, store, securely isolate, or transmit information in the form of electronic data.

### Key Capabilities
- **Creation** - Capturing raw inputs (media, audio, biosignals) converting to digital metrics
- **Storage** - Locally retaining transactional, operational, and user telemetry data
- **Transmission** - Moving payloads across distributed computing networks

---

## Handheld Device Anatomy

### Core Definition
A computer or digital engine small enough to be sustained, operated, and manipulated completely within the palm of a human hand.

### Essential Hardware
- **Display Systems:** LCD or OLED frameworks
- **Input Interfaces:** Dual-modality (touchscreens + physical keypads or virtual matrices)
- **Connectivity:** Wi-Fi, Bluetooth, cellular bands (3G+), NFC

---

## Historical Timeline: The Mobility Curve

| Era | Development |
|-----|-------------|
| **1985-1995** | Genesis of Portability - first voice transceivers, battery life engineering |
| **2000** | Convergence Threshold - digital networks, dual-band radios, basic color screens |
| **2005** | High-Speed Infrastructure - GPRS/3G, high-res displays, MP3 engines |
| **2007** | Mainstream Milestone - Apple iPhone & Microsoft Surface launch |
| **2009+** | Modern Smartphone Matrix - capacitive touchscreens, GPS, advanced PDAs |

---

## Taxonomy of Handheld Form Factors

### Personal Digital Assistants (PDAs)
- Standalone personal information managers (calendars, address books)
- **Displaced by** smartphones (Android/iOS)

### Tablets & Slates
- Wireless portable PC with expansive touch-screen
- Fits between smartphone and laptop

### Portable Media Players (PMPs)
- Optimized for storing/executing digital media
- Supports audio, images, video

### Auxiliary Handhelds
- Pagers, feature phones, satellite communication
- Game consoles, GPS systems, fax/data terminals

---

## Wearable Systems

### Core Definition
Products controlled by integrated electronic components and embedded micro-software engines incorporated into clothing or worn on the body.

### Primary Archetypes
- **Smart Glasses** - Optical head-mounted displays (OHMDs)
- **Smartwatches** - Wrist-worn computers
- **Biosensors** - Medical-grade sensors on skin
- **Head-Mounted Displays (HMDs)** - AR/VR devices

### Wearable Classifications

| Type | Examples | Function |
|------|----------|----------|
| **Smart Jewelry** | Rings, bracelets, interactive pins | Micro-displays, vibration |
| **Body-Mounted Biosensors** | Medical sensors | Monitor biological data |
| **Fitness Trackers** | Wristbands, straps | Track movement, vital signs |
| **Smart Clothing** | Tech Textiles | Biometric circuitry, temperature control |
| **AI Hearing Aids** | Hearables | Noise filtering, fitness tracking, translation |

---

# MODULE 3: TOUCH USER INTERFACES (TUI)

## Definition
A computer-pointing technology based upon the sense of touch (haptics).

### GUI vs. TUI
| GUI | TUI |
|-----|-----|
| Relies primarily on sight | Relies on sense of touch |
| Windows, icons, menus | Direct physical manipulation |
| Indirect input (mouse) | Direct input (touch) |

### Accessibility Benefit
Provides tactile/Braille input - highly beneficial for users with visual impairments.

### Historical Milestone
- Early concepts: 1960s
- **Mainstream breakthrough: 2007** (Microsoft Surface + Apple iPhone)

---

## Design Considerations (Wigdor & Wixon, 2011)

1. **Extension of the Body** - Interface should feel like natural extension of user's body
2. **Natural Experience** - Intuitive interaction mimicking real-world physics
3. **Immediate Feedback** - System must respond instantly to touch
4. **Size Factor** - Account for ergonomic constraints and finger size

---

## Core Interaction Techniques

### Tapping-it
- **Most common gesture** - selecting item by briefly touching it
- Fundamental to almost every modern UI action

### Crossing-in
- Selecting target by dragging across or crossing it
- **Advantage:** Improved target selection for motor-impaired individuals
- Useful in high-density interfaces

### Directional Gesturing
- Only technique that **eliminates** strict requirement for predefined target spaces
- Trigger actions based on motion paths anywhere on device surface

---

## Core Touchscreen Technologies

### 1. Wire Resistive Touchscreen

**Construction:** Glass base + film screen layer, each covered with thin metallic layer separated by narrow space

**How it works:** Touch pressure forces layers to make contact, changing voltage flow to locate touch point

| Advantages | Disadvantages |
|------------|---------------|
| Activated by ANY input object (finger, stylus, gloved hand, pen) | Lower image definition |
| Distinct tactile feel | Highly vulnerable to scratches/damage |
| Cost-effective | |
| Low power consumption | |
| Resistant to contaminants (dust, oil, moisture) | |

---

### 2. Surface Capacitive Touchscreen

**Construction:** Transparent electrode layer on glass substrate, protected by covering layer

**How it works:** Reacts to static electrical capacity of human body; draws charges from corner sensors to calculate coordinates

| Advantages | Disadvantages |
|------------|---------------|
| Superior image clarity | Can ONLY be activated by human skin contact |
| Durable screen integration | Specialized electrical stylus required for non-skin |

---

### 3. Projected Capacitive Touchscreen (P-CAP)

**How it works:** Glass with embedded transparent electrode films + IC chip; detects via 3D electrostatic field

| Advantages | Disadvantages |
|------------|---------------|
| Excellent image clarity | Requires bare finger or specialized capacitive stylus |
| High scratch resistance | Susceptible to EMI/RFI interference |
| Resilient against liquids/contaminants | |
| Full multi-touch support | |
| Can activate with thin surgical/cotton gloves | |

---

### 4. Surface Acoustic Wave (SAW) Touchscreen

**How it works:** Ultrasonic wave transducers/receivers along edges; pressing glass absorbs part of ultrasonic wave grid

| Advantages | Disadvantages |
|------------|---------------|
| Excellent image clarity and light transmission | Must activate with bare finger or thin/surgical glove |
| High scratch resistance | Highly sensitive to EMI/RFI |
| Supports multi-touch | Contaminants can disable |

---

### 5. Infrared (IR) Touchscreen

**How it works:** Infrared emitters/sensors around outer frame create invisible grid of light beams; interruption maps location

| Advantages | Disadvantages |
|------------|---------------|
| **Highest** image clarity and light transmission | Won't activate with hard items (pen, credit card, fingernails) |
| Infinite touch-life durability | Water droplets can block beams |
| Impervious to scratches | Accidental activation (beams above glass) |
| Exceptional scratch resistance | Sensitive to snow, rain, ambient light |
| | Higher cost |

---

### Comparison Summary

| Technology | Activation | Clarity | Multi-touch | Durability | Cost |
|------------|------------|---------|-------------|------------|------|
| **Resistive** | Any object | Low | No | Vulnerable | Low |
| **Surface Capacitive** | Skin only | Good | No | Durable | Medium |
| **Projected Capacitive** | Skin/thin glove | Excellent | Yes | Scratch-resistant | High |
| **SAW** | Bare finger/soft glove | Excellent | Yes | Scratch-resistant | High |
| **Infrared (IR)** | Any object (blocks beams) | Highest | Yes | Infinite | Highest |

---

# MODULE 4: AUDITORY INTERFACES & SONIFICATION

## Introduction

### Why Auditory Interfaces?
- Complement visual interfaces
- Reduce **visual overload**
- Support tasks where sight is limited
- Enable multitasking (e.g., while driving)
- Provide situational awareness

### Definition
A bidirectional, communicative connection between human user and technical product:
- **Machine side:** Machine listening, speech recognition, dialogue systems
- **Human side:** Auditory displays (sounds to send information)

---

## The Auditory Interface Processing Loop

```
DATA → A (Representation & Preprocessing) → B (Application, Processing Loop) → C (Sonification Techniques/Rendering) → D (Technical Sound Display) → USER
                                                                                    ↑                                    |
                                                                                    └────────────── INTERACTIONS ──────┘
```

### Stages:
- **Data:** Raw information
- **A: Representation & Preprocessing** - Translate raw data for processing
- **B: Application, Processing Loop** - Computation cycle
- **Interactions:** User input; feeds back to processing loop
- **C: Sonification Techniques (Rendering)** - Convert data to sound waves/signals
- **D: Technical Sound Display** - Physical output (speaker)

---

## Types of Auditory Interfaces

### Type 1: Audification

**Definition:** Direct translation of a data waveform to the audible domain

**How it works:**
- Interprets data sequence as audio waveform
- Input directly mapped to sound pressure levels
- Listener hears periodic components as frequencies

**Requirement:** Works best with large datasets with periodic features

**Example:** Seismic/Earthquake Data - speeding up playback of vibrations creates rumble/roar

---

### Type 2: Sonification

**Definition:** Use of non-speech audio to convey information or perceptualize data

**Advantages:** Auditory perception excels at:
- Temporal (time) resolution
- Spatial (location) perception
- Amplitude (loudness) discrimination
- Frequency resolution

**Challenge:** Difficult to present/analyze data using only sound; many implementations coded from scratch; requires sufficient "context" for understanding

**Example:** Geiger Counter - rate of clicks indicates radiation level (faster clicks = higher radiation)

---

### Type 3: Earcon

**Definition:** Brief, distinctive sound that represents a specific event

**Origin:** Pun on "icon" - coined by **D.A. Sumikawa in 1985**
- Visual icon = "eye-con"
- Auditory icon = **"earcon"**

**Characteristics:** Usually synthesized tones or sound patterns

**Examples:**
| Application | Sound |
|-------------|-------|
| Operating Systems | Beep on error; startup/shutdown sounds; low battery alert |
| Broadcast Media | Emergency Broadcast System alert; NBC's three-tone chime |

---

### Type 4: Voicemail System

**Definition:** Computer-based system allowing users to exchange personal voice messages

**Also known as:** Voice message or voice bank

**Functionality:**
- Delivers voice information
- Processes transactions using ordinary telephone

**Modern Context:**
- Almost all cell phone services include voicemail
- Corporate PBX systems include internal voice-messaging

**Example:** *98 Vertical Service Code - US landlines dial *98 to access voicemail box

---

## Comparison Table

| Type | Definition | Example |
|------|------------|---------|
| **Audification** | Direct waveform translation | Seismic data sped up to sound |
| **Sonification** | Non-speech audio conveying data | Geiger counter clicks |
| **Earcon** | Brief symbolic sound for events | OS error beep, NBC chime |
| **Voicemail** | Voice message exchange | *98 voicemail access |

---

# MODULE 5: QR CODES & PYTHON PERMUTATIONS

## QR Codes

### Definition
A 2D matrix barcode (Quick Response code) that stores data in a grid of modules.

### History
| Year | Development |
|------|-------------|
| **1960s** | Traditional 1D barcodes (railroads) |
| **1994** | QR Code invented by **Denso Wave** (Toyota subsidiary) - for vehicle/parts tracking |
| **2000** | Approved as ISO international standard |

### Barcode vs. QR Code Comparison
| Feature | 1D Barcode | QR Code |
|---------|------------|---------|
| Structure | Parallel lines of varying widths | 2D grid of modules |
| Read Direction | Left to right | Any direction |
| Data Capacity | Small (ID number) | Large (Kanji, Kana, alphanumeric) |
| Analogy | A sentence | A paragraph |

---

## QR Code Variants

| Variant | Description | Capacity |
|---------|-------------|----------|
| **Micro QR Code** | Highly compact, small spaces | 11×11 modules, up to 21 chars |
| **Model 1 QR Code** | Original prototype | 1-14 versions, ~707 chars max |
| **Model 2 QR Code** | Improved with alignment pattern | 1-40 versions, 4,296 chars max |
| **IQR Code** | Square/rectangular formats | 61 available formats |
| **SQRC** | Secret function, restricted reading | Public + password-locked data |
| **Frame QR** | Customizable frame area in center | Logo-safe, still scannable |

**Analogy:** "A set of camera lenses" - same basic function, different lens for different job.

---

## Anatomy of a QR Code

1. **Finder Patterns (3 corners)**
   - Bold squares that tell scanner orientation
   - Like corner flags on a map

2. **Data Modules**
   - Scattered small squares carrying encoded bits
   - **Position, not color, carries information**

3. **Quiet Zone (Border)**
   - Outer safety margin (minimum 4 modules)
   - Helps scanners find the code

4. **Frame/Logo Area** (Frame QR)
   - Reserved center zone for branding

---

## QR Code Error Correction Levels

| Level | Correctable Damage | Best For |
|-------|-------------------|----------|
| **L** | Up to 7% | Clean environments |
| **M** (Default) | Up to 15% | General use |
| **Q** | Up to 25% | Business/commercial |
| **H** | Up to 30% | Logos/graphics, high damage risk |

**Analogy:** "A safety net with different mesh sizes" - L is small net (minor falls), H is dense net (catches almost anything).

---

## QR Code Generation with Python

### Installation
```python
# pip install qrcode pillow
import qrcode
```

### Quick Generation
```python
# Fastest method - uses defaults
img = qrcode.make("https://your-target-url.com")
img.save("quick_qr.png")
```

### Advanced Customization
```python
# Control version, size, error correction
qr = qrcode.QRCode(
    version=3,              # 1-40 (matrix size)
    box_size=12,            # pixels per module
    border=4,               # quiet zone (min 4)
    error_correction=qrcode.constants.ERROR_CORRECT_M  # L, M, Q, H
)
qr.add_data("Customized Styling Information")
qr.make(fit=True)

# Custom colors
styled_img = qr.make_image(fill_color="darkgreen", back_color="lightyellow")
styled_img.save("styled_qr.png")
```

### QRCode Parameters

| Parameter | Type/Range | Description |
|-----------|-----------|-------------|
| **version** | Integer (1-40) | Controls matrix size; Version 1 = 21×21 |
| **error_correction** | Constants (L, M, Q, H) | Determines survivability of damage |
| **box_size** | Integer | Pixels per module (grid cell) |
| **border** | Integer (min: 4) | Thickness of quiet zone |

---

## QR Code Decoding with OpenCV

```python
import cv2

# Initialize detector
detector = cv2.QRCodeDetector()

# Detect and decode from image
data, points, straight_qrcode = detector.detectAndDecode(cv2.imread("qr_code.png"))

if points is not None:
    print(f"Decoded Data: {data}")
else:
    print("No valid QR code detected.")
```

**Features:**
- Handles perspective distortion automatically
- Handles rotation automatically
- Returns decoded data, corner points, straightened version

**Analogy:** "A barcode scanner app" - finds pattern, corrects angle, extracts text.

---

## Python Permutations (itertools)

### Definition
An arrangement of a set where **order of elements matters**

### Key Concepts
| Term | Description |
|------|-------------|
| **Permutation** | Ordering of elements; order changes identity |
| **Combination** | Selection of elements; order doesn't matter |
| **n!** (n factorial) | Number of permutations for n unique items |

### Examples
- 4 runners = 4! = **24** possible finish orders
- 3-digit padlock: 4-1-7 ≠ 7-1-4 (order matters)

### itertools.permutations()

```python
import itertools

# Permuting numbers
val = [1, 2, 3, 4]
perm_set = itertools.permutations(val)

for i in perm_set:
    print(i)
# Output: (1,2,3,4), (1,2,4,3), ... 24 total (4!)

# Permuting letters in a string
name = "someone"
for x in itertools.permutations(name):
    print("".join(x))
# Output: 7! = 5040 arrangements
```

### Key Features
- **Lazy evaluation** - generates only when asked (like vending machine, not printed catalog)
- **Memory efficient** - doesn't store all permutations at once
- Works on **any iterable** (lists, strings, tuples)

### Quick Reference
| Set | Number of Permutations |
|-----|----------------------|
| 1 item | 1! = 1 |
| 2 items | 2! = 2 |
| 3 items | 3! = 6 |
| 4 items | 4! = 24 |
| 7 items | 7! = 5,040 |

---

# MODULE 6: HUMAN VISUAL SENSATION, PERCEPTION & COGNITION

## The Visual Pathway

```
Light Stimulus → SENSATION (eye/retina) → PERCEPTION (brain/interpretation) → COGNITION (memory & action)
```

**Analogy:** "A camera pipeline"
- Sensation = sensor capturing raw light
- Perception = image processor recognizing a face
- Cognition = deciding to smile or wave (action following recognition)

---

## Sensation vs. Perception

| Feature | Visual Sensation | Visual Perception |
|---------|------------------|-------------------|
| **Definition** | Physical experience of light entering eyes | Mental ability to recognize colors, patterns, structures |
| **Nature** | Physiological process (cornea, pupil, lens, retina, rods, cones, optic nerve) | Physiological + mental + psychological interpretations |
| **Consistency** | Fundamentally same for all sighted individuals | Highly subjective; varies by experience, culture, expectations |
| **Behavior** | Identical stimuli yield identical sensations | Same sensory details interpreted differently based on context |

**Analogy:** "Camera sensor vs. photo editor"
- Sensation = raw capture (same for everyone)
- Perception = editing (same raw image = sunset for one, warning sky for another)

---

## How the Eye Works

### Structure
- Slightly asymmetrical sphere, 20-25mm diameter
- ~6.5cc volume
- Acts like a physical camera

### Image Formation
- Lens refracts light onto retina's photoreceptive cells (rods and cones)
- Rods and cones convert light photons into neural impulses → brain

### Brightness Adaptation
- Eye cannot transition instantly between extreme dark and light
- Adjusts sensitivity over time

**Analogy:** "Camera with autofocus and auto-ISO"
- Pupil = aperture
- Lens = focuses light
- Retina = sensor
- Rods/cones = high-ISO vs. low-ISO pixels

---

## Cognition

### Definition
The mental engine that drives action; transforms perceived information into meaningful action.

### Components
- **Basic mental processes:** Attention, awareness, orientation
- **Complex operations:** Memory, language, reasoning, problem-solving, decision-making

**Analogy:** "Decision-maker in a control room"
- Sensation = screen displaying data
- Perception = operator recognizing pattern
- Cognition = operator deciding which button to press

---

## UI Design Principles (Based on Visual System)

1. **High Contrast Elements** - Interactive components must stand out sharply
2. **Consistent Luminance** - Abrupt brightness changes cause visual fatigue
3. **Clear Structure** - Grouping elements guides attention
4. **Container Grouping** - Styled containers focus visual attention

**Analogy:** "Lighting a stage" - smooth, consistent luminance keeps users comfortable and focused.

---

# MODULE 7: ADVANCED QR CODES & ITERTOOLS CHUNKING

## itertools Chunking (Grouper Recipe)

### The Problem
Need to process data in fixed-size batches (chunks) for:
- API pagination
- Memory-limited environments
- Parallel processing
- Rate-limited APIs

### The Solution: grouper()

```python
import itertools as it

def grouper(inputs, n, fillvalue=None):
    """Collect data into non-overlapping, fixed-length chunks"""
    iters = [iter(inputs)] * n
    return it.zip_longest(*iters, fillvalue=fillvalue)

# Example
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
chunked_data = list(grouper(alpha, 3))
print(chunked_data)
# Output: [('a','b','c'), ('d','e','f'), ('g','h','i'), ('j','k','l'), ('m', None, None)]
```

### How It Works
1. Creates **n references** to the same iterator
2. Uses `zip_longest` to pair elements from each reference
3. Pads with `fillvalue` when one reference runs out
4. **Memory-efficient** - never materializes whole input at once

### Key Concepts
| Feature | Description |
|---------|-------------|
| **Memory efficiency** | Processes one chunk at a time |
| **Predictable batches** | Fixed-size groups |
| **Lazy evaluation** | Only consumes input as iterated |
| **Works with any iterable** | Lists, generators, file handles, database cursors |

**Analogy:** "Eating a pizza slice by slice" - you don't put whole pizza in your mouth at once; take one slice (chunk), eat it, take next.

---

## QR Code Complete Workflow

### Generation Workflow
```python
# 1. Install libraries
# pip install qrcode pillow opencv-python

# 2. Generate basic QR
import qrcode
img = qrcode.make("https://example.com")
img.save("basic_qr.png")

# 3. Generate styled QR
qr = qrcode.QRCode(version=3, box_size=12, border=4)
qr.add_data("Styled content")
qr.make(fit=True)
styled = qr.make_image(fill_color="darkgreen", back_color="lightyellow")
styled.save("styled_qr.png")

# 4. Decode QR
import cv2
detector = cv2.QRCodeDetector()
data, points, _ = detector.detectAndDecode(cv2.imread("styled_qr.png"))
print(f"Decoded: {data}")
```

### Error Correction Levels Summary

| Level | Code | Corrects | Use Case |
|-------|------|----------|----------|
| L | ERROR_CORRECT_L | 7% | Clean, controlled environment |
| M | ERROR_CORRECT_M | 15% | **Default** - general use |
| Q | ERROR_CORRECT_Q | 25% | Business/commercial |
| H | ERROR_CORRECT_H | 30% | Logos, graphics, high damage risk |

---

## Quick Reference: Module Summary

| Module | Topic | Key Takeaway |
|--------|-------|--------------|
| **2** | Handheld & Wearable Devices | Evolution from PDAs to smartwatches; form factors and ecosystems |
| **3** | Touch User Interfaces | 5 touchscreen technologies; design considerations; interaction techniques |
| **4** | Auditory Interfaces | 4 types: Audification, Sonification, Earcon, Voicemail |
| **5** | QR Codes & Permutations | QR variants; generation/decoding; itertools.permutations |
| **6** | Visual Sensation/Perception/Cognition | Sensation→Perception→Cognition pathway; UI design implications |
| **7** | Advanced QR & Itertools | grouper recipe; styled QR generation; OpenCV decoding |

---

## Common Quiz Questions

### True/False
1. QR codes store data in a 1D line of modules. → **FALSE** (2D grid)
2. The three finder patterns help the scanner determine orientation. → **TRUE**
3. Resistive touchscreens can be activated with any input object. → **TRUE**
4. Visual sensation is a subjective process that varies person-to-person. → **FALSE** (sensation is physical/consistent; perception is subjective)
5. Infrared touchscreens can be activated with hard plastic pens. → **FALSE** (requires object that blocks light beams)
6. The grouper function creates n independent iterators. → **FALSE** (n references to the same iterator)
7. ERROR_CORRECT_L can correct up to 15% of errors. → **FALSE** (7%; M=15%, Q=25%, H=30%)
8. Cognition includes memory, reasoning, and decision-making. → **TRUE**

### Identification Terms
| Term | Description |
|------|-------------|
| **Finder patterns** | Three corner squares in QR codes for orientation |
| **Earcon** | Brief distinctive sound representing an event |
| **Audification** | Direct waveform translation to audible domain |
| **Sonification** | Non-speech audio to convey information |
| **Crossing-in** | Selecting target by dragging across or crossing it |
| **Tapping-it** | Most common gesture; selecting by brief touch |
| **Quiet zone** | Outer white safety border of QR code |
| **Pupil** | Colored part of eye controlling light entry |
| **Iris** | Controls pupil size |

### Fill in the Blanks
1. The grouper function returns an iterator of ______ when zipped. → **tuples**
2. To style a QR code, you pass ______ and back_color to make_image. → **fill_color**
3. The default error correction level in qrcode is ______. → **ERROR_CORRECT_M**
4. The retina converts light photons into ______ impulses. → **neural**
5. What does HCI stand for? → **Human-Computer Interaction**

---

## Practical Code Snippets

### Chunking with grouper
```python
import itertools as it

def grouper(inputs, n, fillvalue=None):
    iters = [iter(inputs)] * n
    return it.zip_longest(*iters, fillvalue=fillvalue)

data = range(10)
chunks = list(grouper(data, 3))
# [(0,1,2), (3,4,5), (6,7,8), (9, None, None)]
```

### QR Generation
```python
import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("https://example.com")
qr.make(fit=True)
img = qr.make_image(fill_color="#1a1a2e", back_color="#e2d9f5")
img.save("custom_qr.png")
```

### QR Decoding
```python
import cv2
detector = cv2.QRCodeDetector()
data, pts, _ = detector.detectAndDecode(cv2.imread("qr.png"))
print(data) if pts is not None else print("No QR found")
```

### Permutations
```python
import itertools
items = ['A', 'B', 'C']
for p in itertools.permutations(items):
    print(p)
# ('A','B','C'), ('A','C','B'), ('B','A','C'), ('B','C','A'), ('C','A','B'), ('C','B','A')
```

---

## Key Equations & Values

| Formula | Value |
|---------|-------|
| n! (n factorial) | n × (n-1) × (n-2) × ... × 1 |
| 3! | 6 |
| 4! | 24 |
| 5! | 120 |
| 7! | 5,040 |

---

**End of Reviewer**