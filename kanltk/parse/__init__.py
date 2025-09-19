# Natural Language Toolkit: Parsers
#
# Copyright (C) 2001-2025 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
# URL: <https://www.nltk.org/>
# For license information, see LICENSE.TXT
#

"""
NLTK Parsers

Classes and interfaces for producing tree structures that represent
the internal organization of a text.  This task is known as "parsing"
the text, and the resulting tree structures are called the text's
"parses".  Typically, the text is a single sentence, and the tree
structure represents the syntactic structure of the sentence.
However, parsers can also be used in other domains.  For example,
parsers can be used to derive the morphological structure of the
morphemes that make up a word, or to derive the discourse structure
for a set of utterances.

Sometimes, a single piece of text can be represented by more than one
tree structure.  Texts represented by more than one tree structure are
called "ambiguous" texts.  Note that there are actually two ways in
which a text can be ambiguous:

    - The text has multiple correct parses.
    - There is not enough information to decide which of several
      candidate parses is correct.

However, the parser module does *not* distinguish these two types of
ambiguity.

The parser module defines ``ParserI``, a standard interface for parsing
texts; and two simple implementations of that interface,
``ShiftReduceParser`` and ``RecursiveDescentParser``.  It also contains
three sub-modules for specialized kinds of parsing:

  - ``nltk.parser.chart`` defines chart parsing, which uses dynamic
    programming to efficiently parse texts.
  - ``nltk.parser.probabilistic`` defines probabilistic parsing, which
    associates a probability with each parse.
"""

from kanltk.parse.api import ParserI
from kanltk.parse.bllip import BllipParser
from kanltk.parse.chart import (
    BottomUpChartParser,
    BottomUpLeftCornerChartParser,
    ChartParser,
    LeftCornerChartParser,
    SteppingChartParser,
    TopDownChartParser,
)
from kanltk.parse.corenlp import CoreNLPDependencyParser, CoreNLPParser
from kanltk.parse.dependencygraph import DependencyGraph
from kanltk.parse.earleychart import (
    EarleyChartParser,
    FeatureEarleyChartParser,
    FeatureIncrementalBottomUpChartParser,
    FeatureIncrementalBottomUpLeftCornerChartParser,
    FeatureIncrementalChartParser,
    FeatureIncrementalTopDownChartParser,
    IncrementalBottomUpChartParser,
    IncrementalBottomUpLeftCornerChartParser,
    IncrementalChartParser,
    IncrementalLeftCornerChartParser,
    IncrementalTopDownChartParser,
)
from kanltk.parse.evaluate import DependencyEvaluator
from kanltk.parse.featurechart import (
    FeatureBottomUpChartParser,
    FeatureBottomUpLeftCornerChartParser,
    FeatureChartParser,
    FeatureTopDownChartParser,
)
from kanltk.parse.malt import MaltParser
from kanltk.parse.nonprojectivedependencyparser import (
    NaiveBayesDependencyScorer,
    NonprojectiveDependencyParser,
    ProbabilisticNonprojectiveParser,
)
from kanltk.parse.pchart import (
    BottomUpProbabilisticChartParser,
    InsideChartParser,
    LongestChartParser,
    RandomChartParser,
    UnsortedChartParser,
)
from kanltk.parse.projectivedependencyparser import (
    ProbabilisticProjectiveDependencyParser,
    ProjectiveDependencyParser,
)
from kanltk.parse.recursivedescent import (
    RecursiveDescentParser,
    SteppingRecursiveDescentParser,
)
from kanltk.parse.shiftreduce import ShiftReduceParser, SteppingShiftReduceParser
from kanltk.parse.transitionparser import TransitionParser
from kanltk.parse.util import TestGrammar, extract_test_sentences, load_parser
from kanltk.parse.viterbi import ViterbiParser
