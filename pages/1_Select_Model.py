import streamlit as st

st.set_page_config(page_title="Select Model", page_icon="🧠")

with open("styles1.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center;'>Select Detection Model</h2>", unsafe_allow_html=True)

model_choice = st.radio(
    "Choose your preferred model:",
    ["YOLOv8 Trash Detector", "Best Model (Optimized)"],
    horizontal=True
)

if st.button("Continue ➡️"):
    if model_choice == "YOLOv8 Trash Detector":
        st.session_state["model_path"] = "models/yolov8-trash-detector.pt"
    else:
        st.session_state["model_path"] = "models/best_model.pt"
    st.switch_page("pages/2_Run_Detection.py")
