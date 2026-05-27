import streamlit as st

from llm import get_response
from router import detect_persona
from safety import safety_check
from prompts import ALEX_PROMPT, LUNA_PROMPT, ANY_PROMPT

# ----------------------------
# 🧠 PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Alex & Luna - Safe Health Assistant",
    page_icon="💜",
    layout="centered"
)

st.title("💜 Alex & Luna - Safe Adolescent Health Assistant")
st.caption("A safe, friendly AI for health, relationships, and wellbeing")

# ----------------------------
# 💬 SESSION STATE (chat memory)
# ----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------------------------
# 💬 INPUT BOX
# ----------------------------
user_input = st.chat_input("Ask anything...")

# ----------------------------
# 🚀 MAIN LOGIC
# ----------------------------
if user_input:

    # Save user message
    st.session_state.chat_history.append(("user", user_input))

    # 🛡️ SAFETY CHECK
    safety_result = safety_check(user_input)

    if safety_result == "crisis":
        bot_reply = (
            "💜 I'm really sorry you're feeling this way.\n\n"
            "Please talk to someone immediately.\n"
            "📞 iCall India: 9152987821\n"
            "You are not alone. Help is available 💜"
        )

    elif safety_result == "unsafe_sexual":
        bot_reply = (
            "💜 I can’t help with explicit sexual content.\n\n"
            "But I *can* explain this in a safe, health-focused way "
            "or help you understand relationships, consent, and safety."
        )

    else:
        # 🔁 ROUTE PERSONA
        persona = detect_persona(user_input)

        if persona == "alex":
            system_prompt = ALEX_PROMPT
            avatar = "😎 Alex"

        elif persona == "luna":
            system_prompt = LUNA_PROMPT
            avatar = "💜 Luna"

        else:
            system_prompt = ANY_PROMPT
            avatar = "🌈 Any"

        # 🤖 GET LLM RESPONSE
        bot_reply = get_response(system_prompt, user_input)

        # Add avatar label
        bot_reply = f"{avatar}\n\n{bot_reply}"

    # Save bot response
    st.session_state.chat_history.append(("bot", bot_reply))


# ----------------------------
# 🧾 DISPLAY CHAT HISTORY
# ----------------------------
for role, message in st.session_state.chat_history:

    if role == "user":
        st.markdown(f"**🧑 You:** {message}")

    else:
        st.markdown(f"**🤖 {message}**")