"""Test configuration helpers."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

for path in (PROJECT_ROOT, SRC_PATH):
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)
