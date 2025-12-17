# ENV
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
# IMPORTS
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import base64
from pathlib import Path
import base64
from pathlib import Path
tf.keras.mixed_precision.set_global_policy("float32")
def load_labels(label_path):
    with open(label_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

from Birds_info import BIRDS_LOOKUP
from leaves_info import LEAF_LOOKUP
import re
def normalize(text):
    """
    Makes text safe for matching:
    - lowercase
    - removes spaces, hyphens, underscores
    - removes special characters
    """
    text = text.lower().strip()
    text = re.sub(r"[^a-z]", "", text)
    return text
predicted_key = None
# PAGE CONFIG
st.set_page_config(
    page_title="AI-Powered Species Identification",
    page_icon="🌿",
    layout="centered"
)
robot_gif = Path("3.gif")
robot_bytes = robot_gif.read_bytes()
encoded_robot = base64.b64encode(robot_bytes).decode()
GIF_PATH = Path("1.gif")
gif_bytes = GIF_PATH.read_bytes()
gif_base64 = base64.b64encode(gif_bytes).decode()
# BASE DIR 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# GLOBAL CSS: FONT, DROPDOWN, UPLOADER, IMAGE, PREDICTION
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Poppins:wght@300;400;500;600&display=swap');

@import url('https://fonts.googleapis.com/css2?family=Alfa+Slab+One&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    text-align: center;
}
/* FORCE MAIN TITLE STYLE (OVERRIDE STREAMLIT) */
h1.main-title {
    white-space: nowrap; 
    font-family: 'Alfa Slab One', cursive !important;
    font-size: 40px !important;
    font-weight: 300 !important;
    letter-spacing: 1.3px !important;
    color: black !important;
    text-align: center;
    text-shadow: 0 0 18px rgba(0, 255, 100, 0.55);
}
/* Center block container */
.block-container {
    display: flex;
    flex-direction: column;
    align-items: center;
}
/* DROPDOWN */
.stSelectbox > div {
    background: rgba(0,0,0,0.85) !important;
    border-radius: 16px !important;
    padding: 6px !important;
    color: #FFD700 !important;
    width: 320px !important;
    margin: auto !important;
}
.stSelectbox label {
    font-weight: 600;
    font-size: 15px;
    color: #FFD700;
    display: block;
    text-align: center;
}
/* FILE UPLOADER */
.stFileUploader {
    background: rgba(0,0,0,0.85);
    border-radius: 18px;
    padding: 18px;
    color: #FFD700;
    width: 640px !important;
    margin: auto !important;
}
.stFileUploader label {
    font-weight: 600;
    font-size: 15px;
    color: #FFD700;
    display: block;
    text-align: center;
}
.stFileUploader button {
    background: linear-gradient(135deg, #FFD700, #FFA500);
    color: black;
    border-radius: 14px;
    font-weight: 600;
    padding: 0.5rem 1.2rem;
    border: none;
    transition: transform 0.2s ease;
    display: block;
    margin: auto;
}
.stFileUploader button:hover {
    transform: scale(1.05);
}
/* IMAGE */
.stImage > img {
    display: block;
    margin: auto;
    width: 300px !important;
    height: 300px !important;
    object-fit: cover;
}
/* PREDICTION CARD */
.prediction-card {
    background: rgba(0,0,0,0.85);
    color: #FFD700;
    padding: 12px;
    border-radius: 14px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.4);
    font-weight: 600;
    font-size: 16px;
    text-align: center;
    width: 320px;
    margin: 12px auto 0 auto;
}
/* RIGHT SIDE GIF */
.right-gif {
    position: fixed;
    right: 300px;        
    top: 320px;         
    width: 350px;       
    z-index: 3;
    pointer-events: none;
    animation: float 4s ease-in-out infinite;
}
.top-gif {
    display: block;
    margin: 10px auto 5px auto;
    width: 70px;      
    height: auto;
    z-index: 2;
}
/* subtle floating animation */
@keyframes float {
    0% { transform: translateY(0); }
    50% { transform: translateY(-12px); }
    100% { transform: translateY(0); }
}
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(12px);}
    to {opacity: 1; transform: translateY(0);}
}
.glass {
    background: rgba(0, 0, 0, 0.45);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: 16px;
    padding: 20px;
    margin-top: 20px;
    color: #ffffff;
    max-width: 650px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}
.glass h3 {
    margin-top: 0;
    color: #ffd700;
}
.glass p {
    line-height: 1.6;
    font-size: 15px;
}
            .info-card {
    background: rgba(255, 255, 255, 0.30);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 16px;
    padding: 20px;
    margin-top: 20px;
    color: #000;
    max-width: 650px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}          
</style>
""", unsafe_allow_html=True)
# BACKGROUND OVERLAY
st.markdown("""
<style>
.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.35);
    z-index: -1;
}
</style>
<div class="overlay"></div>
""", unsafe_allow_html=True)
# BACKGROUND VIDEO FUNCTION
VIDEO_PATH = Path("BG.PINK.mp4")
def set_background_video(video_path):
    if not video_path.exists():
        st.warning("Background video file not found.")
        return
    video_bytes = video_path.read_bytes()
    encoded_video = base64.b64encode(video_bytes).decode()
    st.markdown(f"""
    <style>
    video.background-video {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: -1;
    }}
    .stApp {{
        background: transparent;
    }}
    </style>
    <video class="background-video" autoplay muted loop playsinline>
        <source src="data:video/mp4;base64,{encoded_video}" type="video/mp4">
    </video>
    """, unsafe_allow_html=True)
set_background_video(VIDEO_PATH)
# TITLE
st.markdown(
    f"""
    <img src="data:image/gif;base64,{gif_base64}" class="top-gif">
    """,
    unsafe_allow_html=True
)
st.markdown(
    '<h1 class="fade-in main-title">AI-Powered Species Identification</h1>',
    unsafe_allow_html=True
)
# MODEL PATHS
birds_model, birds_labels = load_model_and_labels(
    "birds_model",
    "birds_labels.txt"
)

leaf_model, leaf_labels = load_model_and_labels(
    "leaf_model",
    "leaf_labels.txt"
)


@st.cache_resource
def load_model_and_labels(model_dir, labels_path):
    # --- Check model folder ---
    if not os.path.isdir(model_dir):
        st.error(f"Model folder not found: {model_dir}")
        return None, None

    # --- Check labels file ---
    if not os.path.isfile(labels_path):
        st.error(f"Labels file not found: {labels_path}")
        return None, None

    # --- Clear TF session (important on Streamlit Cloud) ---
    tf.keras.backend.clear_session()

    # --- Load SavedModel (NO hacks needed) ---
    model = tf.keras.models.load_model(
        model_dir,
        compile=False
    )

    # --- Load labels ---
    with open(labels_path, "r", encoding="utf-8") as f:
        labels = [line.strip() for line in f if line.strip()]

    return model, labels


# IMAGE PREPROCESS
def preprocess_image(img):
    img = img.convert("RGB").resize((224, 224))
    arr = np.array(img, dtype=np.float32) / 255.0
    return np.expand_dims(arr, axis=0)
# UI
selected_model = st.selectbox("Select AI Model", list(MODELS.keys()))
uploaded_file = st.file_uploader("Upload an image", ["jpg", "jpeg", "png"])
if uploaded_file:
    # Load model & labels
    model_path = MODELS[selected_model]["model"]
    label_path = MODELS[selected_model]["labels"]
    model, labels = load_model_and_labels(model_path, label_path)
    if model is None or labels is None:
        st.stop()
    # uploaded image
    image = Image.open(uploaded_file)
    st.image(image, use_column_width=False)
    # robot GIF
    st.markdown(
        f"""
        <img src="data:image/gif;base64,{encoded_robot}" class="right-gif">
        """,
        unsafe_allow_html=True
    )
    # Prediction
    preds = model.predict(preprocess_image(image), verbose=0)
    idx = int(np.argmax(preds))
    conf = float(preds[0][idx]) * 100
    predicted_label = labels[idx]
    predicted_key = normalize(predicted_label)
    st.markdown(f"""
    <div class="prediction-card">
        <b>Prediction:</b> {predicted_label}<br>
         <b>Confidence:</b> {conf:.2f}%
    </div>
    """, unsafe_allow_html=True)
    # Species Information
    from Birds_info import BIRDS_LOOKUP
    from leaves_info import LEAF_LOOKUP
    info = None
    if selected_model.lower().startswith("bird"):
        for key, data in BIRDS_LOOKUP.items():
            if normalize(key) == predicted_key:
                info = data
                break
    elif selected_model.lower().startswith("leaf"):
        for key, data in LEAF_LOOKUP.items():
            if normalize(key) == predicted_key:
                info = data
                break

    if info:
     st.markdown(f"""
    <div class="glass">
        <h3>{info['name']}</h3>
        <p>{info['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    else:
        st.info("No additional information available for this species.")












