import csv
import extractor

def process_file():
    data = []

    file = open('datasets/1377882923_sentence_pairs.csv', 'r')

    for row in list(csv.reader(file, delimiter=',')):
        data.append(row[0])
        data.append(row[1])

    file.close()

    distance = float(input('epsilon'))

    clusters = extractor.cluster_data(data=data, distance=distance)

    numOfClusters = list(clusters)[-1].split(" ")[1]

    print(f'# OF CLUSTERS: {numOfClusters}')
    return clusters

clusters = process_file()
for key, value in clusters.items():
    print(key)
    print(value)

'''distance=0.30
prev_dict={}
while distance < 0.50:
    print(f'DISTANCE: {distance}')
    current_dict=process_file(distance=distance)
    distance+=0.01
    if prev_dict:
        if prev_dict.get('Noise data')==current_dict.get('Noise data'):
            print(True)
        else:
            print(False)
    prev_dict=current_dict'''