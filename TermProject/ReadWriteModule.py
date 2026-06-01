import csv

def readFile(filename):
    records = []
    with open(f'{filename}.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            records += [row]
    return records


def write(filename, records):
    with open(f'{filename}.csv', newline = "", mode='w') as csvfile:
        csv_writer = csv.writer(csvfile)
        for record in records:
            csv_writer.writerow(record)

