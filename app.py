import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile

st.title("🔥 Fire Detection System")

model = YOLO(
    "runs/detect/fire_detector/weights/best.pt"
)

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image"
    )

    if st.button("Detect Fire"):

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".jpg"
        )

        temp_file.write(
            uploaded_file.getvalue()
        )

        results = model.predict(
            source=temp_file.name,
            conf=0.25
        )

        result_image = results[0].plot()

        st.image(
            result_image,
            caption="Detection Result"
        )