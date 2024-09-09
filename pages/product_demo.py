import streamlit as st
import requests

# Set the API URL
API_URL = 'https://fashval-x5mrnd2lfa-ew.a.run.app/predict'


st.markdown('''
# 2nd Hand Fashion Evaluation
## Sell you pre-owned luxury items at the optimal price!
''')

def load_options(file_path):
    with open(file_path, 'r') as file:
        options = [line.strip() for line in file]
    return options


brands = load_options('unique_values_txt_files/uv_brands.txt')
materials = load_options('unique_values_txt_files/uv_materials.txt')
conditions = load_options('unique_values_txt_files/uv_condition.txt')
shipping_days = load_options('unique_values_txt_files/uv_shipping_days.txt')
genders = load_options('unique_values_txt_files/uv_gender.txt')
colors = load_options('unique_values_txt_files/uv_colors.txt')
categories = load_options('unique_values_txt_files/uv_category.txt')
seasons = load_options('unique_values_txt_files/uv_season.txt')
seller_badges = load_options('unique_values_txt_files/uv_seller_badge.txt')

st.title('Product Information')

product_description = st.text_input('Enter a short product description: ')

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
