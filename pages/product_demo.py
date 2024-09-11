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
        max-width: 80% !important;
        margin: 0 auto;
        padding: 20px;
    }

    /* General Selectbox Styling */
    .stSelectbox>div {
        width: 100% !important;
        height: 60px !important;
        background-color: #D4C9BA !important; /* Beige background */
        border: 1px solid #94806B !important;
        padding: 10px !important;
        height: 60px !important; /* Set consistent height */
        font-size: 18px !important;
        margin-bottom: 20px;
        border-radius: 10px !important;
    }

    /* Style for text area container */
    .stTextArea textarea {
        font-size: 22px !important;
        color: #7F7F7F !important;
        padding: 10px !important;
        box-sizing: border-box;
        line-height: 1.5 !important;
        border: 2px solid #94806B !important; /* Border color */
        border-radius: 10px !important; /* Rounded corners */
    }

    /* Style for placeholder text */
    .stTextArea textarea::placeholder {
        font-size: 22px !important;
        color: #7F7F7F !important;
    }


    /* Style for the container of the number input */
    .st-emotion-cache-1e043ys.e116k4er3 {
        border: 1px solid #94806B !important; /* Border color */
        border-radius: 10px !important; /* Rounded corners */
        background-color: #D4C9BA !important; /* Background color */
        padding: 10px !important; /* Padding */
        height: 60px;
    }

    /* Style for the number input field itself */
    .st-be.st-cg.st-db.st-dc.st-dd.st-de.st-ch.st-cj.st-ci.st-ck.st-cl.st-b9.st-df.st-cb.st-bh.st-dg.st-c4.st-c5.st-c6.st-c7.st-ae.st-af.st-ag.st-bd.st-ai.st-aj.st-bs.st-dl.st-dm {
        border: none !important; /* Remove default border if needed */
        background-color: transparent !important; /* Transparent background */
        color: #94806B !important; /* Text color */
        font-size: 24px !important; /* Font size */
        height: 60px;
    }

    /* Style for the step buttons */
    .st-emotion-cache-76z9jo.e116k4er2 {
        display: flex;
        height: 100%;
        font-size: 24px;
        flex-direction: row;
    }

    /* Style for the step buttons */
    .st-emotion-cache-44e0oq.e116k4er1 {
        border: none !important;
        background-color: #D4C9BA !important; /* Match background color */
        height: 100% !important; /* Make buttons fill half the container height */
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0 !important; /* Remove padding */
        cursor: pointer;
    }

    .st-emotion-cache-44e0oq.e116k4er1 {
        border: none !important;
        background-color: transparent !important;
    }

    button.st-emotion-cache-s5ekhb.ef3psqc8 {
        background-color: #B4A069 !important;
        color: #ffffff !important;
        border: 2px solid #94806B !important;
        font-weight: bold;
        border-radius: 5px;
        padding: 15px 20px !important;
        margin-bottom: 20px !important;
        cursor: pointer;
    }
    .stButton>button {
        font-size: 30px !important;
        padding: 15px 20px !important; /* Adjust padding if needed */
    }

    .header {
        text-align: center;
        color: #d4af37 !important;
        margin-bottom: 20px;
    }
    .title {
        font-size: 20px;
        color: #ffffff;
        margin-bottom: -80px;
        line-height: 1;
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

with st.form("my_form"):
    # Adjusting layout for product description
    st.markdown('<p class="title">Product Description:</p>', unsafe_allow_html=True)
    product_description = st.text_area('', placeholder='Enter a short product description here...', height=100)
    if not product_description:
        st.warning('Please enter a product description.')

    # Split remaining input fields across two columns
    col1, col2 = st.columns([1,1])  # Equal column widths

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
        seller_products_sold = st.number_input('', min_value=0, step=1, key='number_input')

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


    submit_button = st.form_submit_button(label="Submit")



    # Submit button
    if submit_button:
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
