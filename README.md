[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/4CHMIixr)
# CS6140 Final Project

**Team Members:** *(fill in after group formation)*

| Name | Role(s) |
|------|---------|
|      |         |
|      |         |
|      |         |

## Project Title

*(Replace with your project title)*

## Quick Links

- **Overleaf Project:** *(paste link here after setup)*
- **Dataset Source:** *(paste link here)*

## Repository Structure

```
├── report/            # LaTeX source for the final report (synced with Overleaf)
│   ├── main.tex       # Main paper file (ICML 2026 format)
│   ├── references.bib # Bibliography
│   └── figures/       # Figures used in the report
├── src/               # All project code
├── data/              # Data files (git-ignored — see instructions below)
└── presentation/      # Slides for final presentation
```

## Getting Started

### 1. Set Up Overleaf (one team member)

One team member should connect this repo to Overleaf for collaborative writing:

1. Go to [Overleaf](https://www.overleaf.com) and log in with your `@northeastern.edu` email (this gives you free Professional features via NEU's institutional license)
2. Click **New Project → Import from GitHub**
3. Select this repository from the list
4. Share the Overleaf project with your teammates using the **Share** button

**Important:** Before importing, download the [ICML 2026 style files](https://media.icml.cc/Conferences/ICML2026/Styles/icml2026.zip), extract the contents, and commit `icml2026.sty` and `fancyhdr.sty` into the `report/` directory. Then push to GitHub before importing into Overleaf.

### 2. Overleaf ↔ GitHub Sync

Sync is **not automatic**. To sync:

- **Overleaf → GitHub:** In Overleaf, go to the left sidebar → **Integrations** → **GitHub** → **Push Overleaf changes to GitHub**
- **GitHub → Overleaf:** Same menu → **Pull GitHub changes to Overleaf**

**Recommended workflow to avoid merge conflicts:**
- Edit the **report** in Overleaf
- Edit **code** via Git (push to GitHub)
- Sync Overleaf → GitHub before teammates pull code changes
- Pull GitHub → Overleaf if repo structure changes (e.g., new figures committed via Git)

### 3. Data Files

Data files are git-ignored by default to keep the repo lightweight. Options for sharing data with your team:

- **Small datasets (<10 MB):** Remove the relevant line from `.gitignore` and commit directly
- **Larger datasets:** Store in Google Drive or use a download script in `src/` that fetches the data. Document the source and any preprocessing steps in your report.
- **Public datasets:** Include a download script or instructions in this README

### 4. Code

Organize your code however makes sense for your project. A reasonable starting point:

```
src/
├── data_preprocessing.py    # or a notebook
├── baseline_model.py
├── advanced_model.py
├── evaluation.py
└── utils.py
```

Use a `requirements.txt` or `pyproject.toml` to track dependencies so your work is reproducible.

## Submissions

Each submission is marked with a **Git tag**. To tag a submission:

```bash
git tag v1-group-proposal
git push origin v1-group-proposal
```

Then submit the tag name and a compiled PDF of the report (if applicable) on Canvas.

| Deliverable | Due Date | Tag Name | Canvas Link |
|------------|----------|----------|-------------|
| Group Formation + Updated Proposal | 3/17 | `v1-group-proposal` | [Submit](https://northeastern.instructure.com/courses/246158/assignments/3109556) |
| Update 1: Literature Review | 3/29 | `v2-lit-review` | [Submit](https://northeastern.instructure.com/courses/246158/assignments/3109560) |
| Update 2: Data & Formal Definitions | 4/5 | `v3-data-methods` | [Submit](https://northeastern.instructure.com/courses/246158/assignments/3109561) |
| Update 3: Baseline Results | 4/12 | `v4-baseline` | [Submit](https://northeastern.instructure.com/courses/246158/assignments/3109562) |
| Final Presentation (recorded) | 4/19 | `v5-presentation` | [Submit](https://northeastern.instructure.com/courses/246158/assignments/3109564) |
| Final Presentation (live) | 4/22 | `v5-presentation` | [Submit](https://northeastern.instructure.com/courses/246158/assignments/3109566) |
| Final Written Report | 4/22 | `v6-final` | [Submit](https://northeastern.instructure.com/courses/246158/assignments/3109565) |

## How to Reproduce Our Results

*(Fill this in before final submission. Include steps to set up the environment, download data, and run the code.)*

```bash
# Example
pip install -r requirements.txt
python src/data_preprocessing.py
python src/baseline_model.py
python src/advanced_model.py
python src/evaluation.py
```
