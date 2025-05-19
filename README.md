
# chess

[![codecov](https://codecov.io/gh/m-310101/chess/branch/main/graph/badge.svg?token=chess_token_here)](https://codecov.io/gh/m-310101/chess)
[![CI](https://github.com/m-310101/chess/actions/workflows/main.yml/badge.svg)](https://github.com/m-310101/chess/actions/workflows/main.yml)

chess by m-310101

## Install it from PyPI

```bash
pip install chess
```

## Usage

```py
from chess import BaseClass
from chess import base_function

BaseClass().base_method()
base_function()
```

```bash
$ python -m chess
#or
$ chess
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## UML Diagrams

Diagrams are auto-generated from PlantUML source files.

### How to update:
1. Ensure [PlantUML](https://plantuml.com/) has been installed
2. Edit `.puml` files in `/uml`
3. Modified files will automatically generate images via pre commit hooks, for manual generation run the script:
```bash
./scripts/generate_umls.sh
```

### Diagram Legend:
| File | Description |
|------|-------------|
| `impl_class_diagram.puml` | Core implementation perspective class relationship diagram |
