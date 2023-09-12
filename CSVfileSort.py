import csv

# fuction to sort a scv file
def sort_csv(input_file, output_file, sort_column, delimiter=","):
    with open(input_file, "r", newline='') as infile, open(output_file, 'w', newline='') as output_file:
        reader = csv.reader(infile, delimiter=delimiter)
        header = next(reader)
        sorted_data = sorted(reader, key=lambda row: row[sort_column])


        writer = csv.writer(output_file, delimiter=delimiter)
        writer.writerow(header)
        writer.writerow(sorted_data)


if __name__=="__main__":
    input_file = 'input.csv'
    output_file = 'output.csv'
    sort_column = 0

    sort_csv(input_file, output_file, sort_column)
    print(f"File '{input_file}' has been sorted by column {sort_column} and saved as '{output_file}'.")
