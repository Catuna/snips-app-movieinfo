import tmdbsimple as tmdb

tmdb.API_KEY = '3f5e463e7b648ef4b2d6f884a81b044f'


def retrieveMovieCredits(movieId):
    creditsResponse = tmdb.Movies(movieId).credits()
    return creditsResponse


def retrieveMovieInfo(movieId):
    castResponse = tmdb.Movies(movieId).info()
    return castResponse


def retrieveMostRelevantMovieFromQuery(query):
    search = tmdb.Search()
    searchResponse = search.movie(query=query)

    if searchResponse['total_results'] == 0:
        return None
    return searchResponse['results'][0]


def retrieveRandomGoodMovieFromGenres(genres):
    raise Exception('Not implemented')
