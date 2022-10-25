import csv
import os

path = 'D:\\Documentos\\Cursos\\Udemy\\Python\\modules_training\\rows\\'


def get_csv_writer(path):
    csv_file = open(path, newline="", mode="w")
    return csv.writer(csv_file), csv_file


rowsize = 100
in_csv = "teste.csv"
number_lines = sum(1 for row in (open(in_csv)))


with open(in_csv, newline="", mode="r") as foo_csv:
    reader = csv.reader(foo_csv)
    header = reader.__next__()
    filenum = 1
    csv_dir = "split_csv"
    os.mkdir(csv_dir)
    filename = f"foo{filenum}.csv"
    path = os.path.join(csv_dir, filename)
    csv_writer, csv_file = get_csv_writer(path)
    csv_writer.writerow(header)
    for i, row in enumerate(reader):
        if i % rowsize == 0 and i != 0:
            csv_file.close()
            filenum += 1
            filename = f"foo{filenum}.csv"
            path = os.path.join(csv_dir, filename)
            csv_writer, csv_file = get_csv_writer(path)
            csv_writer.writerow(header)
        csv_writer.writerow(row)
