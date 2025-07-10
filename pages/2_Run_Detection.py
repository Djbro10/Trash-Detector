import streamlit as st
import cv2
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(page_title="Run Detection", page_icon="📷")

with open("styles1.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center;'>Trash Detection Interface</h2>", unsafe_allow_html=True)

model_path = st.session_state.get("model_path", "models/yolov8-trash-detector.pt")
model = YOLO(model_path)

tab1, tab2 = st.tabs(["📤 Upload Image", "📹 Use Webcam"])

def detect_image(img_array):
    results = model(img_array)
    annotated_img = results[0].plot()
    return annotated_img

with tab1:
    uploaded_file = st.file_uploader("Upload an image of trash", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)
        result = detect_image(np.array(image))
        st.image(result, caption="Detection Result")

with tab2:
    run = st.checkbox("Start Webcam Detection")
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)

    while run:
        ret, frame = camera.read()
        if not ret:
            st.warning("Webcam not accessible.")
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = detect_image(frame)
        FRAME_WINDOW.image(result)
