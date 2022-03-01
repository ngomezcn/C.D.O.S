import os
tests_path = os.path.join(os.sep, os.path.realpath(__file__), "..","..", "src")
print(tests_path)
os.system("cd " + tests_path + " && python.exe -m unittest -v tests")