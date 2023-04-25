import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import DBSCAN
# import mysql.connector

def cluster_data(data, eps):
    # Remove stop words and tokenize text data
    stop_words = set(stopwords.words('english'))
    tokenized_data = [nltk.word_tokenize(text.lower()) for text in data]
    tokenized_data = [[word for word in text if word not in stop_words] for text in tokenized_data]

    # Convert tokenized data into a matrix of TF-IDF features
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([' '.join(text) for text in tokenized_data])

    # Cluster data into categories using DBSCAN
    dbscan = DBSCAN(eps=eps, min_samples=2, metric='cosine')
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
            results[f'Cluster {cluster_id}'] = list(cluster_data['text'])
    return results


"""

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

"""