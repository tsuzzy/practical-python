# fileparse.py
#
# Exercise 3.17
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=None, silence_error=False, isFile=False):
    '''
    Parse lines into a list of records
    While isFile=True, parse a csv file
    '''
    if isFile: # Check if the input object is a filename
        lines = open(lines, 'rt')

    if delimiter:
        rows = csv.reader(lines, delimiter=' ')
    else:
        rows = csv.reader(lines)
    records = []

    if select and not has_headers:
        raise RuntimeError('Select argument requires column headers')

    if has_headers:
        headers = next(rows)
    
    if select: # If a column selector was given, find indices of the specified columns.
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []
    
    for rowno,row in enumerate(rows, start=1):
        if not row:  # Skip rows without data
            continue
        
        if types: # Map each element in row with a data type in the list "types"
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if silence_error:
                    pass
                else:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue # skip this error row
        
        if has_headers: # With headers, making a dictionary for records
            if indices: # Filter the row if specific columns were selected
                row = [ row[index] for index in indices ]
            record = dict(zip(headers,row))
        else: # Without headers, using tuples as substitute
            record = [item for item in row]
            record = tuple(record)
        
        records.append(record)

    if isFile: # Close the opened file
        lines.close()

    return records