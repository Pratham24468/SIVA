# ============================================
#   SIVA — Mini CLI Chatbot by EKA
#   Project 1: Loops, Conditions, Lists
# ============================================

chat_history = []
BOT_NAME = "SIVA"

print("=" * 40)
print(f"  {BOT_NAME} — EKA Mini Chatbot")
print("  Type 'quit' to exit")
print("=" * 40)
print()


def get_reply(user_input):
    msg = user_input.lower()

    if "hello" in msg or "hi" in msg or "hey" in msg:
        return "Hey! I'm SIVA. What's on your mind?"

    elif "who are you" in msg or "what are you" in msg:
        return "I'm SIVA — a mini version of the SIVRAJ architecture built by EKA."

    elif "your name" in msg:
        return f"My name is {BOT_NAME}. Short for SIVRAJ."

    elif "eka" in msg:
        return "EKA is building AGI, Hyperloop, and BioGrid. Big things coming."

    elif "agi" in msg or "sivraj" in msg:
        return "SIVRAJ is a 5-layer agentic AGI system. I'm just its tiny CLI sibling."

    elif "hyperloop" in msg:
        return "EKA Hyperloop targets 2,660 km/h using spiral electromagnetic propulsion. Insane, right?"

    elif "biogrid" in msg:
        return "EKA BioGrid converts organic waste to biomethane. Revenue potential: ₹770 crore network-wide."

    elif "mma" in msg:
        return "MMA is for warriors and you've done it for 6 days. Maintain the consistency and you will be one."

    elif "weather" in msg:
        return "I can't check weather yet — that's Project 2."

    elif "how are you" in msg:
        return "Running at full capacity. No bugs today — so far."

    elif "good morning" in msg or "good night" in msg or "good evening" in msg:
        return "Right back at you. Time means little to a bot, but I appreciate it."

    elif "thank" in msg:
        return "No problem. That's what I'm here for."

    elif "help" in msg:
        return "Try asking me about EKA, AGI, Hyperloop, BioGrid, MMA, or just say hi."

    elif "history" in msg or "what did i say" in msg:
        if len(chat_history) == 0:
            return "You haven't said anything yet."
        else:
            summary = "Here's our conversation so far:\n"
            for i, entry in enumerate(chat_history):
                summary += f"  {i+1}. You: {entry}\n"
            return summary

    # --- FIXED: last message ---
    elif "last message" in msg or "last msg" in msg:
        if len(chat_history) == 0:
            return "You haven't said anything yet."
        else:
            return f"Your last message was: '{chat_history[-1]}'"

    elif "how many" in msg and "message" in msg:
        count = len(chat_history)
        return f"You've sent {count} message(s) so far."

    else:
        return "Hmm, I don't have a response for that yet. Ask me about EKA or say 'help'."


while True:
    user_input = input("You: ").strip()

    if user_input == "":
        continue

    if user_input.lower() == "quit":
        print(f"\n{BOT_NAME}: Shutting down. Total messages: {len(chat_history)}. Stay building.")
        break

    chat_history.append(user_input)
    reply = get_reply(user_input)
    print(f"{BOT_NAME}: {reply}")
    print()
