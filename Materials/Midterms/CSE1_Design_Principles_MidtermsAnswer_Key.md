# CSE1 — The Anatomy of Good Design: Principles & CSS
## Answer Key

**Total: 60 pts**

---

## PART I — MULTIPLE CHOICE (20 pts)

| # | Answer | # | Answer |
|---|--------|---|--------|
| 1 | **B. Visual Hierarchy** 
| 2 | **B. Symmetrical** 
| 3 | **B. color** 
| 4 | **C. Alignment** 
| 5 | **A. Proximity** 
| 6 | **B. Repetition** 
| 7 | **C. Improves readability/focus** 
| 8 | **B. line-height** 
| 9 | **C. Dominant color** 
| 10 | **C. Everyone, incl. visual impairments** 

| 11 | **B. Grid & Layout** |
| 12 | **A. CSS Grid** |
| 13 | **B. Responsive Design** |
| 14 | **B. media query** |
| 15 | **A. Clear navigation** |
| 16 | **B. alt** |
| 17 | **B. Keyboard accessibility** |
| 18 | **B. margin** |
| 19 | **B. padding** |
| 20 | **A. Style on mouse-over** |
---

## PART II — IDENTIFICATION / ENUMERATION (10 pts)

1. **Contrast**
2. **Repetition**
3. **Visual Hierarchy**
4. **Asymmetrical** (balance)
5. **White Space** (or Negative Space)
6. **60-30-10 rule** (or 60-30-10 color rule)
7. **Grid** (or Grid system / 12-column grid)
8. **Accessibility**
9. **Dominant, Secondary, Accent**
10. **Size, Color, Weight/Contrast, Position**  
    *(any 3 of: Size, Color, Contrast/Weight, Position/Spacing, Typography)*

---

## PART III — SITUATIONAL IDENTIFICATION (10 pts)

1. **Visual Hierarchy**
2. **Repetition**
3. **Proximity**
4. **Symmetrical balance** (or Symmetry)
5. **Contrast** (color contrast)
6. **Accessibility** (alt text for accessibility)
7. **Alignment**
8. **Responsive Design**
9. **Contrast** (or Visual Hierarchy / Affordance)
10. **White Space** (or Negative space)

---

## PART IV — GUESS THE OUTPUT (5 pts)

1. **Red**
2. **Gold**
3. **Centered** (horizontally in the middle)
4. **It fades in** (from opacity 0 → 1 over 1 second)
5. **The space OUTSIDE the card’s border** (margin 20px > padding 10px)

---

## PART V — CODING PROBLEMS (15 pts)

### 1. The 60-30-10 Rule

```css
.dominant {
  background-color: #1A1A2E;
}

.secondary {
  background-color: #6A4C93;
}

.accent {
  background-color: #F4A300;
}
```

### 2. Responsive Design

```css
.container {
  display: flex;
  flex-wrap: wrap;
}

@media (max-width: 767px) {
  .container {
    flex-direction: column;
  }
}
```

### 3. Alignment & Repetition

```css
.btn {
  padding: 10px 20px;
  border-radius: 6px;
  text-align: center;
}
```

---

***End of Answer Key***
