import sys

file_name = 'recipes.txt'

try:
    my_file = open(file_name, 'x')
    my_file.write('Spaghetti\n')
    my_file.close()
except FileExistsError as err:
    print(f"The {file_name} file already exists.")
    sys.exit(1)
except Exception:
    print(f"Unable to write to the file")
    raise
finally:
    print("Execution completed")


