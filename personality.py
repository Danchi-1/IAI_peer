# personality.py

def welcome_message():
    return (
        "👋 Hello! I'm CryptoBuddy, your AI-powered crypto sidekick!\n"
        "Ask me about any cryptocurrency and I’ll give you insights based on price trends 📈 and sustainability 🔋.\n"
        "Type 'help' to see what I can do or 'exit' to leave."
    )

def help_message():
    return (
        "🆘 Here's what I can help you with:\n"
        "- Ask me about a cryptocurrency (e.g., 'Tell me about Bitcoin')\n"
        "- I’ll give you advice based on recent price trends and sustainability\n"
        "- Type 'exit' to end our chat\n"
        "Ready when you are! 🚀"
    )

def goodbye_message():
    return "👋 Thanks for chatting with CryptoBuddy! Stay savvy and sustainable out there! 💰🌱"

def error_message():
    return (
        "😕 Oops! I didn't catch that. You can try asking about a coin or type 'help' for options."
    )

def trend_response(trend):
    if trend == "up":
        return "📈 This coin is on an upward trend! Now might be a good time to look into it."
    elif trend == "down":
        return "📉 Looks like it's dipping. Might want to wait or proceed cautiously."
    elif trend == "stable":
        return "➖ The trend is stable right now. Consider your goals before investing."
    else:
        return "🤷‍♂️ I couldn't determine the trend right now. Try again later."

def sustainability_response(score):
    if score >= 8:
        return "🌿 Highly sustainable project! Backed by strong eco-friendly and technical fundamentals."
    elif score >= 5:
        return "♻️ Moderately sustainable. Not bad, but could be better."
    else:
        return "⚠️ Low sustainability score. Do your research before investing."
