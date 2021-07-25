dataset = {
    "action" : ["matrix","batman","superman","dabang","avengers","thor","hulk","krrish","ironman"],
    "comedy" : ["the mask","dhamaal","bala","housefull","golmaal","hera pheri","golmaal 2","dhamaal 2","hera pheri 2"],
    "drama" : ["dabang","krrish","hera pheri","bala","kahani","batla house","kgf","zero","sultan"],
    "thriller" : ["kahani","kgf","batla house","madras cafe","uri","raw","lucy","the ring","oculus"],
    "horror" : ["oculus","the ring","it","the ring 2","evil dead","conjuring","conjuring 2","bhootnath","aatma"]
}

user_1 = {'batman','kgf','bala','thor','kahani','lucy','raw','uri'}
user_2 = {'matrix','batman','kgf','thor','raw','batla house','the ring','golmaal'}

# 1. Find sim movies of user_1 and user_2
# 2. Find Similarity Score of sim movies with all the genres
# 3. Get the category name which is most common b/w both users
# 4. Recommend movies from user_2 of that category to user_1 that he has not watched yet...

simMovies = user_1.intersection(user_2)
print(simMovies)

scores = {}
for key in dataset:
    movies = dataset[key]
    numer = len(simMovies.intersection((set(movies))))
    denom = len(simMovies.union((set(movies))))
    simScore = numer/denom
    scores[key] = simScore

print(scores)



