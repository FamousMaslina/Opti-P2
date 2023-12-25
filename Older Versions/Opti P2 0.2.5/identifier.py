import os
import re

def find_python_files(directory):
  """Finds all Python files in the specified directory."""
  files = os.listdir(directory)
  python_files = []
  for file in files:
    if file.endswith(".py"):
      python_files.append(os.path.join(directory, file))
  return python_files

def find_variables(file_path):
  """Finds all variables in the specified Python file."""
  variables = []
  with open(file_path, "r") as f:
    for line in f:
      match = re.search(r"(spMB)", line)
      if match:
        variables.append(match.group(1))
  return variables

def main():
  """The main function."""
  directory = os.getcwd()
  python_files = find_python_files(directory)
  for file in python_files:
    if os.path.basename(file) != "identifier.py":
      variables = find_variables(file)
      if variables:
        print(file, variables)
        cpu = os.path.basename(file)
        print(cpu)
        file_id = cpu
        with open("idcpu.py", "w") as f:
          f.write("cpu = '{}'".format(file_id))

if __name__ == "__main__":
  main()
  #exec(open('test.py').read())