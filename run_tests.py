import os

tests_path = os.path.join(os.sep, os.getcwd(), "src")
os.system("cd " + tests_path + " && python.exe -m unittest -v tests")