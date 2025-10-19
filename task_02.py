from pathlib import Path

def get_cats_info(path):
    """Return list of dictionaries describing each cat's info."""

    path = Path(path)

    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as lines:
            lines = lines.readlines()
            for line in lines:
                line = line.strip().split(',')

                if len(line) != 3 or '' in line:
                    print('Cat data is not full')
                elif any(cat['id'] == line[0] for cat in cats_info):
                    print('Duplicate cat info')
                else:
                    cats_info.append({'id':line[0], 'name': line[1], 'age': line[2]})

            if not cats_info:
                print('Cats data set is empty')
            return cats_info

    except FileNotFoundError:
        print('File not found')

    except PermissionError:
        print('Access denied')

    except IsADirectoryError:
        print('This is not a file, but a directory')

    except UnicodeDecodeError:
        print('Encoding error: the file cannot be decoded with utf-8')

    return cats_info
