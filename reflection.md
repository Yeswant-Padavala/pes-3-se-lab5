# Lab Reflection

1) Which issues were the easiest to fix, and which were the hardest? Why?
- Easiest: dding docstrings. These are local, low-risk edits with immediate feedback from linters.
- Hardest: state- and API-level fixes (mutable default args and global state). Proper fixes require refactoring function signatures or introducing an object to encapsulate state, which impacts call sites and tests.

2) Did the static analysis tools report any false positives? If so, describe one example.
- No major false positives were encountered. One minor case: Pylint's recommendation to prefer lazy `%` formatting for logging (W1203) is conservative — using f-strings improves readability and is acceptable when logging calls are not on hot paths, so that warning can be contextually ignored.

3) How would you integrate static analysis tools into your actual software development workflow?
- Local development: enable editor plugins (pylint/flake8/bandit) and pre-commit hooks to catch issues before commits.
- CI: add a pipeline stage (GitHub Actions / GitLab CI) that runs flake8, pylint, and bandit and fails the build for high-severity issues.
- Incremental enforcement: start with warnings only, then promote to required checks; use autofix where safe (black, isort) and schedule refactors for harder issues.

4) What tangible improvements did you observe after applying the fixes?
- Readability: clearer logging and added docstrings make intent easier to follow.
- Robustness: specific exception handling prevents silent failures; input validation reduces invalid state.
- Security: removing eval removes an arbitrary-code execution risk.