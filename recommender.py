import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load only top 2100 rows to reduce memory usage
df = pd.read_csv("load and clean data/cleaned_data.csv").head(2100)

# Fill missing values and combine name and cuisines
df['combined'] = df['name'] + ' ' + df['cuisines'].fillna('')

# TF-IDF and cosine similarity
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])

# Precompute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Create reverse index (lowercased and stripped names)
indices = pd.Series(df.index, index=df['name'].str.lower().str.strip()).drop_duplicates()

# Recommendation function
def recommend_restaurant(name):
    name = name.lower().strip()

    if name not in indices:
        return "Restaurant not found in database."

    idx = indices[name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
    restaurant_indices = [i[0] for i in sim_scores]

    return df.iloc[restaurant_indices][['name', 'location', 'rate', 'cost']].reset_index(drop=True)
