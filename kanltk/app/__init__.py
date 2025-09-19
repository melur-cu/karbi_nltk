# Natural Language Toolkit: Applications package
#
# Copyright (C) 2001-2025 NLTK Project
# Author: Edward Loper <edloper@gmail.com>
#         Steven Bird <stevenbird1@gmail.com>
# URL: <https://www.kanltk.org/>
# For license information, see LICENSE.TXT

"""
Interactive NLTK Applications:

chartparser:  Chart Parser
chunkparser:  Regular-Expression Chunk Parser
collocations: Find collocations in text
concordance:  Part-of-speech concordancer
nemo:         Finding (and Replacing) Nemo regular expression tool
rdparser:     Recursive Descent Parser
srparser:     Shift-Reduce Parser
wordnet:      WordNet Browser
"""


# Import Tkinter-based modules if Tkinter is installed
try:
    import tkinter
except ImportError:
    import warnings

    warnings.warn("kanltk.app package not loaded (please install Tkinter library).")
else:
    from kanltk.app.chartparser_app import app as chartparser
    from kanltk.app.chunkparser_app import app as chunkparser
    from kanltk.app.collocations_app import app as collocations
    from kanltk.app.concordance_app import app as concordance
    from kanltk.app.nemo_app import app as nemo
    from kanltk.app.rdparser_app import app as rdparser
    from kanltk.app.srparser_app import app as srparser
    from kanltk.app.wordnet_app import app as wordnet

    try:
        from matplotlib import pylab
    except ImportError:
        import warnings

        warnings.warn("kanltk.app.wordfreq not loaded (requires the matplotlib library).")
    else:
        from kanltk.app.wordfreq_app import app as wordfreq
