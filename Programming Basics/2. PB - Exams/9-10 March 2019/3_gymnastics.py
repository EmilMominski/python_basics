# Data Input
country = input()    # Russia, Bulgaria and Italy
equipment = input()    # ribbon, hoop and rope

# Logic
if country == "Russia":
    if equipment == "ribbon":
        score_difficulty = 9.1
        score_performance = 9.4
    elif equipment == "hoop":
        score_difficulty = 9.3
        score_performance = 9.8
    elif equipment == "rope":
        score_difficulty = 9.6
        score_performance = 9.0
elif country == "Bulgaria":
    if equipment == "ribbon":
        score_difficulty = 9.6
        score_performance = 9.4
    elif equipment == "hoop":
        score_difficulty = 9.55
        score_performance = 9.75
    elif equipment == "rope":
        score_difficulty = 9.5
        score_performance = 9.4
elif country == "Italy":
    if equipment == "ribbon":
        score_difficulty = 9.2
        score_performance = 9.5
    elif equipment == "hoop":
        score_difficulty = 9.45
        score_performance = 9.35
    elif equipment == "rope":
        score_difficulty = 9.7
        score_performance = 9.15
score = score_difficulty + score_performance
percent = 100 * (1 - score / 20)

# Print Output
print(f"The team of {country} get {score:.3f} on {equipment}.")
print(f"{percent:.2f}%")
