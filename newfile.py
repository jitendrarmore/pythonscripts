

import csv

def sorted_fuction(input_file, output_file, sort_colum, delimiter):
    with open(input_file, "r") as infile, open(output_file, 'w') as outfile:
        reader = csv.reader(infile, delimiter=delimiter)
        header = next(reader)
        sort_colum_data = sorted(reader, key=lambda row: row[sort_colum])


        writer = csv.writer(outfile, delimiter="\n")
        writer.writerow(header)
        writer.writerow(sort_colum_data)


if __name__=="__main__":
    input_file = 'input.csv'
    output_file = 'output2.csv'
    sort_colum = 1
    delimiter = ","

    sorted_fuction(input_file, output_file, sort_colum, delimiter)

