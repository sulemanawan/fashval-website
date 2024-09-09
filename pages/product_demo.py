import streamlit as st


st.markdown('''
#2nd Hand Fashion Evaluation
## Sell you pre-owned luxury items at the optimal price!
''')

def load_options(file_path):
    with open(file_path, 'r') as file:
        options = [line.strip() for line in file]
    return options

'''
## Here we would like to add some controllers in order to ask the user to select the parameters
'''
# Load options from txt files
brands = load_options('unique_values_txt_files/uv_brands.txt')
materials = load_options('unique_values_txt_files/uv_materials.txt')
conditions = load_options('unique_values_txt_files/uv_condition.txt')
shipping_days = load_options('unique_values_txt_files/uv_shipping_days.txt')
genders = load_options('unique_values_txt_files/uv_gender.txt')
colors = load_options('unique_values_txt_files/uv_colors.txt')
categories = load_options('unique_values_txt_files/uv_category.txt')
seasons = load_options('unique_values_txt_files/uv_season.txt')
seller_badges = load_options('unique_values_txt_files/uv_seller_badge.txt')

# Streamlit app layout
st.title('Product Information')

# Input field for product description
product_description = st.text_input('Enter a short product description: ')

# Drop-down menus for selections
material = st.selectbox('Select Material', materials)
brand = st.selectbox('Select Brand', brands)
condition = st.selectbox('Select Condition', conditions)
shipping_time = st.selectbox('Select Shipping Time', shipping_days)
gender_target = st.selectbox('Select Gender Target', genders)
color = st.selectbox('Select Color', colors)
category = st.selectbox('Select Category', categories)
season = st.selectbox('Select Season', seasons)
seller_badge = st.selectbox('Select Seller Badge', seller_badges)

# Input field for number of products sold
products_sold = st.number_input('Enter the number of products sold', min_value=0, step=1)

# Button to submit the form
if st.button('Submit'):

    st.write('Product Description:', product_description)
    st.write('Material:', material)
    st.write('Brand:', brand)
    st.write('Condition:', condition)
    st.write('Shipping Time:', shipping_time)
    st.write('Gender Target:', gender_target)
    st.write('Color:', color)
    st.write('Category:', category)
    st.write('Season:', season)
    st.write('Seller Badge:', seller_badge)
    st.write('Number of Products Sold:', products_sold)
