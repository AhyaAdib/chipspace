# ChipSpace Repository Architecture

## Purpose

ChipSpace separates learning materials, engineering implementations, experiments, and documentation.

## Directory Responsibilities

| Directory | Responsibility |
|---|---|
| `learning/` | Theoretical concepts, derivations, exercises, and learning notes |
| `projects/` | RTL, testbenches, integration, and practical engineering implementations |
| `experiments/` | Measurements, synthesis results, timing, performance, and quantitative comparisons |
| `docs/` | Architecture documentation, competition documents, references, and engineering decisions |
| `scripts/` | Reusable simulation, setup, and automation scripts |
| `assets/` | Diagrams, images, and waveforms |
| `daily_reports/` | Records of individual learning sessions |
| `weekly_reports/` | Weekly summaries, assessment, and milestone records |


## Evidence Principle
Learning completion, implementation completion, verification status, and Git synchronization are tracked separately.
A written explanation alone does not prove that an implementation works. Verification requires appropriate evidence, such as simulation results, test reports, measurements, or other reproducible checks.

## Naming Convention
New files and directories use `snake_case` where applicable. Existing names are not changed without an explicit decision.

## Repository Management
Git workflow:
1. Write or modify files.
2. Inspect changes using `git status` and `git diff`.
3. Stage relevant files using `git add`.
4. Review staged changes using `git diff --cached`.
5. Commit logically grouped changes.
6. Push to the configured remote.
7. Verify repository synchronization.
