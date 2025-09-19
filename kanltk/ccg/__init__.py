# Natural Language Toolkit: Combinatory Categorial Grammar
#
# Copyright (C) 2001-2025 NLTK Project
# Author: Graeme Gange <ggange@csse.unimelb.edu.au>
# URL: <https://www.kanltk.org/>
# For license information, see LICENSE.TXT

"""
Combinatory Categorial Grammar.

For more information see nltk/doc/contrib/ccg/ccg.pdf
"""

from kanltk.ccg.chart import CCGChart, CCGChartParser, CCGEdge, CCGLeafEdge
from kanltk.ccg.combinator import (
    BackwardApplication,
    BackwardBx,
    BackwardCombinator,
    BackwardComposition,
    BackwardSx,
    BackwardT,
    DirectedBinaryCombinator,
    ForwardApplication,
    ForwardCombinator,
    ForwardComposition,
    ForwardSubstitution,
    ForwardT,
    UndirectedBinaryCombinator,
    UndirectedComposition,
    UndirectedFunctionApplication,
    UndirectedSubstitution,
    UndirectedTypeRaise,
)
from kanltk.ccg.lexicon import CCGLexicon
