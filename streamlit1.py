import streamlit as st
from newsAPI import NewsAPI
from tts_video import VideoGenerator
from dotenv import load_dotenv
import os
import base64

load_dotenv()

news_api_key = os.getenv("NEWS_API_KEY")
username = os.getenv("VIDEO_API_USERNAME")
password = os.getenv("VIDEO_API_PASSWORD")

news_client = NewsAPI(api_key=news_api_key)

video_api_key = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('utf-8')
video_generator = VideoGenerator(video_api_key)

st.set_page_config(
    page_title="AI News Presenter",
    layout="wide"
)

st.title("AI News Presenter")
st.markdown('<style>h1{color: orange; text-align: center;}</style>', unsafe_allow_html=True)
st.subheader('Built with ❤️ by Dharmanshu Singh')
st.markdown('<style>h3{color: pink;  text-align: center;}</style>', unsafe_allow_html=True)

image_url = st.text_input("Enter Image URL of the anchor from MidJourney", "")
query = st.text_input("Enter Query Keywords for news", "")
num_news = st.slider("Number of News", min_value=1, max_value=5, value=3)

if st.button("Generate"):
    if image_url.strip() and query.strip() and num_news > 0:
        try:
            col1, col2, col3 = st.columns([1, 1, 1])

            with col1:
                st.info("Your AI News Anchor: Sophie")
                st.image(image_url, caption="Anchor Image", use_column_width=True)

            with col2:
                desc_list = news_client.get_news_descriptions(query, num_news=num_news)
                st.success("Your Fetched News")
                numbered_paragraphs = "\n".join([f"{i+1}. {paragraph}" for i, paragraph in enumerate(desc_list)])
                st.write(numbered_paragraphs)

            with col3:
                final_text = f"""
                    Hello World, I'm Sophie, your AI News Anchor. Bringing you the latest updates for {query}.
                    Here are the news for you: {numbered_paragraphs}
                    That's all for today. Stay tuned for more news, Thank you!
                """

                video_url = video_generator.generate_video(final_text, image_url)
                print(f"Video URL: {video_url}")
                if video_url:
                    st.warning("AI News Anchor Video")
                    st.video(video_url)
                else:
                    st.error("Failed to generate video. Please try again later.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter all required fields.")
