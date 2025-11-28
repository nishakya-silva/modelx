import sys
import re

# --- CONFIGURATION: CATEGORIES & KEYWORDS ---

INDUSTRIES = {
    "Agriculture": ["farming", "livestock", "forestry", "rice", "paddy", "fertilizer", "tea", "coconut", "rubber", "harvest", "farmers", "fisheries"],
    "Manufacturing": ["factory", "production", "garment", "apparel", "industrial", "textile", "export", "manufacturing", "assembly"],
    "Construction": ["building", "infrastructure", "cement", "housing", "road", "highway", "bridge", "development project", "construction"],
    "Energy": ["oil", "gas", "renewable", "solar", "wind", "mining", "fuel", "petrol", "diesel", "power", "electricity", "ceb", "cpc", "energy"],
    "Retail": ["shops", "supermarket", "mall", "price", "consumer", "buying", "selling", "market", "retail", "e-commerce"],
    "Transportation & Logistics": ["airlines", "shipping", "trucking", "transport", "bus", "train", "railway", "flight", "cargo", "port", "logistics"],
    "Technology": ["software", "hardware", "it", "internet", "cyber", "digital", "ai", "app", "platform", "tech"],
    "Telecommunications": ["phone", "network", "broadband", "data", "5g", "telecom", "dialog", "mobitel", "slt", "signal"],
    "Finance & Banking": ["bank", "insurance", "investment", "stock", "cse", "rupee", "dollar", "tax", "loan", "interest rate", "cbsl", "imf", "economy"],
    "Real Estate": ["land", "property", "renting", "housing market", "apartment", "real estate"],
    "Healthcare": ["hospital", "pharmaceutical", "medicine", "doctor", "health", "virus", "disease", "medical", "clinic"],
    "Education": ["school", "university", "training", "exam", "student", "campus", "education", "teacher"],
    "Tourism & Hospitality": ["hotel", "travel", "restaurant", "resort", "tourist", "visa", "hospitality", "booking"],
    "Entertainment & Media": ["movie", "music", "cricket", "sports", "match", "cinema", "concert", "media", "news"]
}

# Major Districts & Cities in Sri Lanka
LOCATIONS = [
    "Colombo", "Gampaha", "Kandy", "Galle", "Jaffna", "Matara", "Kurunegala", 
    "Anuradhapura", "Trincomalee", "Batticaloa", "Badulla", "Nuwara Eliya", 
    "Ratnapura", "Hambantota", "Negombo", "Kalutara", "Island-wide"
]

# Risk & Advice Mapping (From previous step)
ADVICE_MAPPING = {
    "fuel": "⛽ Activate WFH & secure diesel backup.",
    "power": "⚡ Shift production to off-peak hours.",
    "strike": "📢 Arrange private transport for staff.",
    "protest": "🛡️ Avoid logistics routes near protest zones.",
    "curfew": "🛑 Issue essential service letters.",
    "tax": "📉 Consult finance on pricing impact."
}

def analyze_news(text):
    text_lower = text.lower()
    
    # 1. DETECT INDUSTRY
    detected_industry = "General / Other"
    for category, keywords in INDUSTRIES.items():
        if any(k in text_lower for k in keywords):
            detected_industry = category
            break # Stop at first match (or remove break to allow multiple)

    # 2. DETECT LOCATION
    detected_location = "National / Unspecified"
    for loc in LOCATIONS:
        if loc.lower() in text_lower:
            detected_location = loc
            break
            
    # 3. DETECT TIMELINE
    timeline = "Immediate / Ongoing"
    if "tomorrow" in text_lower or "next week" in text_lower:
        timeline = "Upcoming (Future)"
    elif "yesterday" in text_lower or "past" in text_lower:
        timeline = "Historical (Past)"
        
    # 4. DETECT RISKS & ADVICE
    risk_keywords = ["strike", "shortage", "protest", "curfew", "power cut", "fuel", "tax", "inflation", "crisis"]
    found_risks = [word for word in risk_keywords if word in text_lower]
    
    status = "⚠️ Risk Detected" if found_risks else "✅ Normal"
    
    advice_list = []
    if found_risks:
        for risk in found_risks:
            for key in ADVICE_MAPPING:
                if key in risk:
                    advice_list.append(ADVICE_MAPPING[key])
    
    # Return a dictionary object for cleaner access
    return {
        "status": status,
        "risks": found_risks,
        "advice": list(set(advice_list)),
        "industry": detected_industry,
        "location": detected_location,
        "timeline": timeline
    }

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    # Test
    print(analyze_news("Farmers in Anuradhapura protest over fertilizer shortage today"))