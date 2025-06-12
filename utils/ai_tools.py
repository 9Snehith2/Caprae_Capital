from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    if not text:
        return "No description available."

    try:
        result = summarizer(text, max_length=60, min_length=20, do_sample=False)
        return result[0]["summary_text"]
    except Exception:
        return "AI summarization failed."

def categorize_company(text):
    if not text:
        return "Uncategorized"
    if any(kw in text.lower() for kw in ["cloud", "platform", "infrastructure"]):
        return "Cloud Services"
    elif any(kw in text.lower() for kw in ["training", "simulation", "education"]):
        return "EdTech / Simulation"
    elif any(kw in text.lower() for kw in ["invoice", "payments", "analytics"]):
        return "FinTech / Automation"
    return "General Tech"

def score_lead(company):
    try:
        employees = int(company.get("Employees", 0))
        revenue_text = company.get("Revenue", "").replace("$", "").replace(",", "")
        revenue = int(revenue_text) if revenue_text.isdigit() else 0

        if revenue > 1000000 and employees > 100:
            return ("🔥 High", "Large team and strong revenue indicates high-value opportunity.")
        elif employees > 30:
            return ("⚖️ Medium", "Moderate team size; possible growth-stage company.")
        else:
            return ("❄️ Low", "Small scale operation; might not be an ideal target.")

    except Exception:
        return ("❓ Unknown", "Insufficient data for scoring.")
