scores = {
    "Russia": {
        "ribbon": {
            "difficulty": 9.100,
            "execution": 9.400,
        },
        "hoop": {
            "difficulty": 9.300,
            "execution": 9.800,
        },
        "rope": {
            "difficulty": 9.600,
            "execution": 9.000,
        },
    },
    "Bulgaria": {
        "ribbon": {
            "difficulty": 9.600,
            "execution": 9.400,
        },
        "hoop": {
            "difficulty": 9.550,
            "execution": 9.750,
        },
        "rope": {
            "difficulty": 9.500,
            "execution": 9.400,
        },
    },
    "Italy": {
        "ribbon": {
            "difficulty": 9.200,
            "execution": 9.500,
        },
        "hoop": {
            "difficulty": 9.450,
            "execution": 9.350,
        },
        "rope": {
            "difficulty": 9.700,
            "execution": 9.150,
        },
    },
}

country = input()  # "Russia", "Bulgaria", or "Italy"
performance = input()  # "ribbon", "hoop", or "rope"

score = scores[country][performance]["difficulty"] + scores[country][performance]["execution"]
max_score = 20.000
percent_to_max_score = (max_score - score) / max_score

print(f"The team of {country} get {score :.3f} on {performance}.")
print(f"{percent_to_max_score :.2%}")
