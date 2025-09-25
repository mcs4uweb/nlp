import os
import sys
from pathlib import Path

sys.path.append('src')

ENV_FILE_PATH = Path(__file__).resolve().parents[2] / '.env'


def _load_env_file(path: Path) -> None:
    if not path.exists():
        return

    for line in path.read_text().splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue

        key, sep, value = stripped.partition('=')
        if not sep:
            continue

        normalized_value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key.strip(), normalized_value)


_load_env_file(ENV_FILE_PATH)
