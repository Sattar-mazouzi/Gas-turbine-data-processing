import os
import numpy as np
import pandas as pd

data_path = "../Data- INST-TC2"


def rename_files(path: str):
    """
    this function renames all the txt file with their proper name
    :param path: the path of the txt data files
    :return: None
    """

    file_list = os.listdir(data_path)
    file_names = [f for f in file_list if f.lower().endswith(".txt")]

    for txt_file in file_names:
        with open(path + '/' + txt_file, 'r') as f:
            lines = f.readline().replace('\n', '')
            #   print(lines)
            new_filename = lines.split('\\')[-1].replace('.', '_')
            print(new_filename)
        os.rename(path + '/' + txt_file, path + '/' + new_filename + '.txt')


def convert_to_csv(path):

    # Get a list of all files and directories in the specified path
    file_list = os.listdir(data_path)
    # Filter only the text files (ending with ".txt")
    file_names = [f for f in file_list if f.lower().endswith(".txt")]
    for file_name in file_names:
        with open(path + '/' + file_name, 'r') as f:
            lines = f.readlines()

        with open(path + '/' + file_name, 'w') as f:
            head = lines[3].replace('\t', ',')
            f.write(head)
            for line in lines[4:]:
                m_line = line.replace('\t', ',').replace(' ', ',')
                f.write(m_line)
        with open(data_path + '/' + file_name, 'r') as f:
            m_lines = f.readlines()
        #
        with open(path + '/' + file_name[:-4] + '.csv', 'w') as csvfile:
            csvfile.writelines(m_lines)


def preprocess_data(path):
    proc_path = path + '/processed_data'
    file_inpath = os.listdir(path)
    csv_files = [f for f in file_inpath if f.lower().endswith(".csv")]
    new_column_names = ["Date", "Time", "Value"]
    for csv_file in csv_files:
        new_column_names[-1] = csv_file[:-4]
        data = pd.read_csv(path + "/" + csv_file, on_bad_lines='skip')
        data = data.iloc[::-1]
        data = data.set_axis(new_column_names, axis=1)
        data.to_csv(proc_path + '/' + csv_file, index=False, header=True)

        data = data = pd.read_csv(path + "/" + csv_file, on_bad_lines='skip')


rename_files(data_path)
convert_to_csv(data_path)
preprocess_data(data_path)

#   print(line)
