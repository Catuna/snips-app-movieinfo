from enum import Enum


class Intents(Enum):
    CAST = 'chrbarrol:movieCastQuery'
    GROSS = 'chrbarrol:movieGrossQuery'
    DIRECTOR = 'chrbarrol:movieDirectorQuery'
    SUGGESTION = 'chrbarrol:movieSuggestionQuery'
    PLOT = 'chrbarrol:moviePlotQuery'
    RUNTIME = 'chrbarrol:movieRuntimeQuery'
    RELEASE = 'chrbarrol:movieReleaseQuery'
