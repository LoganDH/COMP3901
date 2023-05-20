from .models import Schools as SchoolsTBL
import pandas as pd
import nltk
import csv
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import DBSCAN
from os.path import join, dirname, realpath
from os import listdir

def cluster_data(data, min_samples, distance):
    # Remove stop words and tokenize text data
    stop_words = set(stopwords.words('english'))
    tokenized_data = [nltk.word_tokenize(text.lower()) for text in data]
    tokenized_data = [[word for word in text if word not in stop_words] for text in tokenized_data]

    # Convert tokenized data into a matrix of TF-IDF features
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([' '.join(text) for text in tokenized_data])
    #print("Matrix dimension:", tfidf_matrix.shape, tfidf_matrix)

    # Cluster data into categories using DBSCAN
    dbscan = DBSCAN(eps=distance, min_samples=min_samples, metric='cosine')
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

def get_datasets_path():
    return(join(dirname(realpath(__file__)), 'static/datasets'))

def get_datasets():
    return(listdir(get_datasets_path()))

def fetch_data(file):
    data = []
    DATASETS_PATH = get_datasets_path()
    file = open(f'{DATASETS_PATH}/{file}', 'r')
    for row in list(csv.reader(file, delimiter=',')):
        data.append(row[0])
    file.close()
    return(data)

def get_schools():
    schools = SchoolsTBL.query.all()
    return(schools)
