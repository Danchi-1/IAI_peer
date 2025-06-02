# CryptoBuddy - AI-Powered Cryptocurrency Advisor 💰🌱

## 📌 Overview
CryptoBuddy is a rule-based chatbot designed to help users analyze cryptocurrency investment options based on **profitability** (price trends) and **sustainability** (energy efficiency and eco-friendliness). 

This chatbot enables informed financial decisions while promoting sustainable crypto choices. It leverages predefined data alongside real-time updates via the **CoinMarketCap API**.

---

## 🎯 Features
✅ **Real-Time Crypto Data** – Fetches latest prices and market caps using CoinMarketCap API.  
✅ **Sustainability Scoring** – Evaluates eco-friendliness based on energy usage and consensus mechanisms.  
✅ **Smart Investment Advice** – Recommends cryptocurrencies based on profitability and sustainability balance.  
✅ **Data Validation** – Ensures accuracy and integrity in crypto insights using validation logic.  
✅ **Industry-Standard Error Handling** – Protects against API failures and faulty data.  
✅ **JSON & CSV Export** – Saves structured crypto insights for future reference.  

---

## 🚀 Installation Guide
### **1. Clone the Repository**
```bash
git clone https://github.com/your-repo/cryptobuddy.git
cd cryptobuddy
2. Set Up Environment
Install dependencies:

bash
pip install -r requirements.txt
Set up API key (replace "your_api_key" with an actual CoinMarketCap API key):

bash
export COINMARKETCAP_API_KEY="your_api_key"
Or on Windows:

powershell
set COINMARKETCAP_API_KEY="your_api_key"
3. Run CryptoBuddy
Execute the chatbot:

bash
python main.py
🧩 Project Structure
├── CryptoBuddy/
│   ├── main.py             # Fetches & processes cryptocurrency data
│   ├── chatbot_core.py     # Handles chatbot responses
│   ├── data_validator.py   # Validates and updates crypto energy usage
│   ├── ui_handle.py        # Manages interactive chatbot loop
│   ├── test_chatbot.py     # Unit tests for chatbot logic
│   ├── test_data_validator.py # Unit tests for crypto validation
│   ├── requirements.txt    # Required libraries & dependencies
│   ├── readme.md           # Project documentation (this file)
│   ├── crypto_db.json      # Saved crypto data in JSON format
│   ├── crypto_db.csv       # Saved crypto data in CSV format
🔍 Lessons Learned
✅ Successes
Designed an effective AI-driven chatbot using structured rule-based logic.

Ensured data integrity using real-time validation and fallback mechanisms.

Implemented secure API handling using environment variables instead of hardcoding sensitive data.

Optimized chatbot query processing and investment logic for better user experience.

❌ Challenges
API request failures required robust error handling to prevent crashes.

Sustainability scoring was subjective, requiring manual refinement of eco-friendly ranking logic.

File exporting initially had formatting errors—fixed by standardizing CSV output structure.

🛠️ Future Improvements
🔹 Live Energy Data – Pull real-time network consumption data instead of manual estimates. 🔹 Improved NLP – Enhance chatbot responses using NLP frameworks like NLTK for natural language understanding. 🔹 Personalized Investment Profiles – Allow users to set preferences for risk tolerance, growth strategy, or sustainability bias. 🔹 Multilingual Support – Enable queries and responses in multiple languages for global accessibility. 🔹 Mobile-Friendly UI – Develop a lightweight web or mobile app interface for seamless interactions.

💡 Conclusion
CryptoBuddy showcases the power of AI-driven financial assistants by offering structured investment advice while promoting eco-conscious cryptocurrency adoption. Whether you're a beginner investor or a sustainability advocate, CryptoBuddy helps you make informed decisions. 🚀🌍

Feel free to contribute, suggest improvements, or fork the project. Let’s build smarter financial tools together! 💰✨

📩 Contact & Contributions
Pull requests are welcome! For feedback or inquiries, contact: 
Daniel Ohachor: ohachordaniel2021@gmail.com
ZebidahM: zebidahm@gmail.com
Israel Oluwaseyi: oluwaseyiisrael2@gmail.com
Dominik Kean: ilsaoltactaiocht@gmail.com
