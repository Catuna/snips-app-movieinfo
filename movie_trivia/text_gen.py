from intents import Intents

MAX_PERSONS_LISTED = 4


def getReplyForNoMovieFound(query):
    return 'I was not able to find the movie \'{}\''.format(query)


def getReplyForSpecificMovieQuery(movieName, movieData, intent):
    if intent is Intents.CAST:
        return getMovieCastReply(movieName, movieData)
    elif intent is Intents.DIRECTOR:
        return getMovieDirectorReply(movieName, movieData)
    elif intent is Intents.PLOT:
        return getMoviePlotReply(movieName, movieData)
    elif intent is Intents.RELEASE:
        return getMovieReleaseReply(movieName, movieData)


def getMovieCastReply(movieName, movieData):
    if 'cast' not in movieData:
        return 'I could not find the cast of {}'.format(movieName)

    reply = 'Starring in {}: '.format(movieName)
    castCount = 0
    for person in movieData['cast']:
        if castCount == MAX_PERSONS_LISTED:
            break
        if castCount == MAX_PERSONS_LISTED-1:
            reply += 'and '
        reply += '{}, '.format(person['name'])
        castCount += 1

    return reply


def getMovieDirectorReply(movieName, movieData):
    raise Exception('Not implemented')


def getMoviePlotReply(movieName, movieData):
    raise Exception('Not implemented')


def getMovieRuntimeReply(movieName, movieData):
    raise Exception('Not implemented')


def getMovieReleaseReply(movieName, movieData):
    raise Exception('Not implemented')


def getReplyForSuggestedMovie(movieData):
    raise Exception('Not implemented')
