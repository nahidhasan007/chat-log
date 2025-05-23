﻿Chat Log Keyword Extractor and Summary Generator
Features
Parses chat logs with lines starting with User: or AI: (case-insensitive).

Separates and counts messages from User and AI.

Extracts top keywords from the conversation using:

Frequency-based keyword extraction (with NLTK).

TF-IDF based keyword extraction (with scikit-learn).

Generates a summary that includes:

Total number of messages.

Number of User and AI messages.

Most common keywords.

A natural language summary of main topics.


chat-log-Text Analyzer/
│
├── main.py                 
├── utils.py                
├── README.md              
├── summarizer.py        
└── sample_chat.txt 

Requirements
Python 3.6+

Packages:

nltk

scikit-learn

tkinter (usually included with Python for file dialogs)

Install the required Python packages with:

bash
Copy
Edit
pip install nltk scikit-learn
Setup
Before running the script, download the necessary NLTK data by running:

python
Copy
Edit
import nltk
nltk.download('punkt')
nltk.download('stopwords')
Usage
Run the main script.

A file dialog will open — select your .txt chat log file.

The script will parse the chat log, extract keywords, and print a summary.
