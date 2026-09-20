# ================================================================
# PROJECT 3: AI RECOMMENDATION LOGIC
# DecodeLabs - Personalization Phase
# ================================================================

print("=" * 72)
print("|                AI RECOMMENDATION ENGINE                       |")
print("|              DecodeLabs - Project 3                            |")
print("=" * 72)

print("\nThis system recommends movies based on your preferences.")
print("Your choices are compared with movie attributes using")
print("a simple similarity scoring system.")

print("=" * 72)


# ------------------------------------------------
# Movie Dataset
# ------------------------------------------------

movies = [
    {
        "title": "The Dark Knight",
        "genre": "action",
        "language": "english",
        "mood": "exciting"
    },
    {
        "title": "Inception",
        "genre": "science fiction",
        "language": "english",
        "mood": "mind-bending"
    },
    {
        "title": "Interstellar",
        "genre": "science fiction",
        "language": "english",
        "mood": "emotional"
    },
    {
        "title": "Avengers: Endgame",
        "genre": "action",
        "language": "english",
        "mood": "exciting"
    },
    {
        "title": "The Notebook",
        "genre": "romance",
        "language": "english",
        "mood": "romantic"
    },
    {
        "title": "Parasite",
        "genre": "thriller",
        "language": "korean",
        "mood": "suspenseful"
    },
    {
        "title": "Your Name",
        "genre": "romance",
        "language": "japanese",
        "mood": "emotional"
    },
    {
        "title": "The Hangover",
        "genre": "comedy",
        "language": "english",
        "mood": "funny"
    },
    {
        "title": "Get Out",
        "genre": "horror",
        "language": "english",
        "mood": "suspenseful"
    },
    {
        "title": "Spider-Man: No Way Home",
        "genre": "action",
        "language": "english",
        "mood": "exciting"
    }
]


# ------------------------------------------------
# Display available preferences
# ------------------------------------------------

print("\nAVAILABLE PREFERENCES")
print("-" * 72)

print("| Genres:")
print("| action")
print("| science fiction")
print("| romance")
print("| thriller")
print("| comedy")
print("| horror")

print("\n| Languages:")
print("| english")
print("| korean")
print("| japanese")

print("\n| Moods:")
print("| exciting")
print("| mind-bending")
print("| emotional")
print("| romantic")
print("| suspenseful")
print("| funny")

print("=" * 72)


# ------------------------------------------------
# Get user preferences
# ------------------------------------------------

print("\nENTER YOUR PREFERENCES")
print("-" * 72)

user_genre = input("| What genre do you prefer? ").lower().strip()

user_language = input("| What language do you prefer? ").lower().strip()

user_mood = input("| What mood are you looking for? ").lower().strip()

print("=" * 72)


# ------------------------------------------------
# Calculate similarity score
# ------------------------------------------------

recommendations = []

for movie in movies:

    score = 0
    matched_preferences = []

    # Genre match
    if user_genre == movie["genre"]:
        score += 40
        matched_preferences.append("genre")

    # Language match
    if user_language == movie["language"]:
        score += 30
        matched_preferences.append("language")

    # Mood match
    if user_mood == movie["mood"]:
        score += 30
        matched_preferences.append("mood")

    recommendations.append(
        {
            "title": movie["title"],
            "score": score,
            "matches": matched_preferences
        }
    )


# ------------------------------------------------
# Sort recommendations
# ------------------------------------------------

recommendations.sort(
    key=lambda movie: movie["score"],
    reverse=True
)


# ------------------------------------------------
# Display recommendations
# ------------------------------------------------

print("\nAI RECOMMENDATIONS")
print("=" * 72)

top_recommendations = recommendations[:5]

for position, movie in enumerate(top_recommendations, start=1):

    print(f"| {position}. {movie['title']}")
    print(f"|    Similarity Score: {movie['score']}%")

    if movie["matches"]:
        print(
            f"|    Matched preferences: "
            f"{', '.join(movie['matches'])}"
        )
    else:
        print("|    Matched preferences: None")

    print("|")


# ------------------------------------------------
# Recommendation explanation
# ------------------------------------------------

best_match = recommendations[0]

print("=" * 72)
print("| TOP RECOMMENDATION")
print("=" * 72)

print(f"| Movie : {best_match['title']}")
print(f"| Score : {best_match['score']}%")

if best_match["matches"]:
    print(
        "| Reason: This movie matches your "
        + ", ".join(best_match["matches"])
        + "."
    )
else:
    print("| Reason: No direct preference matches were found.")

print("=" * 72)

print("\nRecommendation process completed.")
print("Thank you for using the AI Recommendation Engine!")
print("=" * 72)