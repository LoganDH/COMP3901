from .models import Schools as SchoolsTBL
import pandas as pd
import nltk
import csv
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import DBSCAN
from os.path import join, dirname, realpath

def cluster_data(data, distance):
    # Remove stop words and tokenize text data
    stop_words = set(stopwords.words('english'))
    tokenized_data = [nltk.word_tokenize(text.lower()) for text in data]
    tokenized_data = [[word for word in text if word not in stop_words] for text in tokenized_data]

    # Convert tokenized data into a matrix of TF-IDF features
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([' '.join(text) for text in tokenized_data])

    # Cluster data into categories using DBSCAN
    dbscan = DBSCAN(eps=distance, min_samples=4, metric='cosine')
    dbscan.fit(tfidf_matrix)

    # Assign each data entry to its corresponding cluster
    clusters = dbscan.labels_
    data_df = pd.DataFrame({'text': data, 'cluster': clusters})

    # Prepare the results
    results = {}
    for cluster_id, cluster_data in data_df.groupby('cluster'):
        if cluster_id == -1:
            results['Noise data'] = list(cluster_data['text'])
        else:
            results[f'Case {cluster_id}'] = list(cluster_data['text'])
    return(results)

def fetch_data():
    data = []
    DATASETS_PATH = join(dirname(realpath(__file__)), 'static/datasets')
    file = open(f'{DATASETS_PATH}/sentence_pairs.csv', 'r')
    for row in list(csv.reader(file, delimiter=',')):
        data.append(row[0])
    file.close()
    return(data)

def get_schools():
    schools = SchoolsTBL.query.all()
    return(schools)

'''
# import mysql.connector




with open('datasets/sentence_pairs.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)




distance = float(input('epsilon'))

    clusters = cluster_data(data=data, distance=distance)

    numOfClusters = list(clusters)[-1].split(" ")[1]

    print(f'# OF CLUSTERS: {numOfClusters}')
    return clusters




clusters = process_file()
for key, value in clusters.items():
    print(key)
    print(value)




events = ("I drive a honda and it's fast.", "I drive a range rover and its luxurious.", "I love to eat an apple.", "The weather is nice today.", "Oranges are my favourite fruit.", "Toyotas are very reliable cars.", "I did not know that grapes were used to make wine.", "I use a towel to dry off after a shower.", "The new hyundai cars are very sleek.")




# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
#   password="yourpassword",
  database="capstone"
)

# Retrieve data from MySQL database
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM sample_data")
data = [str(row[0]) for row in mycursor.fetchall()]

# Prompt the user to enter the eps parameter
eps = input("Enter the eps parameter (default is 0.5): ").strip()

if eps == "":
    eps = 0.5
else:
    eps = float(eps)

# Cluster data and print the results
results = cluster_data(data, eps=eps)
print(results)
'''