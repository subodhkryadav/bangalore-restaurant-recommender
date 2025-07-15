import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load top 2100 rows (optional for performance)
df = pd.read_csv("load and clean data/cleaned_data.csv").head(2100)

# Fill missing cuisines and create 'combined' column
df['combined'] = df['name'] + ' ' + df['cuisines'].fillna('')

# TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])

# Cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Create index mapping: lowercase and strip names
indices = pd.Series(df.index, index=df['name'].str.lower().str.strip()).drop_duplicates()

# Main recommendation function
def recommend_restaurant(name):
    name = name.lower().strip()

    if name not in indices:
        return "Restaurant not found in database."

    idx = indices[name]

    # Flatten the similarity vector to avoid ambiguity
    sim_scores = list(enumerate(cosine_sim[idx].flatten()))

    # Sort by similarity score (highest to lowest)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Skip the first one (it’s the same restaurant)
    top_matches = sim_scores[1:11]

    # Get the top 10 recommended restaurant indices
    restaurant_indices = [i[0] for i in top_matches]

    return df.iloc[restaurant_indices][['name', 'location', 'rate', 'cost']].reset_index(drop=True)
