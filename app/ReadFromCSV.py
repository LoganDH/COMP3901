import csv
from os.path import join, dirname, realpath

def process_file():
    data = []
    DATASETS_PATH = join(dirname(realpath(__file__)), 'static/datasets')
    file = open(f'{DATASETS_PATH}/deaths-in-india-satp-dfe.csv', 'r')
    for row in list(csv.reader(file, delimiter=',')):
        data.append(row[23])
    file.close()
    data = list(dict.fromkeys(data))
    ref_data=[]
    for d in data:
        ref_data.append([d])

    with open(f'{DATASETS_PATH}/military-incidents-in-india.csv', 'w', encoding='UTF-8', newline='') as file:
        writer = csv.writer(file)
        for row in ref_data:
            writer.writerow(row)

process_file()



#numOfClusters = list(clusters)[-1].split(" ")[1]