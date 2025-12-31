# Text To Speech with Python

from newspaper import Article
import nltk
from gtts import gTTS
import os

# Get the article
article = Article('https://hackernoon.com/future-of-python-language-bright-or-dull-uv41u3xwx')

# Download and parse
article.download()
article.parse()

# Download nltk punkt (only first time)
nltk.download('punkt')

# Apply NLP
article.nlp()

# Get article text
mytext = article.text

# Select language
language = 'en'  # English

# Convert text to speech
myobj = gTTS(text=mytext, lang=language, slow=False)

# Save audio file
myobj.save("read_article.mp3")

# Play audio (Windows)
os.system("start read_article.mp3")