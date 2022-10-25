import os
import time
import pandas as pd


# csv file name to be read in
in_csv = 'D:\\Documentos\\Cursos\\Udemy\\'
'Python\\modules_training\\rows\\teste.csv'

# get the number of lines of the csv file to be read
number_lines = sum(1 for row in (open(in_csv)))

# size of rows of data to write to the csv,

# you can change the row size according to your need
rowsize = 100


# start looping through data writing it to a new file for each set
for i in range(1, number_lines, rowsize):

    df = pd.read_csv(in_csv,
                     nrows=rowsize,  # number of rows to read at each loop
                     skiprows=range(1, i))  # skip rows that have been read
    # Subdir maker
    directory = 'output'
    parent_dir = 'D:\\Documentos\\Cursos\\Udemy'
    '\\Python\\modules_training\\rows'

    path = os.path.join(parent_dir, directory)
    # os.mkdir(path)
    # print('Diretorio criado.\n')

    time.sleep(2)

    # csv to write data to a new file with indexed name. input_1.csv etc.
    out_csv = os.path.join(path, 'NewFile' + str(i) + '.csv')

    print('Iniciando fatiador...')
    time.sleep(2)

    df.to_csv(out_csv,
              index=False,
              header=True,
              mode='a',  # append data to csv file
              chunksize=rowsize)  # size of data to append for each loop
