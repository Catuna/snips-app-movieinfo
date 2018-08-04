from intents import Intents


def getReplyForSpecificMediaQuery(media, intent):
    if intent is Intents.CAST:
        return getMediaCastReply(media)
    elif intent is Intents.DIRECTOR:
        return getMediaDirectorReply(media)
    elif intent is Intents.PLOT:
        return getMediaPlotReply(media)
    elif intent is Intents.RELEASE:
        return getMediaReleaseReply(media)


def getMediaCastReply(mediaData):
    raise Exception('Not implemented')


def getMediaDirectorReply(mediaData):
    raise Exception('Not implemented')


def getMediaPlotReply(mediaData):
    raise Exception('Not implemented')


def getMediaRuntimeReply(mediaData):
    raise Exception('Not implemented')


def getMediaReleaseReply(mediaData):
    raise Exception('Not implemented')


def getReplyForSuggestedMovie(mediaData):
    raise Exception('Not implemented')
