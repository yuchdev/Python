# AGENTS Guide for This Repository

## Big picture
- This repo is a **chaptered Python learning codebase**, not a single app/service; each top-level numbered folder (`01_native_datatypes` ... `15_testing`) is mostly independent examples.
- `README.md` is the canonical map of chapter intent and file-level examples; use it first to locate the right script before editing.
- Most scripts are designed for direct execution and demonstration output (prints, inline calls), not reusable package APIs.

## How code is structured
- Common pattern: many files expose small demo functions, then dispatch from `if __name__ == '__main__'` using `sys.argv[1]` and `locals()`/`globals()` (example: `01_native_datatypes/02-numeric-types.py`, `11_async/07-net-server.py`).
- `__doc__` is frequently used as in-file theory notes; preserve and extend this style when adding educational examples (example: `04_decorators/01-debug-print.py`).
- `15_testing/testing.py` provides core demo functions (`rle`, `sort`) consumed by nearby test/demo files.

## Developer workflows that matter
- Install deps from root:
  - `python3 -m pip install -r requirements.txt`
- Run a chapter script directly from root (or its directory), e.g.:
  - `python3 11_async/07-net-server.py square_server`
- Run unittest example (from `15_testing/` so local import `from testing import ...` resolves):
  - `python3 -m unittest 02-unittest.py`
- Run pytest property examples:
  - `python3 -m pytest 15_testing/04-property.py`

## Integration points / cross-file flows
- TCP demo flow is coupled by host/port `127.0.0.1:10001`:
  - server: `11_async/07-net-server.py` or `11_async/08-async-server.py` or `11_async/09-async-server2.py`
  - client: `11_async/06-net-client.py`
- Module/package demo flow:
  - `14_modules/02-packages.py` imports `small_package.package_file` and demonstrates lazy import via `importlib`.
- File-IO iterator demo expects relative files in `10_iterators/` (`file1.txt`, `file2.txt`) in `10_iterators/07-io.py`.

## Conventions specific to this repo
- Prefer **small, single-topic educational scripts** over large abstractions.
- Keep examples executable with minimal setup; avoid introducing framework scaffolding.
- When adding examples, follow existing naming style (`NN-topic.py`) inside the relevant chapter folder.
- Avoid breaking relative-import assumptions in chapter demos (many imports are intentionally local-directory based).
- Preserve demonstrative print-based output unless the file already uses tests/assertions.

## Agent checklist before editing
- Confirm target chapter/file intent in `README.md`.
- Verify whether the file is a standalone demo, a test module, or a helper module (`15_testing/testing.py`).
- If editing `11_async` or `10_iterators`, check related peer files that provide input/client behavior.
- Run the narrowest relevant command (single script or single test file), not full-repo test sweeps.
