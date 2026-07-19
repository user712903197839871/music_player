# contains CRUD operations on JSON files

import json

def check_filepath_validity(filepath: str, mode: str):
    try:
        with open(filepath, mode) as file:
            return file

    except FileNotFoundError:
        print(f"[ERROR] The path '{filepath}' does not exist or is invalid.")
        return None
        
    except IsADirectoryError:
        print(f"[ERROR] The path '{filepath}' points to a folder, not a file.")
        return None
        
    except PermissionError:
        print(f"[ERROR] The file exists, but we do not have the permission to read it.")
        return None
    
    except ValueError as e:
        print(f"[ERROR]: Invalid mode {mode} for opening a file")
        return None
        
    except OSError as e:
        print(f"[ERROR]: Invalid path syntax or OS error: {e}")
        return None


def read_data(path: str) -> dict:
    """
    reads json from file

    Args:
        path - path to the file (must be a valid path)

    Returns:
        a dictionary of the read json
    """

    f = check_filepath_validity(path, 'r')

    if not f:
        return {}
    else:
        return json.load(f)


def write_data(path: str, data):
    """
    OVERWRITES file with data

    Args:
        path - path of file
        data - data that will be written to file
    """

    f = check_filepath_validity(path, 'w')

    if f:
        json.dump(data, f, indent=4)
