import csv

def read_csv(file_path):
    try:
        with open(file_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        raise RuntimeError("CSV file not found")

    except Exception as error:
        raise RuntimeError(f"Failed to read CSV: {error}")

