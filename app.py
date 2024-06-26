import os
import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS

def local_css(file_name):
    """Function to apply local CSS file to Streamlit app."""
    path = os.path.join(os.path.dirname(__file__), file_name)
    with open(path) as f:
        css = f.read()
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Assuming this function is called somewhere else in your script
local_css("style/style.css")
# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/117fc2df-5079-4d2f-a056-c1b21ef9f06f/dXAatK1ZJM.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Samuel :wave:")
    st.title("A Data Scientist & Analyst From Spain")
    st.write("As an aspiring data scientist & data analyst, I am fueled by curiosity and driven to excel in this dynamic field. With a foundation in data analysis and a keen eye for detail, I am eager to apply my skills and learn from seasoned professionals. I approach each project with enthusiasm and a commitment to continuous improvement, ready to contribute fresh perspectives and make meaningful contributions to your team.")
    st.write("[Learn More >](https://www.linkedin.com/in/samuel-baah-sr/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("""
        About Me

        Welcome to my professional corner!

        Who I Am

        I'm Samuel Baah, a dedicated and passionate Data Analyst with one year of experience in the industry. I have a solid foundation in data analysis and am driven by a desire to help companies make informed decisions through data insights.

        My Journey

        My professional journey began in 2023 when I graduated from Impelia Campus with a degree in Data Science and Analytics. Shortly after, I had the opportunity to start my career with ALTEN in Spain, where I have been contributing to impactful projects and refining my skills in data analysis.

        What I Do

        I specialize in data analysis, with a focus on transforming complex data sets into actionable insights. My work is characterized by my attention to detail and my ability to communicate findings effectively. I thrive in collaborative environments and am passionate about leveraging data to help companies achieve their goals.

        Why Choose Me?

        - Experience: Although I have one year of experience, I bring a fresh perspective and up-to-date knowledge in data analysis.
        
        - Quality: I am committed to delivering high-quality analysis and insights that drive strategic decisions.
        
        - Passion: My passion for helping companies succeed through data analysis drives me to continuously learn and improve.

        My Skills

        - Teamwork: I have successfully collaborated with my colleagues at ALTEN to deliver complex projects efficiently and effectively.
        
        - Communication: I possess strong communication skills, enabling me to present data insights in a clear and understandable manner.
        
        - Adaptability: I am a fast learner who quickly adapts to new tools and methodologies, ensuring that I stay ahead in the ever-evolving field of data analysis.

        Let's Connect

        I am always looking for new opportunities to grow and contribute. If you are looking for a Data Analyst who is dedicated, innovative, and results-driven, I would love to connect. Feel free to reach out to me at samuelbaah531@gmail.com or connect with me on https://www.linkedin.com/in/samuel-baah-sr/.

        Thank you for visiting my profile. I look forward to the possibility of working together!
        """)
        
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        
        
# ---- Contact ---- 
with st.container():
    st.write("---")
    st.header("Get in Touch With Me")
    st.write("##")
    
    # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS
    
    contact_form = """ 
    <form action="https://formsubmit.co/samuelbaah531@gmail.com" method="POST">
        <input type= "hidden" name = "_captcha" value= "false">
        <input type="text" name="name" placeholder = "Your name" required>
        <input type="email" name="email" placeholder = "Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>

    """
    
    left_column , right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()