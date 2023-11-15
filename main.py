import pandas as pd
from flask import Flask, jsonify

movies = pd.read_csv('movies.csv')
print(movies.head())
app = Flask(__name__)

@app.route("/")
def home():
    return "Felix estuvo aqui"

@app.route("/api/peli")
def movie_api():
    pelicula = movies.sort_values(by="title", ascending=False)
    return jsonify(pelicula.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
