# Item-Based Recommendation System
dataset = {
    "action" : ["matrix","batman","superman","dabang","avengers","thor","hulk","krrish","ironman"],
    "comedy" : ["the mask","dhamaal","bala","housefull","golmaal","hera pheri","golmaal 2","dhamaal 2","hera pheri 2"],
    "drama" : ["dabang","krrish","hera pheri","bala","kahani","batla house","kgf","zero","sultan"],
    "thriller" : ["kahani","kgf","batla house","madras cafe","uri","raw","lucy","the ring","oculus"],
    "horror" : ["oculus","the ring","it","the ring 2","evil dead","conjuring","conjuring 2","bhootnath","aatma"]
}

user = {'batman','kgf','bala','thor','kahani','lucy','raw','uri'}
scores = {}
for key in dataset:
    movies = set(dataset[key])
    numer = len(movies.intersection(user))
    denom = len(movies.union(user))

    sim = numer / denom
    scores[key] = round(sim,2)

print(scores)

cat = max(scores.items(), key=lambda y : y[1])[0]

recommended = set(dataset[cat]) - user
print("Recommended Movies",recommended)

