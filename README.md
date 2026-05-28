<div align="center">

# 💜 Alex & Luna — Safe Adolescent Health Assistant

### *A safe space to ask the questions you were too afraid to ask.*

> A safe, friendly AI for health, relationships, and wellbeing — judgment-free, inclusive, and crisis-aware.

🌐 **[View Live Demo](https://alex-luna-chatbot.streamlit.app/)**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)

</div>

---

## 🌍 The Problem It Solves

Many teenagers and young adults have nowhere safe to turn for sensitive health questions.

- Parents avoid the topic
- Schools provide limited sex education
- Google feels overwhelming
- Friends spread myths
- Pornography creates misinformation

**Alex & Luna** fills that gap — a friendly, emotionally intelligent AI that answers the questions you were too embarrassed to ask anywhere else.

---

## 💜 Meet the Personas

The heart of this project is its **multi-persona AI system** — each persona has a distinct tone, purpose, and audience.

**😎 Alex** — *The supportive older brother*
> For boys. Casual Gen-Z tone, funny, non-judgmental.
> Covers: puberty, body image, masturbation myths, porn addiction, consent, relationships, peer pressure

**🌸 Luna** — *The caring best friend*
> For girls. Warm, emotionally validating, comforting.
> Covers: periods, PCOS, body image, sexual safety, harassment, emotional wellbeing

**🌈 Any** — *The inclusive companion*
> For everyone. Gender-neutral, LGBTQ+ friendly.
> Covers: identity questions, emotional conversations, general safe guidance

---

## 🛡️ Safety First

Alex & Luna is built with a **3-level boundary system**:
Normal educational question   →   Answer normally
Curious / edge question       →   Answer safely + redirect
Explicit / inappropriate      →   Refuse politely

**Crisis Detection** — the system actively watches for signs of:
- Suicidal thoughts
- Abuse or assault
- Self-harm risk

When detected, it immediately shifts tone, provides emotional support, and shares helpline numbers (iCall India + mental health resources).

---

## 🧠 AI Features

```text
🎭  Persona-based prompting (Alex / Luna / Any)
🧭  Intent-aware routing
💬  Emotional tone adaptation
📚  Sexual health & puberty education
🚫  Myth busting (especially around pornography)
✅  Consent education
💔  Relationship & breakup guidance
🏥  STI awareness & safe sex guidance
🧠  Mental health support
🚨  Crisis escalation handling
```

---

## ⚙️ Tech Stack

| Layer | Tech |
|---|---|
| 🐍 Backend | Python |
| 🖥️ Frontend | Streamlit |
| ⚡ LLM Inference | Groq API (ultra-fast) |
| 🤖 AI Model | Llama 3 |
| 🔗 Orchestration | LangChain |
| 🔐 Config | dotenv |

---

## 🏗️ Architecture
User Input
↓
Persona Router  (Alex / Luna / Any)
↓
Safety Layer  (crisis detection + content filter)
↓
Groq LLM  (contextual response generation)
↓
Streamlit UI  (response displayed)

---

## 🗂️ Project Structure
alex-luna-chatbot/
├── app.py            # Streamlit frontend
├── llm.py            # Groq API integration
├── prompts.py        # Persona system prompts
├── router.py         # Persona routing logic
├── safety.py         # Safety & crisis filters
├── requirements.txt
├── .gitignore
└── .env

---

## 🎯 Who It's For

- Teenagers (13–19) with limited sex education
- Young adults (19–25) seeking safe guidance
- LGBTQ+ youth looking for inclusive support
- Anyone too uncomfortable to ask these questions openly

---

## 🔐 Disclaimer

Alex & Luna is an **educational and emotional support tool only.**
It does not replace licensed doctors, therapists, or emergency services.
Please seek professional help for serious medical or mental health concerns.

---

<div align="center">

*Built for the questions nobody talks about. Powered by AI. Driven by empathy.*

</div>
