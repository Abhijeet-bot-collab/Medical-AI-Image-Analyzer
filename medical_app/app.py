import streamlit as st
from PIL import Image
from models.bytez_qwen import run_qwen

st.set_page_config(page_title="Medical AI (Qwen)", layout="centered")

st.title("🏥 Medical Imaging Diagnosis (Qwen)")
st.caption("Educational AI analysis using Qwen (via Bytez)")

uploaded_file = st.file_uploader(
    "Upload Medical Image (JPG / PNG)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("🔍 Analyze Image"):
        with st.spinner("Analyzing with Qwen..."):
            prompt = f"""
You are a medical imaging expert.

A medical image has been uploaded.

Image info:
- File type: {uploaded_file.type}
- Resolution: {image.size[0]} x {image.size[1]}

Generate a structured medical-style report:
1. Possible imaging modality & body region
2. Typical findings that could be assessed
3. Possible abnormalities (educational)
4. Patient-friendly explanation
5. Medical disclaimer

IMPORTANT:
- This is NOT a real diagnosis
- Educational use only
"""

            response = run_qwen([
                {"role": "user", "content": prompt}
            ])

            st.markdown("### 📋 AI Analysis Result")
            st.markdown(response)
            st.caption("⚠️ AI-generated content. Consult professionals.")

else:
    st.info("👆 Upload an image to start analysis")
