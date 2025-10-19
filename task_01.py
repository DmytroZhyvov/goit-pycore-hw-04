from pathlib import Path

def total_salary(path):
    """Return total and average salary of employees from the given file"""

    path = Path(path)

    total = 0
    average = 0
    employees = 0

    try:
        with open(path, 'r', encoding='utf-8') as lines:
            lines = lines.readlines()
            for line in lines:
                line = line.strip().split(',')

                if len(line) == 2:
                    try:
                        total += float(line[1])
                        employees += 1
                    except ValueError:
                        print('Employee data is not correct')
                else:
                    print('Employee data is not full')

            if employees > 0:
                average = round((total / employees), 2)
            else:
                print('Employee data set is empty')

    except FileNotFoundError:
        print('File not found')

    except PermissionError:
        print('Access denied')

    except IsADirectoryError:
        print('This is not a file, but a directory')

    except UnicodeDecodeError:
        print('Encoding error: the file cannot be decoded with utf-8')

    return (total, average)

