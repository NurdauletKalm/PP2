def ok1(m):
    return m['imdb'] > 5.5

def ok2(m):
    return [x for x in m if x['imdb'] > 5.5]

def ok3(m, c):
    return [x for x in m if x['category'] == c]

def ok4(m):
    if not m:
        return 0
    return sum(x['imdb'] for x in m) / len(m)

def ok5(m, c):
    return ok4(ok3(m, c))

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

print(ok1(movies[0]))
# print(ok2(movies))
# print(ok3(movies, 'Romance'))
# print(ok4(movies))
# print(ok5(movies, 'Romance'))