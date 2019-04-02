import csv


def process_salary(csv_reader):
    """Process salary of user from csv file."""
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} salary: {row["salary"]}')
        line_count += 1
    print(f'Completed {line_count} lines.')


with open('employee.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    process_salary(csv_reader)
