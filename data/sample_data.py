# Demonstration data only. Replace with validated datasets in the data-ingestion phase.

COUNTRIES = {
    "India": {
        "security": 55,
        "political": 35,
        "diplomatic": 45,
        "economic": 30,
        "social": 25,
        "strategic": 60,
    },
    "China": {
        "security": 65,
        "political": 40,
        "diplomatic": 55,
        "economic": 45,
        "social": 30,
        "strategic": 75,
    },
    "Pakistan": {
        "security": 70,
        "political": 65,
        "diplomatic": 60,
        "economic": 70,
        "social": 55,
        "strategic": 65,
    },
    "United States": {
        "security": 35,
        "political": 30,
        "diplomatic": 25,
        "economic": 20,
        "social": 25,
        "strategic": 55,
    },
    "Russia": {
        "security": 60,
        "political": 55,
        "diplomatic": 50,
        "economic": 55,
        "social": 45,
        "strategic": 70,
    },
    "Japan": {
        "security": 30,
        "political": 20,
        "diplomatic": 25,
        "economic": 25,
        "social": 20,
        "strategic": 45,
    },
}

RELATIONSHIPS = {
    tuple(sorted(("China", "India"))): {
        "type": "STRATEGIC_COMPETITION",
        "modifier": 18,
        "description": "Demo relationship profile representing strategic competition, unresolved territorial issues, and economic interdependence.",
    },
    tuple(sorted(("India", "Pakistan"))): {
        "type": "ADVERSARIAL",
        "modifier": 24,
        "description": "Demo relationship profile representing persistent security competition and historical disputes.",
    },
    tuple(sorted(("India", "United States"))): {
        "type": "STRATEGIC_PARTNERSHIP",
        "modifier": -12,
        "description": "Demo relationship profile representing strategic cooperation and defence/economic ties.",
    },
    tuple(sorted(("India", "Russia"))): {
        "type": "STRATEGIC_PARTNERSHIP",
        "modifier": -5,
        "description": "Demo relationship profile representing longstanding defence and strategic ties.",
    },
    tuple(sorted(("China", "United States"))): {
        "type": "GREAT_POWER_COMPETITION",
        "modifier": 20,
        "description": "Demo relationship profile representing sustained strategic, economic, and technological competition.",
    },
    tuple(sorted(("India", "Japan"))): {
        "type": "STRATEGIC_PARTNERSHIP",
        "modifier": -10,
        "description": "Demo relationship profile representing strategic cooperation in the Indo-Pacific.",
    },
}
