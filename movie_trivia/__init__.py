from intents import Intents
from text_gen import (getReplyForSpecificMovieQuery,
                      getReplyForSuggestedMovie,
                      getReplyForNoMovieFound)
from data_retrieval import (retrieveMostRelevantMovieFromQuery,
                            retrieveMovieCredits,
                            retrieveMovieInfo,
                            retrieveRandomGoodMovieFromGenres)
from snipshelpers.intent_helper import (getFirstBySlotName, getAllBySlotName)


def isIntentSpecificMovieQuery(intent):
    return (intent is Intents.CAST
            or intent is Intents.CAST
            or intent is Intents.DIRECTOR
            or intent is Intents.PLOT
            or intent is Intents.RUNTIME
            or intent is Intents.RELEASE)


def handleIntent(sessionId, intentString, slots):
    intent = Intents(intentString)

    if isIntentSpecificMovieQuery(intent):
        query = extractQueryFromSlots(slots)
        movie = retrieveMostRelevantMovieFromQuery(query)
        if movie is None:
            return getReplyForNoMovieFound(query)

        extraData = None
        if (intent is Intents.PLOT
           or intent is Intents.RUNTIME
           or intent is Intents.RELEASE):
            extraData = retrieveMovieInfo(movie['id'])
        elif (intent is Intents.DIRECTOR
              or intent is Intents.CAST):
            extraData = retrieveMovieCredits(movie['id'])

        return getReplyForSpecificMovieQuery(movie['title'], extraData, intent)
    else:
        if intent is Intents.SUGGESTION:
            genres = extractGenresFromSlots(slots)
            movie = retrieveRandomGoodMovieFromGenres(genres)
            return getReplyForSuggestedMovie(movie)


def extractQueryFromSlots(slots):
    matchingSlot = getFirstBySlotName(slots, 'movieName')
    if matchingSlot is None:
        return None
    else:
        return matchingSlot['rawValue']


def extractGenresFromSlots(slots):
    matchingSlots = getAllBySlotName(slots, 'movieGenre')
    genres = []
    for slot in matchingSlots:
        genres.append(slot['rawValue'])
    return genres
