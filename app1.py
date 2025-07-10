import streamlit as st

st.set_page_config(page_title="Smart Trash Detector", layout="wide", page_icon="🗑️")

with open("styles1.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<div class='header'><h1>🗑️ Smart Trash Detector</h1><p>Revolutionizing Waste Sorting with AI</p></div>", unsafe_allow_html=True)

st.image("assets/background.jpg", use_container_width=True, caption="Trash Detection with YOLOv8")

st.markdown("### Click below to begin detecting trash using AI-powered models!")

if st.button("🚀 Get Started"):
    st.switch_page("Pages/1_Select_Model.py")
