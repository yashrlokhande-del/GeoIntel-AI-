WEIGHTS = {
    "security": 0.25,
    "political": 0.15,
    "diplomatic": 0.15,
    "economic": 0.15,
    "social": 0.10,
    "strategic": 0.20,
}

def _clamp(value):
    return max(0.0, min(100.0, float(value)))

def calculate_risk(scores):
    """Return a weighted 0–100 risk score."""
    total = sum(_clamp(scores.get(k, 0)) * w for k, w in WEIGHTS.items())
    return round(total, 1)

def dimension_contributions(scores):
    return {
        k: round(_clamp(scores.get(k, 0)) * w, 2)
        for k, w in WEIGHTS.items()
    }

def risk_level(score):
    score = float(score)
    if score <= 20:
        return "VERY LOW"
    if score <= 40:
        return "LOW"
    if score <= 60:
        return "MODERATE"
    if score <= 80:
        return "HIGH"
    return "CRITICAL"
