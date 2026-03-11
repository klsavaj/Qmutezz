# Submission Checklist

Use this checklist to make sure you have everything before each submission. Check off items as you complete them.

---

## Group Formation + Updated Proposal (Due 3/17) — 5%

- [ ] All group members listed in README.md with roles
- [ ] Overleaf project created and linked to this repo
- [ ] Updated proposal includes:
  - [ ] Project title
  - [ ] Problem statement and motivation
  - [ ] Dataset description
  - [ ] Baseline model idea
  - [ ] More advanced model idea
  - [ ] Evaluation metrics
  - [ ] Timeline for remaining weeks
  - [ ] Areas of uncertainty / where you need help
  - [ ] Roles and communication plan
- [ ] Proposal is ≤ 2 pages, submitted as PDF
- [ ] Tagged: `v1-group-proposal`

---

## Update 1: Literature Review (Due 3/29) — 5%

- [ ] Introduction / related work section drafted in `report/main.tex`
  - [ ] Clear problem statement using formal language (inputs, outputs)
  - [ ] Motivation: why does this problem matter?
  - [ ] Survey of related work (aim for 8–15 references)
  - [ ] How your approach differs from or builds on prior work
- [ ] References added to `references.bib`
- [ ] PDF compiled and submitted on Canvas
- [ ] Tagged: `v2-lit-review`

---

## Update 2: Data & Methodology (Due 4/5) — 5%

- [ ] Dataset section drafted in report
  - [ ] Formal definition of input and output data
  - [ ] Distribution, size, and missingness details
  - [ ] Preprocessing steps described
  - [ ] Exploratory data analysis (figures/tables as appropriate)
- [ ] Methodology section drafted in report
  - [ ] Evaluation metrics defined and motivated
  - [ ] Model descriptions with relevant math
  - [ ] At least one scikit-learn baseline identified
  - [ ] At least one more complex model identified
  - [ ] Training and validation procedure described
- [ ] Data preprocessing code in `src/`
- [ ] PDF compiled and submitted on Canvas
- [ ] Tagged: `v3-data-methods`

---

## Update 3: Baseline Results (Due 4/12) — 5%

- [ ] Results section started in report
  - [ ] Baseline model trained and evaluated
  - [ ] Results reported using your defined metrics
  - [ ] Initial comparison or analysis
- [ ] Baseline model code in `src/`
- [ ] PDF compiled and submitted on Canvas
- [ ] Tagged: `v4-baseline`

---

## Final Presentation (Due 4/19 recorded / 4/22 live) — 30%

- [ ] Slides in `presentation/`
- [ ] 5-minute presentation (4:30–5:30 if recorded)
- [ ] Covers: problem, data, methods, results, conclusions
- [ ] If recorded: video posted to Canvas discussion forum
- [ ] Tagged: `v5-presentation`

---

## Q&A and Discussion Participation — 5%

- [ ] Commented on at least one recorded presentation
- [ ] Asked at least one question during live Q&A

---

## Final Code + Report (Due 4/22) — 40% (10% code + 30% report)

### Code (10%)
- [ ] All code in `src/` is well-organized and documented
- [ ] README includes reproduction instructions
- [ ] `requirements.txt` or equivalent included
- [ ] Code runs end-to-end (data → preprocessing → training → evaluation)

### Report (30%)
- [ ] ICML 2026 format, written in LaTeX
- [ ] Contains all required sections:
  - [ ] Introduction with problem definition and motivation
  - [ ] Related work / literature review
  - [ ] Dataset description (distribution, size, preprocessing)
  - [ ] Evaluation metrics (defined and motivated)
  - [ ] Model descriptions with mathematical formulations
  - [ ] Training and validation procedure (incl. hyperparameter tuning)
  - [ ] Results and analysis
  - [ ] Discussion of pitfalls, ethical considerations, and limitations
- [ ] At least one simple baseline (scikit-learn)
- [ ] At least one complex model (deep learning, ensembles, transfer learning, etc.)
- [ ] Figures and tables are clear and well-labeled
- [ ] References are complete and properly formatted
- [ ] PDF compiled and submitted on Canvas
- [ ] Tagged: `v6-final`
