import re
from utils import extract_keywords, extract_tfidf_keywords

import tkinter as tk
from tkinter import filedialog

def choose_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    return file_path

def parse_chat_log(file_path):
    user_messages = []
    ai_messages = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line_lower = line.lower()
            if line_lower.startswith("user:"):
                user_messages.append(line[5:].strip())
            elif line_lower.startswith("ai:"):
                ai_messages.append(line[3:].strip())

    return user_messages, ai_messages

def get_message_stats(user_messages, ai_messages):
    return {
        "total_messages": len(user_messages) + len(ai_messages),
        "user_messages": len(user_messages),
        "ai_messages": len(ai_messages)
    }

def generate_summary(stats, keywords):
    print("Summary:")
    print(f"- Total messages: {stats['total_messages']}")
    print(f"- User messages: {stats['user_messages']}, AI messages: {stats['ai_messages']}")
    print(f"- Most common keywords: {', '.join(keywords)}")
    topic_summary = ', '.join(keywords[:3])
    print(f"- The user asked mainly about {topic_summary}.")

if __name__ == "__main__":
    filepath = choose_file()
    if filepath:
        user_msgs, ai_msgs = parse_chat_log(filepath)
        stats = get_message_stats(user_msgs, ai_msgs)
        keywords = extract_tfidf_keywords(user_msgs + ai_msgs)
        generate_summary(stats, keywords)

