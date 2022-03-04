from ast import arg
from operator import mod
import pytest
import os
from settings import modules, arguments

# See ./settings.py
src_path = os.path.join(os.sep, os.path.dirname(os.path.realpath(__file__)), '..', '..','src')
modules_abosulte_paths = []
for modul in modules:
    print(modul)
    modules_abosulte_paths.append(os.path.join(src_path, modul))

arguments.extend(modules_abosulte_paths)
pytest.main(arguments)