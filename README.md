# AI News Presenter

This project is an **AI-powered news presenter** that reads news articles in a human-like voice. It leverages natural language processing and text-to-speech (TTS) synthesis to create a realistic news presentation experience. The AI presenter allows users to submit any AI image of anchor and the news content is fetched dynamically using the NewsAPI service.

## Features

- **Text-to-Speech Synthesis**: Converts news articles into speech using the Microsoft Azure TTS service via D-ID API.
- **Customizable Presenter**
- **Streamlit Web Application**: A simple and interactive web interface using Streamlit.
- **News Input**: Users can input keywords to fetch news articles, which are then read aloud by the AI.
- **Virtual Avatar**: The news presenter reads articles aloud while the text is displayed on the screen.

## Text-to-Speech Model

We are using **Microsoft Azure Text-to-Speech (TTS)** via the **D-ID API**. The specific neural voice model used is `"en-US-JennyNeural"`, which produces natural-sounding speech for an enhanced user experience.

For more information about Microsoft's TTS models, visit the [Microsoft Azure Text-to-Speech Documentation](https://azure.microsoft.com/en-us/services/cognitive-services/text-to-speech/).

## News Source

The news content is fetched using the **NewsAPI** service. NewsAPI allows you to search for and retrieve news articles from various sources across the web. 

For more details about NewsAPI, visit the [NewsAPI Documentation](https://newsapi.org/docs).

## Demo Video

[![Watch the video](https://img.youtube.com/vi/Fhs2jQe4msQ/0.jpg)](https://www.youtube.com/watch?v=Fhs2jQe4msQ)

## Deployed Application

The application has been deployed using **Streamlit**. You can access the live version of the AI News Presenter at the following link:

[**AI News Presenter - Live Application**](https://ainewspresentergit-wyvkhrgbufyjwbum6dyffs.streamlit.app/)

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI Models**: Microsoft Azure TTS via D-ID API for text-to-speech synthesis
- **News Source**: NewsAPI
- **Deployment**: Streamlit Cloud

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/dharmanshu1921/Ai_news_presenter.git
    cd Ai_news_presenter
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application locally:
    ```bash
    streamlit run streamlit1.py
    ```

## Usage

1. Open the application in your browser.
2. Input the keywords to search for relevant news articles.
3. upload image link of anchor - # news anchor: https://i.ibb.co/hYcxXTW/anchor.png
4. Click on the "Submit" button to generate the news articles.
5. The AI news presenter will read the articles aloud.

