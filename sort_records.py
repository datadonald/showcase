import csv
import operator

def sort_records(filename, sort_key, sort_style, delimiter=','):
    """Reads, sorts, and writes records to a CSV file.

    Args:
        filename: The name of the CSV file.
        sort_key: The field to sort by (column name or index).
        sort_style: 'ascending' or 'descending'.
        delimiter: The delimiter used in the CSV file (default: ',').
    """
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile, delimiter=delimiter)
            records = list(reader)  # Read all records into a list

            if not records:
                print("File is empty. Nothing to sort.")
                return

            if isinstance(sort_key, str): #check if sort key is a string (header)
                if sort_key not in records[0]:
                    raise ValueError(f"Sort key '{sort_key}' not found in file headers.")
            elif not isinstance(sort_key, int) or sort_key < 0 or sort_key >= len(records[0]):
                raise ValueError("Invalid sort key. Must be a valid header name or a positive integer within the number of columns.")
            
            # Convert sort key to index if it's a string (header name)
            if isinstance(sort_key, str):
                sort_key = reader.fieldnames.index(sort_key)

            # Sort the records
            reverse_order = (sort_style.lower() == 'descending')
            records.sort(key=lambda row: list(row.values())[sort_key], reverse=reverse_order)

        with open(filename, 'w', newline='', encoding='utf-8') as outfile:
            fieldnames = records[0].keys()
            writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=delimiter)
            writer.writeheader()
            writer.writerows(records)

        print(f"File '{filename}' sorted successfully by {list(fieldnames)[sort_key]} in {sort_style} order.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
    except Exception as e: #Catch any other exceptions
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    filename = input("Enter the filename: ")
    try:
        sort_key = input("Enter the sort key (header name or column index): ")
        if sort_key.isdigit():
            sort_key = int(sort_key)
    except ValueError:
        print("Invalid sort key. Please enter a valid header name or a positive integer.")
        exit()
    
    sort_style = input("Enter the sort style (ascending/descending): ")

    sort_records(filename, sort_key, sort_style)