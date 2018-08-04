import tmdbsimple as tmdb

tmdb.API_KEY = '3f5e463e7b648ef4b2d6f884a81b044f'


def retrieveMostRelevantMediaFromQuery(query):
    search = tmdb.Search()
    searchResponse = search.movie(query=query)

    if searchResponse['total_results'] == 0:
        return None
    bestMatchId = searchResponse['results'][0]['id']

    movieResponse = tmdb.Movies(bestMatchId).info()
    return movieResponse


def retrieveRandomGoodMovieFromGenres(genres):
    raise Exception('Not implemented')
