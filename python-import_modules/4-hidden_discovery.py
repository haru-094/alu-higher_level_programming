#!/usr/bin/python3
import importlib.util
import sys
from pathlib import Path

if __name__ == "__main__":
    mod_path = Path("hidden_4.pyc")
    sp = importlib.util.spec_from_file_location("hidden_4", mod_path)
    hidden_4 = importlib.util.module_from_spec(sp)
    sys.modules["hidden_4"] = hidden_4
    spec.loader.exec_module(hidden_4)
    names = [name for name in dir(hidden_4) if not name.startwith("__")]
    for name in sorted(names):
        print(name)
