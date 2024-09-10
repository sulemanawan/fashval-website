import streamlit as st
import requests

# Set the API URL
API_URL = 'https://fashval-x5mrnd2lfa-ew.a.run.app/predict'

# Set page config to wide layout
st.set_page_config(layout="wide")

# Hide default Streamlit menu and footer
hide_default_format = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_default_format, unsafe_allow_html=True)

# Load options from text files
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

st.markdown("""
    <style>
        body {
            background: url("https://i.kinja-img.com/image/upload/c_fill,h_900,q_60,w_1600/707141e2979c393e3bfed23e892dfa28.jpg");
            background-size: cover;
        }
    </style>""", unsafe_allow_html=True)

# Apply custom CSS styles
st.markdown('''
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
    }
    .stApp {
        max-width: 80% !important; /* Limit the width of the entire app */
        margin: 0 auto; /* Center the content */
        padding: 20px; /* Add padding around the content */
    }
    .stSelectbox>div>div {
        width: 100% !important;
        height: 60px !important; /* Consistent height for select boxes */
        padding: 10px; /* Padding inside the select boxes */
        background-color: #D4C9BA !important;
        border: 1px solid #555555 !important;
        color: #94806B !important; /* Correct text color */
        font-size: 20px !important;
        box-sizing: border-box;
        margin-bottom: 20px; /* Space between fields */
    }
    /* Style for the dropdown options when the dropdown is expanded */
    .stSelectbox > div > div > div {
        background-color: #D4C9BA !important;  /* Options background color */
        color: #94806B !important;  /* Options text color */
    }

    /* Style for the dropdown arrow */
    .stSelectbox > div > div > svg {
        color: #94806B !important;  /* Arrow color */
    }

    /* Style for the dropdown options on hover */
    .stSelectbox > div > div > div > div:hover {
        background-color: #BEBEBC !important;  /* Hover background color */
        color: #94806B !important;  /* Hover text color */
    }


    .stTextInput>div>textarea::placeholder {
        font-size: 20px !important;  /* Change this value to your desired font size */
        color: #7F7F7F !important;   /* Optional: Change placeholder color if needed */
    }

    .stNumberInput>div {
        width: 100% !important;
        height: 60px !important;
        padding: 10px;
        background-color: #D4C9BA !important;
        border: 1px solid #555555 !important;
        color: #94806B !important;
        font-size: 20px !important;
        box-sizing: border-box;
        margin-bottom: 20px;
    }

    .stButton>button {
        background-color: #D4C9BA !important;
        color: #ffffff !important;
        border: 2px solid #555555 !important;
        font-size: 30px !important;
        font-weight: bold;
        border-radius: 5px;
        padding: 12px 24px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #8c6c4f !important;
    }
    .header {
        text-align: center;
        color: #d4af37 !important;
        margin-bottom: 20px; /* Corrected margin */
    }
    .title {
        font-size: 20px;
        color: #ffffff;
        margin-bottom: -80px; /* Space between title and field */
        line-height: 1; /* Adjust line height if needed */
    }

    /* Hide labels for number inputs */
    .stNumberInput > div > label {
        display: none !important;
    }
</style>
''', unsafe_allow_html=True)

# Header
st.markdown('''
    <div class="header">
        <h1 style="color:#ffffff;">2nd Hand Fashion Evaluation</h1>
        <h2 style="color:#ffffff;">Sell your pre-owned luxury items at the optimal price!</h2>
    </div>
''', unsafe_allow_html=True)

# Info section with inline CSS for text styling
st.markdown(
    '<p style="font-size:24px; text-align: center;color:#ffffff;">Want to know how much your barely used luxury items are worth?</p>',
    unsafe_allow_html=True
)
st.markdown(
    '<p style="font-size:24px; text-align: center;color:#ffffff;">Give us some information about your item and we will answer this question for you!</p>',
    unsafe_allow_html=True
)

# Page title
st.markdown(
    '<h1 style="font-size:24px; color:#ffffff";">Product Information</h1>',
    unsafe_allow_html=True
)

with st.container():
    # Adjusting layout for product description
    st.markdown('<p class="title">Product Description:</p>', unsafe_allow_html=True)
    product_description = st.text_area('', placeholder='Enter a short product description here...', height=100)
    if not product_description:
        st.warning('Please enter a product description.')

    # Split remaining input fields across two columns
    col1, col2 = st.columns(2)  # Equal column widths

    with col1:
        st.markdown('<p class="title">Select Material:</p>', unsafe_allow_html=True)
        product_material = st.selectbox('', materials)

        st.markdown('<p class="title">Select Brand:</p>', unsafe_allow_html=True)
        brand_name = st.selectbox('', brands)

        st.markdown('<p class="title">Select Condition:</p>', unsafe_allow_html=True)
        product_condition = st.selectbox('', conditions)

        st.markdown('<p class="title">Select Shipping Time:</p>', unsafe_allow_html=True)
        shipping_days = st.selectbox('', shipping_days)

        st.markdown('<p class="title">Enter the number of products sold:</p>', unsafe_allow_html=True)
        seller_products_sold = st.number_input('', min_value=0, step=1)

    with col2:
        st.markdown('<p class="title">Select Target Gender:</p>', unsafe_allow_html=True)
        product_gender = st.selectbox('', genders)

        st.markdown('<p class="title">Select Color:</p>', unsafe_allow_html=True)
        product_color = st.selectbox('', colors)

        st.markdown('<p class="title">Select Category:</p>', unsafe_allow_html=True)
        product_category = st.selectbox('', categories)

        st.markdown('<p class="title">Select Season:</p>', unsafe_allow_html=True)
        product_season = st.selectbox('', seasons)

        st.markdown('<p class="title">Select Seller Badge:</p>', unsafe_allow_html=True)
        seller_badge = st.selectbox('', seller_badges)

    # Submit button
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

            # Make a GET request to the API
            try:
                response = requests.get(url=API_URL, params=data)
                if response.status_code == 200:
                    predicted_price = response.json()['price']
                    st.success(f'The predicted price for the product is: ${predicted_price}')
                else:
                    st.error('Error: Could not get a prediction from the API.')

            except Exception as e:
                st.error(f'Error occurred while making the API request: {e}')
