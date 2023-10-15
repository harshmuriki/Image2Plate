import streamlit as st
import cv2
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
import requests
from webcam import webcam
import io
import av
from PIL import Image

# API_URL = "https://api-inference.huggingface.co/models/google/vit-base-patch16-224"
API_URL = "https://api-inference.huggingface.co/models/microsoft/resnet-50"

headers = {"Authorization": "Bearer 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"}

captured_image = webcam()


def query(img):
    img_bytes = io.BytesIO()
    img = img.convert("RGB")
    img.save(img_bytes, format='JPEG')
    response = requests.post(API_URL, headers=headers,
                             data=img_bytes.getvalue())
    return response.json()


idx = 0
if captured_image is None:
    st.write("Waiting for capture...")
else:
    st.write("Got an image from the webcam:")
    st.image(captured_image)
    print(type(captured_image))
    frame = av.VideoFrame

    val = query(captured_image)
    print("identified:", val)

    st.write(val)
