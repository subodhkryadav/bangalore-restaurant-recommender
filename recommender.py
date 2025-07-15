import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data (top 2100 rows for performance)
df = pd.read_csv("load and clean data/cleaned_data.csv").head(2100)

# Combine name and cuisines (fillna for safety)
df['combined'] = df['name'].fillna('') + ' ' + df['cuisines'].fillna('')

# Vectorize
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Index with lowercase and stripped names
indices = pd.Series(df.index, index=df['name'].str.lower().str.strip()).drop_duplicates()

# Recommend function
def recommend_restaurant(name):
    name = name.lower().strip()

    if name not in indices:
        return "Restaurant not found in database."

    idx = indices[name]

    # Flatten the similarity vector
    sim_scores = list(enumerate(cosine_sim[idx].flatten()))

    # Sort by score and skip self (idx)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Slice only as many as exist (max 10)
    top_matches = sim_scores[1:min(len(sim_scores), 11)]

    # Safely get restaurant indices
    restaurant_indices = [i[0] for i in top_matches if i[0] < len(df)]

    # Return results
    return df.iloc[restaurant_indices][['name', 'location', 'rate', 'cost']].reset_index(drop=True)
