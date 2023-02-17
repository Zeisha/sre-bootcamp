from pathlib import Path
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomlib

CFG = tomlib.loads(Path("config.toml").read_text(encoding="utf-8"))