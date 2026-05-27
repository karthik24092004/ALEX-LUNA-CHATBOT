def detect_persona(user_input: str) -> str:
    """
    Routes user query to Alex, Luna, or Any persona.

    Returns:
        "alex" | "luna" | "any"
    """

    text = user_input.lower()

    # ----------------------------
    # 💜 LUNA (female / reproductive / emotional body topics)
    # ----------------------------
    luna_keywords = [
        "period", "periods", "menstruation", "cramps",
        "pregnant", "pregnancy", "vagina", "vaginal",
        "breast", "breasts", "discharge",
        "pcos", "gynecologist", "gyno",
        "tampon", "pad", "sanitary",
        "female", "girl", "girlhood"
    ]

    if any(word in text for word in luna_keywords):
        return "luna"

    # ----------------------------
    # 😎 ALEX (male puberty / sexual curiosity / grooming)
    # ----------------------------
    alex_keywords = [
        "penis", "balls", "testicle", "testicles",
        "masturbate", "masturbation",
        "erection", "condom", "sex",
        "sperm", "semen",
        "porn", "orgasm",
        "grooming", "shaving",
        "boy", "male"
    ]

    if any(word in text for word in alex_keywords):
        return "alex"

    # ----------------------------
    # 🌈 ANY (default: relationships, mental health, consent, identity)
    # ----------------------------
    any_keywords = [
        "consent", "relationship", "girlfriend", "boyfriend",
        "breakup", "love", "crush",
        "anxiety", "depression", "stress",
        "suicide", "kill myself",
        "lgbt", "gay", "lesbian", "bi",
        "peer pressure", "friends"
    ]

    if any(word in text for word in any_keywords):
        return "any"

    # ----------------------------
    # DEFAULT FALLBACK
    # ----------------------------
    return "any"