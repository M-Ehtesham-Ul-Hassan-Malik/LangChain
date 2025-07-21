from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
import random
import time

# Dummy movie database
MOVIES = [
    {"title": "Inception", "genre": "Sci-Fi", "actors": ["Leonardo DiCaprio"], "rating": 8.8},
    {"title": "The Matrix", "genre": "Sci-Fi", "actors": ["Keanu Reeves"], "rating": 8.7},
    {"title": "The Godfather", "genre": "Crime", "actors": ["Marlon Brando", "Al Pacino"], "rating": 9.2},
    {"title": "Titanic", "genre": "Romance", "actors": ["Leonardo DiCaprio", "Kate Winslet"], "rating": 7.9},
    {"title": "Gladiator", "genre": "Action", "actors": ["Russell Crowe"], "rating": 8.5},
    {"title": "Pulp Fiction", "genre": "Crime", "actors": ["John Travolta", "Samuel L. Jackson"], "rating": 8.9},
    {"title": "La La Land", "genre": "Musical", "actors": ["Ryan Gosling", "Emma Stone"], "rating": 8.0},
    {"title": "Interstellar", "genre": "Sci-Fi", "actors": ["Matthew McConaughey", "Anne Hathaway"], "rating": 8.6},
    {"title": "The Notebook", "genre": "Romance", "actors": ["Ryan Gosling", "Rachel McAdams"], "rating": 7.8},
    {"title": "The Dark Knight", "genre": "Action", "actors": ["Christian Bale", "Heath Ledger"], "rating": 9.0}
]

# Welcome Message
def welcome():
    print("🎬 Welcome to the Movie Recommender CLI App 🎬")
    print("-" * 50)
    time.sleep(1)

# Get user preferences
def get_user_preferences():
    genres = input("Enter your favorite genres (comma-separated): ").lower().split(",")
    actors = input("Enter your favorite actors (comma-separated): ").lower().split(",")
    try:
        min_rating = float(input("Minimum IMDb rating you prefer (e.g., 7.5): "))
    except ValueError:
        min_rating = 0.0
        print("Invalid input. Defaulting to 0.0 rating.")
    
    return [g.strip() for g in genres], [a.strip() for a in actors], min_rating

# Recommend movies based on preferences
def recommend_movies(genres, actors, min_rating):
    print("\n🔍 Searching for the best movies for you...\n")
    time.sleep(2)

    recommended = []
    for movie in MOVIES:
        if movie["rating"] >= min_rating:
            genre_match = movie["genre"].lower() in genres
            actor_match = any(actor.lower() in actors for actor in movie["actors"])
            if genre_match or actor_match:
                recommended.append(movie)

    if not recommended:
        print("😢 Sorry, no movies match your preferences.")
    else:
        print("🎯 Recommended Movies:")
        for idx, movie in enumerate(recommended, 1):
            print(f"{idx}. {movie['title']} ({movie['genre']}) - ⭐ {movie['rating']}")
            print(f"   Cast: {', '.join(movie['actors'])}")
            print("-" * 40)

# Main application loop
def main():
    welcome()
    while True:
        genres, actors, min_rating = get_user_preferences()
        recommend_movies(genres, actors, min_rating)
        again = input("\nWould you like another recommendation? (y/n): ").lower()
        if again != 'y':
            print("\n👋 Thanks for using Movie Recommender CLI App. Happy watching!")
            break
        print("\n" + "="*50 + "\n")

# Entry point
if __name__ == "__main__":
    main()

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=500,
    # chunk_overlap=200, 
)

result = splitter.split_text(text)

print(result)
print()
print(len(result))
print()
print(result[2])


