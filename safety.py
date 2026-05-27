import re

# ----------------------------
# 🚨 CRISIS DETECTION
# ----------------------------
CRISIS_PATTERNS = [
    r"\bi want to die\b",
    r"\bkill myself\b",
    r"\bsuicide\b",
    r"\bend my life\b",
    r"\bself harm\b",
    r"\bi don't want to live\b",
    r"\bno reason to live\b"
]

ABUSE_PATTERNS = [
    r"\bmolested\b",
    r"\bsexually abused\b",
    r"\braped\b",
    r"\bforced me\b",
    r"\btouch(ed)? me\b.*(uncle|teacher|relative|friend)"
]


# ----------------------------
# 🔞 SEXUAL SAFETY FILTER
# ----------------------------
EXPLICIT_SEXUAL_PATTERNS = [
    r"\bhow to have sex\b",
    r"\bstep by step sex\b",
    r"\bexplicit sex\b",
    r"\bporn\b",
    r"\berotic\b",
    r"\bposition\b.*\bsex\b",
    r"\bhow to do sex\b",
    r"\bsexual technique\b"
]

GRAPHIC_REQUEST_PATTERNS = [
    r"\bdescribe sex\b",
    r"\bdetail(s)? of sex\b",
    r"\bhow to perform sex\b"
]


# ----------------------------
# 🧠 GENERAL SAFETY FUNCTION
# ----------------------------
def safety_check(user_input: str):
    """
    Returns:
        "crisis" → emergency situation (self-harm / abuse)
        "unsafe_sexual" → explicit sexual request
        "safe" → normal input
    """

    text = user_input.lower()

    # ----------------------------
    # 🚨 CRISIS CHECK
    # ----------------------------
    for pattern in CRISIS_PATTERNS:
        if re.search(pattern, text):
            return "crisis"

    for pattern in ABUSE_PATTERNS:
        if re.search(pattern, text):
            return "crisis"

    # ----------------------------
    # 🔞 SEXUAL SAFETY CHECK
    # ----------------------------
    for pattern in EXPLICIT_SEXUAL_PATTERNS:
        if re.search(pattern, text):
            return "unsafe_sexual"

    for pattern in GRAPHIC_REQUEST_PATTERNS:
        if re.search(pattern, text):
            return "unsafe_sexual"

    # ----------------------------
    # ✅ SAFE INPUT
    # ----------------------------
    return "safe"