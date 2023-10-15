import streamlit as st
import requests
from webcam import webcam
import io
# import cv_model
import create_dish

openaikey = st.text_input('OpenAI Key', '')
hfkey = st.text_input('hf Key', '')
empty_str = ""
if 'list_of_items' not in st.session_state:
    st.session_state.list_of_items = []

if 'all_data' not in st.session_state:
    st.session_state.all_data = ""

captured_image = webcam()


API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-101"
headers = {"Authorization": hfkey}


def query(img):
    img_bytes = io.BytesIO()
    img = img.convert("RGB")
    img.save(img_bytes, format='JPEG')
    response = requests.post(API_URL, headers=headers,
                             data=img_bytes.getvalue())
    return response.json()[0]["label"]


idx = 0
if captured_image is None:
    st.write("Waiting for capture...")
else:
    st.write("Got an image from the webcam:")
    st.image(captured_image)
    # print(type(captured_image))
    # val = cv_model.find_objects(captured_image)
    val = query(captured_image)
    if val:
        st.session_state.list_of_items.append(val)
        st.write(val)


for i in st.session_state.list_of_items:
    st.session_state.all_data += i + ", "

# print("hweqw", st.session_state.all_data)
st.write("Objects Captured:", st.session_state.all_data)

# get recipes
if st.button("Create the Recipes!!!"):

    st.write("Object Captured:", st.session_state.list_of_items)
    init_prompt = "These are the list of food items. Give me recipes based on these assuming I have the basic spices"
    response = create_dish.openai_prompt(
        init_prompt, st.session_state.all_data, openaikey)

    st.write("AI response:", response)
