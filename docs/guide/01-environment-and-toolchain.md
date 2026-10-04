# Module 01: Environment Setup & Toolchain Guide

## 1. Why Python Requires a Virtual Environment (`venv`)

By default, executing `pip install <package>` installs libraries globally in the host operating system. This introduces two major risks in professional software engineering:

1. **Dependency Hell / Version Conflicts:** Project A might require `pydantic v1.10`, while Project B depends on `pydantic v2.8`. Overwriting global packages breaks unrelated projects.
2. **Lack of Reproducibility:** Global installations prevent you from determining the exact minimal dependencies required to run your specific application in cloud or container environments.

A virtual environment (`.venv`) creates an isolated, self-contained directory tree containing its own Python binaries, pip installer, and installed site-packages.

---

## 2. Standard Setup Procedures (Step-by-Step)

### Step 1: Verify Python Runtime

Ensure you are using a modern, supported runtime:

```bash
python --version
# Expected: Python 3.12+ (or 3.13+)
```
