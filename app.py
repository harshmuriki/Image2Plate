import streamlit as st
# import cv2
# from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
import requests
from webcam import webcam
import io
import cv_model
import create_dish
# import av
# from PIL import Image
# API_URL = "https://api-inference.huggingface.co/models/google/vit-base-patch16-224"
API_URL = "https://api-inference.huggingface.co/models/microsoft/resnet-50"

headers = {"Authorization": "Bearer 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"}

captured_image = webcam()

list_of_items = []


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
    # frame = av.VideoFrame

    # val = query(captured_image)
    # print("identified:", val)
    val = cv_model.find_objects(captured_image)
    # val = "apple"
    if val:
        list_of_items.append(val)
        st.write(val)

    st.write("Object Captured:", val)

# get recipes
if st.button("Create the Recipes!!!"):
    st.write("Object Captured:", list_of_items)
    init_prompt = "These are the list of food items. Give me recipes based on these assuming I have the basic spices"
    response = create_dish.openai_prompt(init_prompt, list_of_items)

    st.write("OpenAI response:", response)
