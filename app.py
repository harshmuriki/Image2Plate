import streamlit as st
import requests
from webcam import webcam
import io
import cv_model
import create_dish

openaikey = st.text_input('OpenAI Key', '')

captured_image = webcam()

list_of_items = []

idx = 0
if captured_image is None:
    st.write("Waiting for capture...")
else:
    st.write("Got an image from the webcam:")
    st.image(captured_image)
    print(type(captured_image))
    val = cv_model.find_objects(captured_image)
    if val:
        list_of_items.append(val)
        st.write(val)

    st.write("Object Captured:", val)

# get recipes
if st.button("Create the Recipes!!!"):
    st.write("Object Captured:", list_of_items)
    init_prompt = "These are the list of food items. Give me recipes based on these assuming I have the basic spices"
    response = create_dish.openai_prompt(init_prompt, list_of_items, openaikey)

    st.write("OpenAI response:", response)
