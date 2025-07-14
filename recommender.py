import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("C:\\Users\\subod\\OneDrive\\Desktop\\zomato_project\\load and clean data\\cleaned_data.csv")
df['combined'] = df['name'] + ' ' + df['cuisines'].fillna('')

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

indices = pd.Series(df.index, index=df['name']).drop_duplicates()

def recommend_restaurant(name):
    if name not in indices:
        return "Restaurant not found in database."

    idx = indices[name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
    restaurant_indices = [i[0] for i in sim_scores]

    return df.iloc[restaurant_indices][['name', 'location', 'rate', 'cost']].reset_index(drop=True)
