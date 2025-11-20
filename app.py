from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__, 
            template_folder="templates",
            static_folder="static")

# ---------------------------
# LOAD DATASET FROM data/
# ---------------------------
DATA_PATH = os.path.join("data", "dataset.csv")
df = pd.read_csv(DATA_PATH)

df = pd.read_csv('data/dataset.csv')

# CLEAN DATA HERE (IMPORTANT)
df = df.drop_duplicates(subset=['track_name', 'artists']).reset_index(drop=True)

# ---------------------------
# CATEGORY MAPPING (FEATURE ENGINEERED)
# ---------------------------
def get_category(row):
    tempo = row["tempo"]
    energy = row["energy"]
    valence = row["valence"]
    dance = row["danceability"]

    if tempo < 90 and energy < 0.4 and valence < 0.4:
        return "Sad/soft"
    elif energy < 0.5 and valence > 0.5:
        return "Chill/Lo-Fi"
    elif energy > 0.75 or tempo > 130:
        return "High-energy gym track"
    elif valence > 0.6 and dance > 0.6:
        return "Party/Dance track"
    elif valence > 0.4 and 0.4 < energy < 0.6:
        return "Romantic"
    else:
        return "Chill/Lo-Fi"

df["mood_category"] = df.apply(get_category, axis=1)

# ---------------------------
# MOOD DESCRIPTIONS
# ---------------------------
mood_descriptions = {
    "Chill/Lo-Fi": "Relaxing, mellow tracks for focus, studying, or unwinding.",
    "Sad/soft": "Emotional, calming songs with slow tempo and soft feel.",
    "Romantic": "Warm, melodic songs with mid-energy and positive vibes.",
    "High-energy gym track": "Fast, loud, motivational tracks for workouts.",
    "Party/Dance track": "High-danceability beats perfect for parties and dancing."
}

# ---------------------------
# HOME PAGE
# ---------------------------
@app.route("/")
def home():
    return render_template("index.html", is_category_page=False)

# ---------------------------
# CATEGORY BUTTON LOGIC (20 songs)
# ---------------------------
@app.route("/mood/<path:category>")

def mood(category):
    filtered = df[df["mood_category"] == category].head(20)

    songs = filtered[["track_name", "artists", "album_name", "popularity"]].to_dict(orient="records")

    return render_template(
        "index.html",
        songs=songs,
        selected_category=category,
        description=mood_descriptions[category],
        is_category_page=True
    )

# ---------------------------
# DROPDOWN MOOD PREDICTION (7 songs)
# ---------------------------
@app.route("/predict", methods=["POST"])
def predict():
    category = request.form["mood_input"]

    filtered = df[df["mood_category"] == category].sort_values(by="popularity", ascending=False).head(7)

    songs = filtered[["track_name", "artists", "album_name", "popularity"]].to_dict(orient="records")

    return render_template(
        "index.html",
        songs=songs,
        selected_category=category,
        description=mood_descriptions[category],
        is_category_page=False
    )

# ---------------------------
# RUN APP
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
