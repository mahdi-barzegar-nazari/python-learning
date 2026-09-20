# 🐍 Python Learning & Practice

My personal Python learning journal and Quera exercise tracker. Each topic is a
Jupyter notebook that explains the idea first and then shows runnable code,
followed by a short practice script.

## Table of Contents

- [Overview](#overview)
- [Learning Path](#learning-path)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [How the Notebooks Are Written](#how-the-notebooks-are-written)
- [Quera Exercise Tracker](#quera-exercise-tracker)
- [Roadmap](#roadmap)
- [Tools](#tools)
- [License](#license)

## Overview

This repository is where I record what I learn while studying Python: the
concepts, the mistakes, and the exercises. It is meant to stay simple. There is
no framework and no package to install, only notebooks and small scripts.

## Learning Path

Work through the files in numeric order.

| # | Topic | Notebook | Practice |
| :-: | :--- | :--- | :--- |
| 01 | Hello, World | | [`01_hello_world.py`](./basics/01_hello_world.py) |
| 02 | Numbers and arithmetic | [`02_numbers.ipynb`](./basics/02_numbers.ipynb) | |
| 03 | Strings, indexing, slicing | [`03_strings.ipynb`](./basics/03_strings.ipynb) | |
| 04 | Types and string methods | [`04_str_methods.ipynb`](./basics/04_str_methods.ipynb) | [`06_exercise_string_split.py`](./basics/06_exercise_string_split.py) |
| 05 | String formatting | [`05_str_formatting.ipynb`](./basics/05_str_formatting.ipynb) | |
| 07 | Lists | [`07_lists.ipynb`](./basics/07_lists.ipynb) | [`08_list_practice.py`](./basics/08_list_practice.py) |
| 09 | Dictionaries | [`09_dictionary.ipynb`](./basics/09_dictionary.ipynb) | [`10_dict_practice.py`](./basics/10_dict_practice.py) |
| 11 | Tuples | [`11_tuples.ipynb`](./basics/11_tuples.ipynb) | [`12_tuple_practice.py`](./basics/12_tuple_practice.py) |

## Repository Structure

```text
.
├── basics/                    # notebooks and practice scripts, in learning order
├── quera-solutions/           # Quera solutions and the exercise tracker
│   ├── README.md              # tracker table and how to add a solution
│   └── _template.py           # starting point that includes a complexity section
├── requirements.txt           # what is needed to run the notebooks
├── pyproject.toml             # PEP 8 settings for the linter
└── .github/workflows/ci.yml   # checks style and runs every script and notebook
```

## Getting Started

**Prerequisites:** Python 3.10 or newer.

```bash
git clone https://github.com/mahdi-barzegar-nazari/python-learning.git
cd python-learning

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

jupyter lab                      # open a notebook from basics/
python basics/08_list_practice.py    # or run a practice script directly
```

## How the Notebooks Are Written

Every notebook follows the same shape so it is easy to review later:

1. **Learning goals** at the top.
2. A short **explanation before each code cell**, saying what is about to
   happen and why.
3. Code that runs top to bottom with *Run All*.
4. **Key takeaways** and links to the previous and next notebook.

Two conventions worth knowing:

- **Errors are shown on purpose, but safely.** Mistakes such as an
  `IndexError` or `ZeroDivisionError` are demonstrated inside `try` / `except`
  so the message is visible and the notebook still runs to the end.
- **Code follows [PEP 8](https://peps.python.org/pep-0008/)** (79 characters
  per line, four-space indents), checked by `ruff` in CI.

Practice scripts state their **approach** and **time / space complexity** in the
docstring, and list alternative solutions there instead of leaving commented-out
code behind.

## Quera Exercise Tracker

Solved [Quera](https://quera.org) problems live in
[`quera-solutions/`](./quera-solutions/). Each one records its approach and
complexity, and the table in
[`quera-solutions/README.md`](./quera-solutions/README.md) tracks progress.

## Roadmap

- [ ] Conditionals (`if` / `elif` / `else`) and booleans
- [ ] Loops (`for`, `while`) and `range`
- [ ] Functions and scope
- [ ] Sets, and reading and writing files
- [ ] Comprehensions
- [ ] First Quera solutions with complexity notes

## Tools

- **Language:** Python 3.10+
- **Notebooks:** JupyterLab
- **Style:** ruff (PEP 8 rules)
- **Editor:** Visual Studio Code
- **Version control:** Git and GitHub

## License

Distributed under the MIT License. See [`LICENSE`](./LICENSE).
