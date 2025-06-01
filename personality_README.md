# Chatbot Personality & Conversation Design  
**CryptoBuddy – Your First AI-Powered Financial Sidekick!** 🌟

---

## Overview

This documentation covers the **Chatbot Personality** and **Conversation Design** components developed by Member 2 for the CryptoBuddy project.

CryptoBuddy is designed to be a friendly, helpful, and witty AI sidekick that guides users through cryptocurrency investment decisions based on price trends and sustainability.

## Personality & Tone

- **Name:** CryptoBuddy  
- **Voice:** Friendly, approachable, and supportive  
- **Tone:** Lighthearted with a touch of wit, never sarcastic or overly technical  
- **Goal:** Make crypto accessible and fun while providing reliable advice

## Key Features

- Welcoming and engaging introductory messages  
- Helpful responses to common commands like `help` and `exit`  
- Error handling that encourages users to rephrase or seek help  
- Personality-driven catchphrases and educational tips  
- Responses tailored around crypto trends, sustainability scores, and investment advice

## Conversation Flow Diagram (Text)

Start
└──> Welcome Message
├──> "help" → Show Help Message
├──> Ask about coin → Check price + trend + sustainability
│ └──> Give advice based on logic
├──> Typo or unknown input → Error message
└──> "exit" → Goodbye Message

## File: `personality.py`

This Python module contains all chatbot responses and templates used to maintain consistent personality and tone.

Example functions include:  
- `welcome_message()`  
- `help_message()`  
- `error_message()`  
- `goodbye_message()`  
- `trend_response(trend)`  
- `sustainability_response(score)`

## Usage

The functions in `personality.py` are imported and called by the chatbot’s core logic (`chatbot_core.py`) to generate responses based on user input and data analysis.

## Contact

For questions regarding the personality design or response templates, contact Member 2.

*End of documentation for Chatbot Personality & Conversation Design*
