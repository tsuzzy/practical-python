# fileparse.py
#
# Exercise 3.6
import csv

def parse_csv(filename, select=None, types=None, has_headers=True):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        records = []

        if has_headers:
            headers = next(rows)
            if select: # If a column selector was given, find indices of the specified columns.
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []
        
        for row in rows:
            if not row:  # Skip rows without data
                continue
            
            if types: # Map each element in row with a data type in the list "types"
                row = [func(val) for func, val in zip(types, row)]
            
            if has_headers: # With headers, making a dictionary for records
                if indices: # Filter the row if specific columns were selected
                    row = [ row[index] for index in indices ]
                record = dict(zip(headers,row))
            else: # Without headers, using tuples as substitute
                record = [item for item in row]
                record = tuple(record)
            
            records.append(record)

    return records