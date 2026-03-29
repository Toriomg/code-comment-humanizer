# humncode

`humncode` is a CLI tool designed to transform AI-generated code comments into natural, human-like developer comments. It breaks the predictable statistical patterns of Large Language Models (LLMs) to help code pass through AI detectors and blend in with manual commits.

## Features

The tool processes code through a modular pipeline consisting of four specialized layers:

1.  **Cleaner Layer**: Strips AI-typical verbosity (e.g., "This function is responsible for..."), removes emojis, emoticons, and redundant numbered lists (e.g., "1. First, we...").
2.  **Jargon Layer**: Replaces formal terminology with industry-standard developer shorthand (e.g., `database` → `db`, `parameters` → `params`, `authentication` → `auth`).
3.  **Styler Layer**: Introduces "human noise" by randomly adjusting capitalization, removing trailing periods, and occasionally injecting developer tags like `TODO:` or `FIXME:`.
4.  **Recursive Processing**: Automatically detects code files within directories and processes them in-place.

## Supported Languages

`humncode` detects comment syntax based on file extensions:
*   **Python** (`.py`)
*   **C / C++** (`.c`, `.cpp`, `.h`, `.hpp`)
*   **JavaScript / TypeScript** (`.js`, `.jsx`, `.ts`, `.tsx`)
*   **Java** (`.java`)
*   **Rust** (`.rs`)
*   **PHP / Ruby / Go**

## Installation

### For Arch Linux / Linux

1. Clone the repository to your local machine.
2. Ensure you have `python` and `pip` installed.
3. Install the package globally for your user:

```bash
pip install --user .
```

4. Make sure `~/.local/bin` is in your `$PATH`.

## Usage

You can process a single file or an entire project directory.

**Process a single file:**
```bash
humncode main.c
```

**Process a directory (recursively):**
```bash
humncode ./src/
```

## Example Transformation

### Before (AI Generated)
```python
# 1. 🚀 This function is used to perform the configuration of the database.
def setup_connection():
    pass
```

### After (Humanized)
```python
# config the db
def setup_connection():
    pass
```

## Project Structure

```text
.
├── layers/
│   ├── cleaner.py    # Removes AI fluff and emojis
│   ├── jargon.py     # Maps formal words to dev slang
│   └── styler.py      # Adds randomness and style tweaks
├── tests/            # Pytest suite
├── main.py           # CLI entry point
└── setup.py          # Installation script
```

## Running Tests

To verify the transformation logic and ensure the regex patterns are working correctly:

```bash
python3 -m pytest -v
```

## Disclaimer

This tool is intended for stylistic formatting and educational purposes. Always ensure your code comments remain clear and useful for your team. Use responsibly in academic or professional environments.