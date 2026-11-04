[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/4CHMIixr)
# Incentive-Aware Multi-Objective Matching for P2P Commuter Carpooling

**CS6140 Machine Learning — Final Project**

**Author:** Krunal Savaj (solo project)

## What This Project Is About

Picture someone driving to work every morning while a person a few blocks away is heading the same way. This project tries to answer one question: **which rider should each driver pick up?**

A good match has to work for both people. The driver shouldn't go far out of their way, the ride should pay enough to be worth it, and the timing has to line up. Simple distance or time cut-offs can't balance all of that at once.

There's no public carpooling dataset, so I built one. Starting from 3.5 million real NYC Yellow Taxi trips (August 2025), I generated realistic driver–rider pairs and simulated whether each driver would accept. I then trained an XGBoost model that predicts two things for every possible pair: how much extra driving it adds, and how likely the driver is to say yes. Those two predictions become one score, and a bipartite matching step uses the scores to pair everyone up at once, so the overall assignment is as good as possible instead of first come, first served.

In the end the model beats both a rule-based approach and logistic regression, matches almost every rider, and earns drivers about $5.75 more per shared ride. The numbers are in [Key Results](#key-results) below.

## Quick Links

- **Report:** `report/main.tex` (ICML 2026 format)
- **Presentation:** `presentation/presentation.html` (Reveal.js slides)
- **Dataset Source:** [NYC TLC Yellow Taxi Trip Records (August 2025)](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- **Overleaf:** https://www.overleaf.com/read/tgthmvhmhqzb#ba2fcc

## Repository Structure

```
├── src/
│   ├── data/loader.py                  # Step 1: Downloads TLC data, synthesizes GPS coordinates
│   ├── simulation/pair_generator.py    # Step 2: Generates driver-rider pairs with stochastic labels
│   ├── models/xgb_matching.py          # Step 3: Dual-objective XGBoost (train + evaluate + figures)
│   ├── models/baselines.py             # Rule-based and logistic regression baselines
│   └── visualization/                  # Feature distribution plots
├── config/
│   ├── dev_config.yaml                 # 25% sample, 3K driver limit (used in paper)
│   └── prod_config.yaml                # Full dataset, 25K driver limit
├── data/                               # Generated data (git-ignored, created by pipeline)
├── figures/                            # Generated figures (created by pipeline)
├── report/
│   ├── main.tex                        # Final report (ICML 2026 template)
│   ├── references.bib                  # Bibliography (12 references)
│   └── figures/                        # Figures embedded in report
├── presentation/                       # Reveal.js slides + speaker notes
├── requirements.txt                    # pip dependencies
├── environment.yml                     # conda environment (recommended)
└── run_all.sh                          # One-command full pipeline
```

## How to Reproduce

### 1. Setup

```bash
conda env create -f environment.yml
conda activate qmutez
```

Or with pip:
```bash
pip install -r requirements.txt
```

### 2. Run Everything

```bash
./run_all.sh
```

This executes the full pipeline:
1. Downloads NYC TLC data (~800 MB) and synthesizes GPS coordinates
2. Generates 38,102 labeled driver-rider pairs via BallTree spatial indexing
3. Trains dual-objective XGBoost with grid search and 5-fold CV
4. Evaluates baselines (rule-based + logistic regression)
5. Generates all figures in `figures/` and copies to `report/figures/`

### Or Run Step-by-Step

```bash
PYTHONPATH=. python src/data/loader.py                              # Data download + coordinate synthesis
PYTHONPATH=. python src/simulation/pair_generator.py                # Pair generation + labeling
PYTHONPATH=. python src/models/xgb_matching.py                      # XGBoost training + evaluation
PYTHONPATH=. python src/models/baselines.py                         # Baseline evaluation
PYTHONPATH=. python src/visualization/generate_feature_distributions.py  # EDA figure
```

## Key Results

| Model | Accuracy | F1 | ROC-AUC |
|-------|----------|-----|---------|
| Rule-Based | 93.3% | 92.9% | n/a |
| Logistic Regression | 90.0% | 89.9% | n/a |
| **XGBoost (tuned)** | **94.0%** | **93.9%** | **0.982** |

System-level (bipartite matching): 98.9% match rate, +$5.75 avg driver earnings, ~3.1 kg CO₂ saved per match.

## Output Figures

| File | Description |
|------|-------------|
| `feature_distributions.png` | Feature distributions by acceptance label (EDA) |
| `feature_importance.png` | XGBoost feature importance by gain |
| `roc_curve.png` | ROC curve with AUC score |
| `ablation_study.png` | ROC-AUC drop when each feature is removed |
| `learning_curve.png` | Train vs CV accuracy across training set sizes |
| `system_tradeoff_curve.png` | Match rate vs avg driver detour across confidence thresholds |

## Git Tags

| Tag | Deliverable |
|-----|------------|
| `v1-group-proposal` | Group Formation + Proposal |
| `v2-lit-review` | Literature Review |
| `v3-data-methods` | Data & Methodology |
| `v4-baseline` | Baseline Results |
| `v5-presentation` | Final Presentation |
| `v6-final` | Final Report + Code |