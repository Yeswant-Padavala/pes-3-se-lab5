| Code / Message |	File:Line(s) |	Explanation / Why it matters |	Severity |	Suggested fix |
|	----- |	----- |	----- |	----- |	----- |
|	W0611 Unused import logging |	cleaned_inventory_system.py:2 |	Unused imports clutter code and may hide missing usage. |	Low | Properly configure logging in the main execution block. |
| C0114 Missing module docstring |	cleaned_inventory_system.py:1 |	Module has no top-level docstring describing purpose/usage. |	Low	| Add a short module docstring at top. |
|	C0116 Missing function docstrings (many)	| multiple (8,14,22,25,31,36,41,48) |	Public functions lack docstrings describing parameters/returns. |	Low |	Add docstrings for each function. |
|	R1732 Consider using 'with' for resource-allocating operations |	cleaned_inventory_system.py:26,32 |	Files opened without context manager may not be closed on errors. |	Medium |	Use with open(file, "r", encoding="utf-8") as f: and similar for write. |
| W0702  / E722 Bare except / do not use bare 'except' |	cleaned_inventory_system.py:19 |	Bare except catches all exceptions (including KeyboardInterrupt/SystemExit) and hides bugs. |	High |	Catch specific exceptions (KeyError) or check existence before operation. |
|	W0102 Dangerous default value [] as argument |	cleaned_inventory_system.py:8 |	Mutable default argument leads to shared state across calls (logs list). |	Medium |	Use None default and create list inside: logs=None; if logs is None: logs = []. |
|	C0209 String formatting could be f-string |	cleaned_inventory_system.py:12 |	Legacy % formatting less readable. |	Low	| Use f-strings for readability. |
| W1514 Using open without explicit encoding |	cleaned_inventory_system.py:26,32 |	Not specifying encoding can lead to platform-dependent behavior. |	Low |	Specify encoding, e.g., encoding="utf-8". |
| W0603 Using global statement |	cleaned_inventory_system.py:27 |	Using global makes state management harder and reduces testability. |	Medium |	Return loaded data from load_data and assign in caller, or encapsulate state in a class. |
|	W0123 Use of eval |	cleaned_inventory_system.py:59 |	eval executes arbitrary code; security risk. |	High |	Remove eval or replace with safe alternative (avoid dynamic code). If parsing, use ast.literal_eval. |

Fixes done:<br>
● Replace except: with specific exception types.<br>
● Use f-strings for cleaner logging/output.<br>
● Implement input validation for functions that take user input.<br>
● Properly configure logging in the main execution block.<br>
● Add module and function docstrings.<br>
