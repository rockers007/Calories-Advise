import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_promt,image):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input_promt,image[0]])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        
        image_parts=[
            {
                "mime_type": uploaded_file.type,
                "data" : bytes_data
            }
        ]
        
        return image_parts
    else:
        raise FileNotFoundError("file not found")

## front end setup    
st.set_page_config(page_title = "Calories Advisori app")
st.header("Gemini health app")
uploaded_file = st.file_uploader("Choose an image..",type=["jpg","jpeg","png","gif"])
image=""
if uploaded_file is not None:
    image= Image.open(uploaded_file) 
    st.image(image ,caption="Uploaded Image" ,use_column_width=True)
    
submit=st.button("Tell me about total calories")   

input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----
        Finally you can also mention weather food is healthy or not and also mention
        the percentage split of ratio of carbohydrates,fats,fibers,sugar and other important things
        required in our diet

"""

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt,image_data)
    st.header("response is here")
    st.write(response)
 