import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
from base64 import b64encode
from io import BytesIO

favicon_path = "images/favicon.ico"

# Function to convert image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return f"data:image/x-icon;base64,{b64encode(f.read()).decode('utf-8')}"

# Set page config with favicon
st.set_page_config(page_title="Vernon-Novo Group", page_icon=image_to_base64(favicon_path), layout="wide")


# Center the image
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Load IMAGES
img_logo = Image.open("images/NOVO-Trans.png")
img_tanker1 = Image.open("images/tanker.png")
img_barrel = Image.open("images/oil barrel.png")


# Pages of the Website
def home():
    st.markdown(
        f'<div style="text-align: center;"><img src="data:image/png;base64,{image_to_base64(img_tanker1)}" width="1100"></div>',
        unsafe_allow_html=True
    )


def about_us():
    with st.container():
        st.write("---")
        st.title("About Us")
        image_column, text_column = st.columns(2)
        with text_column:
            st.write("##")
            st.write(""" Novo, formally known as Vernon-Novo Group Ltd, is a reputable Ghanaian
    agency founded in August 2019. Our core operations revolve around the
    petroleum marketing sector, with a dedicated focus on delivering top quality
    petroleum products at the most competitive prices.""")
        with image_column:
            st.image(img_logo)


def values():
    with st.container():
        st.write("---")
        st.title("Our Values")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Our Vision")
            st.write(
                """ To Be A World-Class Provider Of Goods And Services In The Petroleum Industry.""")
        with right_column:
            st.subheader("Our Mission")
            st.write(""" To market quality petroleum services in all its branches in an ethical, healthy, safe,
environmentally friendly and socially responsible manner.""")


def services():
    with st.container():
        st.write("---")
        st.title("Our Services")
        left_column, right_column = st.columns(2)
        with right_column:
            st.write("""At Novo, We specialize in
    the supply of various commodities such as Crude Oil, Gas Oil, Gasoline, Fuel Oil,
    Liquified Natural Gas (LNG), Liquified Petroleum Gas (LPG), and other related
    products. At Novo, we are dedicated to fostering lasting partnerships, delivering
    value, and making a positive impact on the energy landscape in Ghana and
    beyond.""")
        with left_column:
            st.image(img_barrel)


def contact():
    st.write("---")
    st.title("Contact Us")

    contact_form = """
    <form action="https://formsubmit.co/kelennison@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with right_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with left_column:
        st.write("Feel free to reach out to us. Here's our contact information.")
        st.write("Address: Near Mystical Rose Academy, Accra")
        st.write("Email: novogroupgh@outlook.com")
        st.write("Phone Number:+233205182314 / +233553137533 / +233557385970")


# horizontal menu to access the pages
EXAMPLE_NO = 1


def streamlit_menu(example=1):
    if example == 1:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Who We Are", "Values",
                     "Services", "Contact Us"],  # required
            orientation="horizontal",
            styles={
                # Remove the background color
                "container": {"padding": "0!important"},
                "icon": {"display": "none"},  # Hide the arrow icons
                "nav-link": {
                    "font-size": "15px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "black",  # Change the hover color to black
                },
                "nav-link-selected": {"background-color": "black"},
            },
        )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Home":
    home()
if selected == "Who We Are":
    about_us()
if selected == "Values":
    values()
if selected == "Services":
    services()
if selected == "Contact Us":
    contact()
