# Gemini PPT Prompt — CS6140 Final Project Presentation

## HOW TO USE THIS FILE

1. Open Google Gemini (gemini.google.com) or Gemini in Google Slides
2. Attach these 4 image files from the project:
   - `figures/roc_curve.png`
   - `figures/feature_importance.png`
   - `figures/system_tradeoff_curve.png`
   - `report/figures/label_distribution.png`
3. Paste the GEMINI PROMPT below, then paste the SLIDE CONTENT after it

---

## GEMINI PROMPT (paste this first)

```
Create a professional 8-slide PowerPoint presentation for a 5-minute academic conference lightning talk.

Design requirements:
- Theme: Dark background (deep navy or charcoal), white/light text
- Accent color: Teal or orange for highlights and callout boxes
- Font: Clean sans-serif (Montserrat or Calibri)
- Each slide has ONE clear headline in large bold text at the top
- Bullet points are SHORT — max 10 words each
- Use the attached images exactly where specified — do not move them
- Add subtle slide numbers bottom right
- NO clip art, NO stock photos — clean and minimal
- The last slide should have a subtle gradient footer with the GitHub repo URL

Here is the complete slide-by-slide content:
```

---

## SLIDE CONTENT (paste after the prompt above)

---

### SLIDE 1 — Title Slide

**Layout:** Centered, full-width title

**Headline (large, bold):**
Incentive-Aware Multi-Objective Matching
for Peer-to-Peer Commuter Carpooling

**Subtitle:** CS6140 Machine Learning · Final Project

**Author line:** Krunal Savaj · Khoury College of Computer Sciences · Northeastern University

**Bottom tag:** April 2026

**Image:** None. Clean dark title slide only.

---

### SLIDE 2 — Problem & Motivation

**Layout:** Left text (60%) + Right diagram box (40%)

**Headline:** The average US car carries **1.08 passengers** during peak hours

**Bullets (left side):**
- Uber/Lyft built for professional drivers — not regular commuters
- Commuters have fixed routes and low detour tolerance
- A 3 km detour on a 4 km commute = unacceptable
- A 3 km detour on a 40 km commute = perfectly fine
- No existing algorithm models this trade-off

**Right side — draw a simple text diagram box:**
```
Driver A:  Bronx → Midtown (8.2 km)
           ↓
  + Rider B:  1.8 km detour, $22 fare  ✅ ACCEPT
  + Rider C:  1.8 km detour,  $3 fare  ❌ REJECT
```
Label the box: *"Same detour. Different economics. Only ML handles this."*

**Image:** None — diagram is text-based, draw it in the slide.

**Speaker note:** "Within the first 40 seconds — hook the audience with the 1.08 stat."

---

### SLIDE 3 — The Data Problem

**Layout:** Left bullets (55%) + Right image (45%)

**Headline:** No P2P carpooling dataset exists. We built one.

**Bullets (left side):**
- Source: NYC Taxi & Limousine Commission — 3.5M trips, August 2025
- Problem: TLC removed GPS coordinates in 2016 (privacy)
- Solution: Synthesize coordinates using official zone shapefiles
  - Zonal bounding box distribution for pickups
  - Corridor-aware spherical projection for dropoffs
- Result: 720 labeled driver–rider pairs (7–10 AM commute window)
- Label split: 45% accepted / 55% rejected

**Right side — image:**
📎 **Attach:** `report/figures/feature_distributions.png`
Caption below image: *"Accepted pairs (green): lower detour, higher overlap — labeling produces realistic patterns"*

---

### SLIDE 4 — The 3-Stage Pipeline

**Layout:** Three horizontal boxes with arrows, full width. Justification text below each box.

**Headline:** Simulate → Predict → Optimize

**Box 1 — SIMULATE (left box, teal border):**
- BallTree spatial index
- 5-min temporal batches
- 9 engineered features per pair
- *Why BallTree?* O(log N) vs O(N²) brute force

**Arrow →**

**Box 2 — PREDICT (center box, orange border):**
- XGBRegressor → detour distance (km)
- XGBClassifier → acceptance probability (0–1)
- Combined rank score
- *Why XGBoost?* Tabular data; outperforms neural nets (Grinsztajn 2022)

**Arrow →**

**Box 3 — OPTIMIZE (right box, teal border):**
- Bipartite graph (drivers ↔ riders)
- Max-weight matching
- Globally optimal 1:1 assignments
- *Why at inference only?* Trains on full distribution, not just winners

**Bottom citation bar:**
*"Follows the Learning-Augmented Matching paradigm — Bjorck et al., AAAI 2021"*

**Image:** None — all text boxes, draw in slide.

---

### SLIDE 5 — Model Results

**Layout:** Left table + key stats (55%) + Right ROC curve image (45%)

**Headline:** XGBoost ranks matches. Rule-based can't.

**Left — Comparison Table:**

| Model | Accuracy | F1 | ROC-AUC |
|---|---|---|---|
| Rule-Based | 93.3% | 92.9% | — |
| Logistic Regression | 90.0% | 89.9% | — |
| **XGBoost (tuned)** | **94.0%** | **94.7%** | **0.971** |

Highlight the XGBoost row in teal/orange.

**Below table — 2 callout stat boxes:**
- 📊 5-Fold CV mean: **94.5%** · Best params: n_estimators=50, max_depth=3, lr=0.05
- 🔍 Regression: MAE = **2.39 km** · RMSE = **3.97 km**

**Key insight text (italic, small):**
*"Rule-based outputs binary 0/1. XGBoost outputs a probability. The bipartite optimizer needs that continuous score."*

**Right side — image:**
📎 **Attach:** `figures/roc_curve.png`
Caption: *"ROC-AUC = 0.971"*

---

### SLIDE 6 — Feature Importance

**Layout:** Left image (50%) + Right bullets (50%)

**Headline:** What actually drives acceptance?

**Left side — image:**
📎 **Attach:** `figures/feature_importance.png`
Caption: *"XGBoost feature importance by gain (classifier)"*

**Right side — bullets:**
- **time_diff_mins** — top feature; temporal compatibility is #1 acceptance factor
- **driver_orig_dist** — detour tolerance scales with trip length
- **fare_ratio** — economic incentive (rider fare / driver fare)
- **shareability_count** — corridor density proxy (Santi et al., PNAS 2014)

**Note on ablation:** Dataset size (720 pairs) is too small for reliable per-feature ablation sensitivity — feature importance by gain (shown left) is the robust measure here.

**Callout box (highlight box, bottom right):**
*"Why logistic regression fails: it can't learn that detour + fare interact non-linearly. XGBoost splits on both simultaneously."*

---

### SLIDE 7 — System-Level Results

**Layout:** Left stats panel (50%) + Right trade-off curve (50%)

**Headline:** Real-world impact of the matching system

**Left — 4 large stat boxes (big numbers, bold):**

```
Match Rate          94.6%
Avg Driver Earnings +$4.76 / ride
Avg Rider Savings   -$4.76 / ride
CO₂ Saved           ~2.5 kg / match
```

**Below stats — 1 bullet:**
- Bipartite optimizer selects globally optimal 1:1 assignments from 112 test drivers

**Right side — image:**
📎 **Attach:** `figures/system_tradeoff_curve.png`
Caption: *"Higher score threshold = lower detour, lower match rate"*

---

### SLIDE 8 — Limitations + Conclusion

**Layout:** Left contributions (50%) + Right limitations (50%)

**Headline:** What we built — and where it breaks

**Left — 3 Contributions (numbered, teal accent):**
1. **Synthetic P2P pipeline** — corridor-aware GPS synthesis from public taxi records
2. **Dual-objective XGBoost** — regression (detour km) + classification (accept prob) → unified rank score
3. **Learning-augmented bipartite matching** — ML scores as edge weights, globally optimal assignments

**Right — Limitations (honest, italic style):**
- ⚠️ Labels are synthetic — simulated, not real human decisions
- ⚠️ Geodesic ≠ road distance — river crossings/bridges ignored
- ⚠️ Dev dataset: 720 pairs (5% sample) — production runs 10K+
- ⚠️ Validated on NYC only — nationwide generalization is theoretical

**Future Work (small text, bottom right):**
Road-network routing (OSRM) · Employer subsidies · 3-tier nationwide config

**Footer bar (gradient):**
`github.com/PEM-Instruct/final-project-team-tle`

**Image:** None.

---

## IMAGE PLACEMENT SUMMARY

| Slide | Image File to Attach | Position | Size |
|---|---|---|---|
| 3 | `report/figures/feature_distributions.png` | Right half | 45% width |
| 5 | `figures/roc_curve.png` | Right half | 45% width |
| 6 | `figures/feature_importance.png` | Left half | 50% width |
| 7 | `figures/system_tradeoff_curve.png` | Right half | 50% width |

All other slides: no images, text/diagram only.

---

## TIMING GUIDE (5:05 total — within 4:30–5:30 window)

| Slide | Topic | Time |
|---|---|---|
| 1 | Title | 0:10 |
| 2 | Problem | 0:40 |
| 3 | Data | 0:40 |
| 4 | Pipeline + design choices | 0:55 |
| 5 | Model results | 0:50 |
| 6 | Feature importance | 0:35 |
| 7 | System results | 0:40 |
| 8 | Limitations + conclusion | 0:35 |
| **Total** | | **~5:05** |

---

## RUBRIC COVERAGE CHECK

| Rubric Criterion | Where Covered |
|---|---|
| Problem crisp within 60 sec | Slide 2 — 1.08 passengers stat + driver/rider diagram |
| Technical approach with design justifications | Slide 4 — WHY BallTree, WHY XGBoost, WHY inference-only bipartite |
| Metrics + comparison + **limitations acknowledged** | Slides 5, 7 (metrics/comparison) + Slide 8 (limitations) |
| Good timing 4:30–5:30 | ~5:05 total |
| Q&A depth | See Q&A prep sheet (separate) |
