import csv
import sys

def load(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            data = [row for row in csv_reader]
        print(f"Loading dataset of dimensions : ({len(data) - 1},  {len(data[0])})")
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: Input/output error with the file '{file_path}'.")
    except UnicodeDecodeError:
        print(f"Error: Unable to decode the file '{file_path}'. Check the encoding.")
    except csv.Error as e:
        print(f"Error: CSV format issue in the file '{file_path}'. Details: {e}")
    return None

