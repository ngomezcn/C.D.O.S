from ast import arg
import pytest
import os
from settings import modules, arguments

src_path = os.path.join(os.sep, os.path.dirname(os.path.realpath(__file__)), '..', '..','src')
modules_paths = []

for modul in modules:
    modules_paths.append(src_path + '/' + modul)

arguments.extend(modules_paths)
pytest.main(arguments)

#class MyPlugin:
#    def pytest_sessionfinish(self):
#        print("*** test run reporting finishing", end='')
#pytest.main(arguments, plugins=[MyPlugin()])
    