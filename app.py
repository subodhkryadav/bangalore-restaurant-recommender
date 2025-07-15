import os
from flask import Flask, render_template, request
from recommender import recommend_restaurant

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    name = request.form['restaurant']
    recommendations = recommend_restaurant(name)
    if isinstance(recommendations, str):
        return render_template('result.html', name=name, recommendations=[], error=recommendations)
    return render_template('result.html', name=name, recommendations=recommendations, error=None)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
