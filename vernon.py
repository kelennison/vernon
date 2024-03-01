import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from time import sleep
from PIL import Image
import base64
from base64 import b64encode
from io import BytesIO
import os 
import pathlib
import shutil
import logging
from bs4 import BeautifulSoup
import re


# Path to the favicon image in ICO format
favicon_path = "images/favicon.ico"

# Function to convert image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return f"data:image/x-icon;base64,{b64encode(f.read()).decode('utf-8')}"


# Path to the favicon image in ICO format
favicon_path = "images/favicon.ico"

# Set page config with favicon
st.set_page_config(page_title="Vernon-Novo Group",
                   page_icon=image_to_base64(favicon_path), layout="wide")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")  # Load your existing CSS file


# Center the image on home page
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


# Load IMAGES
img_logo_dark = Image.open("images/NOVO-Trans.png")
img_logo_light = Image.open("images/NOVO LOGO.png")
img_tanker1 = Image.open("images/tanker.png")
img_barrel = Image.open("images/oil barrel.png")


# Pages of the Website
def home():
    st.write("---")
    st.markdown(
        f'<div style="text-align: center;"><img src="data:image/png;base64,{image_to_base64(img_tanker1)}" width="1100"></div>',
        unsafe_allow_html=True
    )


def about_us():
    with st.container():
        st.write("---")
        st.title("Who We Are")
        image_column, text_column = st.columns(2)
        with text_column:
            st.write("##")
            st.write(""" Novo, formally known as Vernon-Novo Group Ltd, is a reputable Ghanaian
    agency founded in August 2019. Our core operations revolve around the
    petroleum marketing sector, with a dedicated focus on delivering top quality
    petroleum products at the most competitive prices.""")
        with image_column:
            st.image(img_logo_dark)


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
    sleep(1)  # Introduce a 1-second delay
    home()
if selected == "Who We Are":
    sleep(1)  # Introduce a 1-second delay
    about_us()
if selected == "Values":
    sleep(1)  # Introduce a 1-second delay
    values()
if selected == "Services":
    sleep(1)  # Introduce a 1-second delay
    services()
if selected == "Contact Us":
    sleep(1)  # Introduce a 1-second delay
    contact()



adsense_url = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"
GA_AdSense = """
      <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7885625779726639"
     crossorigin="anonymous"></script>
<!-- Square ads -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-7885625779726639"
     data-ad-slot="3146417758"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
    """

 # Insert the script in the head tag of the static template inside your virtual
index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
logging.info(f'editing {index_path}')
soup = BeautifulSoup(index_path.read_text(), features="html.parser")
if not soup.find("script", src=adsense_url): 
    bck_index = index_path.with_suffix('.bck')
    if bck_index.exists():
        shutil.copy(bck_index, index_path)  
    else:
        shutil.copy(index_path, bck_index)  
    html = str(soup)
    new_html = html.replace('<head>', '<head>\n' + GA_AdSense)
    index_path.write_text(new_html)




second_script = """
<script type="text/javascript">//<![CDATA[ 
(function() {
    var configuration = {
        "token": "a1c6282764be55d461d230bc4f50546e",
        "excludeDomains": [
            "yourowndomain.com"
        ],
        "capping": {
            "limit": 5,
            "timeout": 24
        }
    };
    var script = document.createElement('script');
    script.async = true;
    script.src = '//cdn.shorte.st/link-converter.min.js';
    script.onload = script.onreadystatechange = function () {var rs = this.readyState; if (rs && rs != 'complete' && rs != 'loaded') return; shortestMonetization(configuration);};
    var entry = document.getElementsByTagName('script')[0];
    entry.parentNode.insertBefore(script, entry);
})();
//]]></script>
"""

# Bootstrap 4 collapse example with both JavaScript snippets
html_string = f"""
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<div id="accordion">
  <div class="card">
    <div class="card-header" id="headingOne">
      <h5 class="mb-0">
        <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
        Collapsible Group Item #1
        </button>
      </h5>
    </div>
    <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
      <div class="card-body">
        Collapsible Group Item #1 content
      </div>
    </div>
  </div>
  <div class="card">
    <div class="card-header" id="headingTwo">
      <h5 class="mb-0">
        <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
        Collapsible Group Item #2
        </button>
      </h5>
    </div>
    <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
      <div class="card-body">
        Collapsible Group Item #2 content
      </div>
    </div>
  </div>
</div>
{second_script}
"""

# Display the HTML string with both JavaScript snippets
components.html(html_string, height=600)


