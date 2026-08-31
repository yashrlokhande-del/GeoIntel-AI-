def _normalise(values):
    total = sum(values)
    return [round(v * 100 / total) for v in values]

def generate_scenarios(overall_risk, relationship):
    modifier = relationship.get("modifier", 0)

    # Demo heuristic. Replace with a trained/calibrated forecasting model later.
    escalation_raw = max(5, 12 + overall_risk * 0.18 + max(modifier, 0) * 0.2)
    deescalation_raw = max(10, 30 - overall_risk * 0.12 - max(modifier, 0) * 0.05)
    baseline_raw = max(10, 100 - escalation_raw - deescalation_raw)

    probs = _normalise([baseline_raw, escalation_raw, deescalation_raw])

    return [
        {
            "name": "Baseline — Managed Competition",
            "probability": probs[0],
            "impact": round(overall_risk * 0.75),
            "description": "Current strategic competition continues without a major discontinuity.",
            "indicators": ["stable military channels", "continued trade", "routine diplomacy"],
        },
        {
            "name": "Escalation",
            "probability": probs[1],
            "impact": min(100, round(overall_risk + 25)),
            "description": "A sequence of adverse events increases political, military, or diplomatic pressure.",
            "indicators": ["military mobilisation", "new sanctions", "communication breakdown", "border incidents"],
        },
        {
            "name": "De-escalation",
            "probability": probs[2],
            "impact": max(0, round(overall_risk - 25)),
            "description": "Diplomatic engagement and confidence-building measures reduce immediate tensions.",
            "indicators": ["new dialogue", "military disengagement", "trade normalisation", "joint statements"],
        },
    ]
