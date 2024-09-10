import streamlit as st
import os
import requests

# Set the API URL
API_URL = 'https://fashval-x5mrnd2lfa-ew.a.run.app/predict'
# Define custom colors


hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

def load_options(file_path):
    with open(file_path, 'r') as file:
        options = [line.strip() for line in file]
    return options

# Load options for select boxes
brands = load_options('unique_values_txt_files/uv_brands.txt')
materials = load_options('unique_values_txt_files/uv_materials.txt')
conditions = load_options('unique_values_txt_files/uv_condition.txt')
shipping_days = load_options('unique_values_txt_files/uv_shipping_days.txt')
genders = load_options('unique_values_txt_files/uv_gender.txt')
colors = load_options('unique_values_txt_files/uv_colors.txt')
categories = load_options('unique_values_txt_files/uv_category.txt')
seasons = load_options('unique_values_txt_files/uv_season.txt')
seller_badges = load_options('unique_values_txt_files/uv_seller_badge.txt')

# Apply custom CSS styles

# Apply custom CSS styles
st.markdown('''
    <style>
    body {
        background-color: #333333 !important;
        color: #ffffff !important;
        font-family: Arial, sans-serif;
    }
    .stTextInput>div>input {
        background-color: #444444 !important;
        border: 1px solid #555555 !important;
        font-size: 24px;
        color: #ffffff !important;
    }
    .stSelectbox>div>div {
        background-color: #444444 !important;
        border: 1px solid #555555 !important;
        color: #ffffff !important;
    }
    .stSelectbox>div>div>div {
        color: #ffffff !important;  /* Dropdown text color */
    }
    .stButton>button {
        background-color: #b08d57 !important;
        color: #ffffff !important;
        border: 2px solid #555555 !important;
        font-size: 20px;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #8c6c4f !important;
    }
    .stWarning {
        color: #ffcc00 !important;
    }
    .stError {
        color: #e74c3c !important;
    }
    .header {
        text-align: center;
        color: #d4af37 !important;
        margin-bottom: 20px;
    }
    </style>
    <div class="header">
        <h1>2nd Hand Fashion Evaluation</h1>
        <h2>Sell your pre-owned luxury items at the optimal price!</h2>
    </div>
    ''', unsafe_allow_html=True)

# Info section with inline CSS for text styling
st.markdown(
    '<p style="font-size:20px; color:white;">Want to know how much your barely used luxury items are worth?</p>',
    unsafe_allow_html=True
)
st.markdown(
    '<p style="font-size:20px; color:white;">Give us some information about your item and we will answer this question for you!</p>',
    unsafe_allow_html=True
)

# Page title
st.markdown(
    '<h1 style="font-size:36px; color:white;">Product Information</h1>',
    unsafe_allow_html=True
)

product_description = st.text_input('Enter a short product description: ')
if not product_description:
    st.warning('Please enter a product description.')

# Drop-down menus for selections
product_material = st.selectbox('Select Material', materials)
brand_name = st.selectbox('Select Brand', brands)
product_condition = st.selectbox('Select Condition', conditions)
shipping_days = st.selectbox('Select Shipping Time', shipping_days)
product_gender = st.selectbox('Select Gender Target', genders)
product_color = st.selectbox('Select Color', colors)
product_category = st.selectbox('Select Category', categories)
product_season = st.selectbox('Select Season', seasons)
seller_badge = st.selectbox('Select Seller Badge', seller_badges)

seller_products_sold = st.number_input('Enter the number of products sold', min_value=0, step=1)

if st.button('Submit'):
    # Validate that all necessary fields are filled
    if not product_description:
        st.warning('Please enter a product description.')
    else:
        # Prepare data to send to the API
        data = {
        'product_description': product_description,
        'product_material': product_material,
        'brand_name': brand_name,
        'product_condition': product_condition,
        'shipping_days': shipping_days,
        'product_gender': product_gender,
        'product_color': product_color,
        'product_category': product_category,
        'product_season': product_season,
        'seller_badge': seller_badge,
        'seller_products_sold': seller_products_sold
        }

        # Make a POST request to the API
        try:
            response = requests.get(url = API_URL, params=data)
            if response.status_code == 200:
                predicted_price = response.json()['price']
                st.success(f'The predicted price for the product is: ${predicted_price}')
            else:
                st.error('Error: Could not get a prediction from the API.')

        except Exception as e:
            st.error(f'Error occurred while making the API request: {e}')



    # Make a POST request to the API
    #try:
        #response = requests.post(API_URL, data=data)
        #if response.status_code == 200:
            #predicted_price = response.json().get('predicted_price', 'No price returned')
            #st.success(f'The predicted price for the product is: ${predicted_price}')
        #else:
            #st.error('Error: Could not get a prediction from the API.')
    #except Exception as e:
        #st.error(f'Error occurred while making the API request: {e}')
