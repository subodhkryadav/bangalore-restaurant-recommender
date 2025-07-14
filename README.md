# 🍽️ Zomato Restaurant Recommendation System - Bangalore

Welcome to the **Zomato Restaurant Recommendation System**, created by [Subodh Kumar Yadav](https://github.com/subodhkryadav).  
This project uses a cleaned Zomato dataset from Bangalore to recommend restaurants based on restaurant similarity using **Cosine Similarity** and **TF-IDF** techniques.

---

## 📊 Features

- Cleaned and preprocessed real-world Zomato data (Bangalore).
- Recommendation based on **restaurant name**.
- Suggests **Top 10 similar restaurants**.
- Interactive web interface using **Flask**.
- Data visualization using:
  - 📈 **Plotly**
  - 📊 **Seaborn**
  - 📉 **Matplotlib**

---

## 💡 How It Works

1. User enters the name of a restaurant.
2. Model finds the closest matches using **cosine similarity**.
3. Displays a table of top 10 similar restaurants based on:
   - Location
   - Rating
   - Cost for two

---

## 🚀 Technologies Used

- Python 🐍
- Flask 🌐
- Pandas 🧮
- NumPy
- Scikit-Learn 🤖
- Plotly / Seaborn / Matplotlib for visualization

---

## 📁 Project Structure
zomato_project/
│
├── app.py # Flask main app
├── recommender.py # Recommendation logic using cosine similarity
├── templates/
│ ├── index.html # Input form UI
│ └── result.html # Result page (top 10 recommendations)
├── load and clean data/
│ ├── cleaned_data_and_visulization.csv # Cleaned Zomato dataset
│ └── clean_csv/ # (optional) processed files
├── requirements.txt # Python dependencies
└── README.md # Project documentation




---

## 🚀 How It Works

1. User enters a restaurant name on the homepage.
2. The app uses **TF-IDF Vectorization** and **Cosine Similarity** to find the 10 most similar restaurants.
3. Output is displayed in a stylish HTML table.

---

## ⚙️ Tech Stack

- **Backend**: Python, Flask  
- **ML/Recommendation**: Scikit-learn, Pandas, NumPy  
- **Visualization (for analysis only)**: Plotly, Seaborn, Matplotlib  
- **Frontend**: HTML, Bootstrap (Jinja2 Templates)

---

## 🛠️ How to Run This App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/subodhkryadav/zomato-bangalore-recommendation.git
cd zomato-bangalore-recommendation




2. (Optional) Create a Virtual Environment

python -m venv venv
venv\Scripts\activate  # On Windows

3. Install Dependencies

pip install -r requirements.txt


4. Run the Flask App
python app.py

  Then open http://127.0.0.1:5000 in your browser.



💡 Sample Output
🎯 Input:
Enter restaurant: San Churro Cafe


📋 Output (Top 10 Similar Restaurants):
#	Restaurant Name	Location	Rating	Cost
1	On The Nose	BTM	3.8	600
2	On The Nose	BTM	3.8	600
3	On The Nose	Koramangala 5th Block	2.7	600
4	Firangi Bake	Rajarajeshwari Nagar	4.0	600
5	Firangi Bake	Banashankari	4.0	600
6	Euki	Jayanagar	4.1	900
7	Firangi Bake	Sarjapur Road	4.1	600
8	Firangi Bake	Indiranagar	3.9	600
9	Firangi Bake	Bannerghatta Road	4.0	600
10	On The Nose	Koramangala 5th Block	2.7	600

## 👨‍💻 Developer
- **Subodh Kumar Yadav**  
- 🔗 [GitHub Profile](https://github.com/subodhkryadav)  
- 🎓 B.Tech (Computer Science) — Data Science Enthusiast

## 📃 License
This project is open-source and intended for learning and demonstration purposes only.
