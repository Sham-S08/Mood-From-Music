# Mood From Music 🎵
AI-powered music recommendation based on mood


## 🎶 Description

Mood From Music is a Flask web application that analyzes audio features such as:
- Tempo  
- Valence  
- Energy  
- Danceability  

Using these features, it classifies songs into multiple mood categories:

- 🎧 **Chill / Lo-Fi**  
- 😔 **Sad / Soft**  
- ❤️ **Romantic**  
- 🔥 **High Energy / Gym**  
- 🎉 **Party / Dance**

### ✨ Additional Highlights
- Shows **20 top songs** for each mood category  
- Displays **7 high-popularity tracks** when predicting via dropdown  
- Includes **autoplay background music**, with playback time remembered via JavaScript  
- Fully **responsive UI** with **rotating disc animation**


## 🛠 Tech Stack
- Python  
- Flask  
- Pandas  
- scikit-learn  
- HTML5 / CSS3 / JavaScript  
- Render (deployment)

## 📂 Project Structure

Mood_From_Music/
│── app.py
│── data/
│   └── dataset.csv
│── static/
│   ├── style.css
│   ├── scripts.js
│   └── music/bg_track.mp3
│── templates/
│   └── index.html
│── requirements.txt
