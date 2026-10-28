# Bug Fixing Using Cursor AI

A developer case study demonstrating how **Cursor AI** was utilized as an intelligent pair programmer to identify, diagnose, and resolve subtle logic flaws, edge cases, and runtime exceptions in Python applications.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Tool](https://img.shields.io/badge/Cursor%20AI-Intelligent%20Debugging-6366f1.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 🐞 Overview

Modern software development often suffers from subtle runtime bugs that evade simple syntax checks:
- **Mutable default arguments** persisting state between separate instances.
- **Off-by-one errors** in pagination and slicing operations.
- **Unsafe deep object traversals** causing unexpected `KeyError` or `TypeError: 'NoneType' object is not subscriptable`.

This repository documents the diagnosis, root causes, and clean architectural fixes formulated with the assistance of Cursor AI.

---

## 🔍 Bug Scenarios & Resolutions

### 1. Mutable Default Argument Trap
- **The Issue**: In Python, default arguments are instantiated once when the function is parsed, not per invocation. Passing a mutable list (`items=[]`) causes all object instances to share the exact same list in memory.
- **Cursor AI Solution**: Replaced the default parameter with `items: Optional[List[str]] = None` sentinel pattern and initialized fresh list copies (`list(items) if items is not None else []`).

### 2. Off-By-One In Pagination Slicing
- **The Issue**: A naive `(page - 1) * per_page + 1` formula skipped index 0, dropping the first item on every dataset.
- **Cursor AI Solution**: Applied correct 0-indexed slice mathematics, clamped page boundaries, and calculated full metadata (`has_next`, `has_prev`, `total_pages`).

### 3. Deep JSON / Dictionary Parsing Flaws
- **The Issue**: Direct chained subscripting (`payload["data"]["user"]["profile"]`) throws unhandled exceptions if any intermediate key is null or missing.
- **Cursor AI Solution**: Implemented a recursive `safe_get` helper that traverses nested dictionaries safely without raising runtime exceptions.

---

## 🚀 Running the Diagnostics Demo

Run the interactive diagnostics script to see the failure modes and the verified fixes:

```bash
python diagnostics_runner.py
```

---

## 🧪 Automated Unit Tests

```bash
python -m unittest discover -s tests
```

---

## 📂 Project Structure

```text
bug-fixing-using-cursor-ai/
├── bug_cases/
│   ├── mutable_default/
│   │   ├── buggy_cart.py
│   │   └── fixed_cart.py
│   ├── pagination/
│   │   ├── buggy_paginator.py
│   │   └── fixed_paginator.py
│   └── json_parser/
│       ├── buggy_parser.py
│       └── fixed_parser.py
├── diagnostics_runner.py
├── tests/
│   └── test_bugs_and_fixes.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 👤 Author
**Neev Rupareliya**  
- B.Tech CSE Student, JECRC University  
- GitHub: [@Neev2850](https://github.com/Neev2850)  
- Portfolio: [personal-portfolio-mu-eosin-58.vercel.app](https://personal-portfolio-mu-eosin-58.vercel.app)
