# CCSFEN1L-LAB-TeamErinyes

Centralized team repository for CCSFEN1L (Software Engineering Laboratory)
covering the full term.

## Laboratory Information

- **Course:** CCSFEN1L, Software Engineering Laboratory
- **Academic Year:** 2026-2027
- **Term:** 2nd Term
- **Team:** Team Erinyes

## Team Members

| Name | GitHub Username | Role |
|---|---|---|
| Munar, Franchesca Cassandra C. | Chiska260 | Project Leader & Environment Testing |
| Cinco, Raju Miguel | raj-student-dev | Documentation & Environment Testing |
| Asidao, Justin Aquiles | justinasidao | Quality Assurance |
| <Member 4 name> | <github-username> | <role> |

## Repository Overview

This repository contains our team's laboratory activities, documentation,
environment checks, and outputs for Software Engineering Laboratory.
Every lab is submitted through this repository.

## Repository Structure

```text
CCSFEN1L-LAB-TeamErinyes/
├── .gitignore        # Python ignore rules
├── LICENSE           # MIT license
├── README.md         # Team information and repository rules
├── CHARTER.md        # Team charter (Lecture Lesson 1)
├── TOPIC_BANK.md     # Running list of thesis ideas, one entry per lab
├── docs/             # Proposal drafts and diagrams
└── labs/             # One folder per lab
    ├── lab01/        # Lab 01: environment check
    │   ├── env_check.py
    │   ├── <surname>_colab_cpu.png
    │   ├── <surname>_colab_gpu.png
    │   └── <surname>_local.png
    └── lab02/        # Lab 02: classical machine learning pipeline
        ├── data.csv
        ├── load_dataset.py
        ├── lab02.ipynb
        └── REPORT.md
```

Later labs go in `labs/lab03/`, `labs/lab04/`, and so on.

## Collaboration Rules

1. Never push directly to `main`. It is protected.
2. Create a separate branch for each task.
3. Submit changes through Pull Requests (PRs).
4. Every PR needs at least one approving review from a teammate.
5. You cannot approve or merge your own PR.
6. Use descriptive commit messages.
7. Keep files organized in their appropriate folders.
8. Delete the branch after it is merged.

## Branch Naming

Format: `category/what-change-in-structure`

| Category | Use for | Example |
|---|---|---|
| `setup/` | Repository structure and setup | `setup/add-repository-structure` |
| `lab/` | Adding lab folders and files | `lab/add-lab02-folder` |
| `docs/` | README, reports, topic bank | `docs/add-lab02-report` |
| `fix/` | Corrections | `fix/readme-typo` |

Use lowercase and `-` between words. Branch names must not contain spaces.

## Commit Message Examples

- `Add Raju to team list`
- `Add env_check.py to labs/lab01`
- `Add dataset loading script for Lab 02`
- `Add Lab 02 notebook`
- `Add five ideas to TOPIC_BANK.md`

## Workflow

```bash
git switch main
git pull
git switch -c <category>/<what-change>
# make your changes
git add <files>
git commit -m "Describe what you changed"
git push -u origin <category>/<what-change>
```

Then open a Pull Request on GitHub, ask a teammate to review and approve it,
merge it, and delete the branch.

## Pull Request Checklist

- [ ] The branch was created from an up-to-date `main`
- [ ] The title and description explain the change
- [ ] Files are in the correct folder
- [ ] A teammate other than the author has approved it

## Lab 01 Deliverables

- [x] Repository with protected `main`
- [x] At least four merged PRs, one per member
- [x] Environment check screenshots (Colab CPU, Colab GPU, local) in `labs/lab01/`
- [ ] `TOPIC_BANK.md` with at least five ideas

**Screenshot naming:** use your surname in lowercase, for example
`macam_colab_cpu.png`, `macam_colab_gpu.png`, `macam_local.png`.

## Lab 02 Deliverables

- [x] `labs/lab02/load_dataset.py` (UCI dataset id 697)
- [x] `labs/lab02/lab02.ipynb` runs top to bottom
- [x] `labs/lab02/REPORT.md` with Table 2.1, Task 6 answers
- [ ] Machine learning entry in `TOPIC_BANK.md`

## Running the Lab 02 Code

```bash
pip install ucimlrepo pandas matplotlib scikit-learn
python labs/lab02/load_dataset.py
```

## Submission

- **Repository:** https://github.com/<owner>/CCSFEN1L-LAB-TeamErinyes
- **Tag:** `lab01-final`

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).