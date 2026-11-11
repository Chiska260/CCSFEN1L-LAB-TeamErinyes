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
    └── lab01/        # Lab 01: environment check outputs
        ├── env_check.py
        ├── <surname>_colab_cpu.png
        ├── <surname>_colab_gpu.png
        └── <surname>_local.png
```

Later labs go in `labs/lab02/`, `labs/lab03/`, and so on.

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

| Type | Pattern | Example |
|---|---|---|
| Add a member to README | `add-<name>` | `add-franchesca` |
| Lab work | `lab<NN>-<name>-<task>` | `lab01-raju-screenshots` |
| Documentation | `docs-<topic>` | `docs-charter` |
| Fix | `fix-<topic>` | `fix-readme-typo` |

Branch names must not contain spaces.

## Commit Message Examples

- `Add Raju to team list`
- `Add env_check.py to labs/lab01`
- `Add Munar environment check screenshots`
- `Add five ideas to TOPIC_BANK.md`

## Workflow

```bash
git switch main
git pull
git switch -c <branch-name>
# make your changes
git add <files>
git commit -m "Describe what you changed"
git push -u origin <branch-name>
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
- [ ] At least four merged PRs, one per member
- [ ] Environment check screenshots (Colab CPU, Colab GPU, local) in `labs/lab01/`
- [ ] `TOPIC_BANK.md` with at least five ideas

**Screenshot naming:** use your surname in lowercase, for example
`macam_colab_cpu.png`, `macam_colab_gpu.png`, `macam_local.png`.

## License

This project is licensed under the MIT License.