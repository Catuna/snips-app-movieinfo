from intents import Intents


def getReplyForNoMovieFound(query):
    return 'Sorry, I was not able to find the movie \'{}\''.format(query)


def getReplyForSpecificMovieQuery(movieData, intent):
    if intent is Intents.CAST:
        return getMovieCastReply(movieData)
    elif intent is Intents.DIRECTOR:
        return getMovieDirectorReply(movieData)
    elif intent is Intents.PLOT:
        return getMoviePlotReply(movieData)
    elif intent is Intents.RELEASE:
        return getMovieReleaseReply(movieData)


def getMovieCastReply(movieData):
    raise Exception('Not implemented')


def getMovieDirectorReply(movieData):
    raise Exception('Not implemented')


def getMoviePlotReply(movieData):
    raise Exception('Not implemented')


def getMovieRuntimeReply(movieData):
    raise Exception('Not implemented')


def getMovieReleaseReply(movieData):
    raise Exception('Not implemented')


def getReplyForSuggestedMovie(movieData):
    raise Exception('Not implemented')
