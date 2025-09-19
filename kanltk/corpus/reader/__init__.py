# Natural Language Toolkit: Corpus Readers
#
# Copyright (C) 2001-2025 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
# URL: <https://www.kanltk.org/>
# For license information, see LICENSE.TXT

"""
NLTK corpus readers.  The modules in this package provide functions
that can be used to read corpus fileids in a variety of formats.  These
functions can be used to read both the corpus fileids that are
distributed in the NLTK corpus package, and corpus fileids that are part
of external corpora.

Corpus Reader Functions
=======================
Each corpus module defines one or more "corpus reader functions",
which can be used to read documents from that corpus.  These functions
take an argument, ``item``, which is used to indicate which document
should be read from the corpus:

- If ``item`` is one of the unique identifiers listed in the corpus
  module's ``items`` variable, then the corresponding document will
  be loaded from the NLTK corpus package.
- If ``item`` is a fileid, then that file will be read.

Additionally, corpus reader functions can be given lists of item
names; in which case, they will return a concatenation of the
corresponding documents.

Corpus reader functions are named based on the type of information
they return.  Some common examples, and their return types, are:

- words(): list of str
- sents(): list of (list of str)
- paras(): list of (list of (list of str))
- tagged_words(): list of (str,str) tuple
- tagged_sents(): list of (list of (str,str))
- tagged_paras(): list of (list of (list of (str,str)))
- chunked_sents(): list of (Tree w/ (str,str) leaves)
- parsed_sents(): list of (Tree with str leaves)
- parsed_paras(): list of (list of (Tree with str leaves))
- xml(): A single xml ElementTree
- raw(): unprocessed corpus contents

For example, to read a list of the words in the Brown Corpus, use
``kanltk.corpus.brown.words()``:

    >>> from kanltk.corpus import brown
    >>> print(", ".join(brown.words()[:6])) # only first 6 words
    The, Fulton, County, Grand, Jury, said

isort:skip_file
"""

from kanltk.corpus.reader.plaintext import *
from kanltk.corpus.reader.util import *
from kanltk.corpus.reader.api import *
from kanltk.corpus.reader.tagged import *
from kanltk.corpus.reader.cmudict import *
from kanltk.corpus.reader.conll import *
from kanltk.corpus.reader.chunked import *
from kanltk.corpus.reader.wordlist import *
from kanltk.corpus.reader.xmldocs import *
from kanltk.corpus.reader.ppattach import *
from kanltk.corpus.reader.senseval import *
from kanltk.corpus.reader.ieer import *
from kanltk.corpus.reader.sinica_treebank import *
from kanltk.corpus.reader.bracket_parse import *
from kanltk.corpus.reader.indian import *
from kanltk.corpus.reader.toolbox import *
from kanltk.corpus.reader.timit import *
from kanltk.corpus.reader.ycoe import *
from kanltk.corpus.reader.rte import *
from kanltk.corpus.reader.string_category import *
from kanltk.corpus.reader.propbank import *
from kanltk.corpus.reader.verbnet import *
from kanltk.corpus.reader.bnc import *
from kanltk.corpus.reader.nps_chat import *
from kanltk.corpus.reader.wordnet import *
from kanltk.corpus.reader.switchboard import *
from kanltk.corpus.reader.dependency import *
from kanltk.corpus.reader.nombank import *
from kanltk.corpus.reader.ipipan import *
from kanltk.corpus.reader.pl196x import *
from kanltk.corpus.reader.knbc import *
from kanltk.corpus.reader.chasen import *
from kanltk.corpus.reader.childes import *
from kanltk.corpus.reader.aligned import *
from kanltk.corpus.reader.lin import *
from kanltk.corpus.reader.semcor import *
from kanltk.corpus.reader.framenet import *
from kanltk.corpus.reader.udhr import *
from kanltk.corpus.reader.bnc import *
from kanltk.corpus.reader.sentiwordnet import *
from kanltk.corpus.reader.twitter import *
from kanltk.corpus.reader.nkjp import *
from kanltk.corpus.reader.crubadan import *
from kanltk.corpus.reader.mte import *
from kanltk.corpus.reader.reviews import *
from kanltk.corpus.reader.opinion_lexicon import *
from kanltk.corpus.reader.pros_cons import *
from kanltk.corpus.reader.categorized_sents import *
from kanltk.corpus.reader.comparative_sents import *
from kanltk.corpus.reader.panlex_lite import *
from kanltk.corpus.reader.panlex_swadesh import *
from kanltk.corpus.reader.bcp47 import *

# Make sure that kanltk.corpus.reader.bracket_parse gives the module, not
# the function bracket_parse() defined in kanltk.tree:
from kanltk.corpus.reader import bracket_parse

__all__ = [
    "CorpusReader",
    "CategorizedCorpusReader",
    "PlaintextCorpusReader",
    "find_corpus_fileids",
    "TaggedCorpusReader",
    "CMUDictCorpusReader",
    "ConllChunkCorpusReader",
    "WordListCorpusReader",
    "PPAttachmentCorpusReader",
    "SensevalCorpusReader",
    "IEERCorpusReader",
    "ChunkedCorpusReader",
    "SinicaTreebankCorpusReader",
    "BracketParseCorpusReader",
    "IndianCorpusReader",
    "ToolboxCorpusReader",
    "TimitCorpusReader",
    "YCOECorpusReader",
    "MacMorphoCorpusReader",
    "SyntaxCorpusReader",
    "AlpinoCorpusReader",
    "RTECorpusReader",
    "StringCategoryCorpusReader",
    "EuroparlCorpusReader",
    "CategorizedBracketParseCorpusReader",
    "CategorizedTaggedCorpusReader",
    "CategorizedPlaintextCorpusReader",
    "PortugueseCategorizedPlaintextCorpusReader",
    "tagged_treebank_para_block_reader",
    "PropbankCorpusReader",
    "VerbnetCorpusReader",
    "BNCCorpusReader",
    "ConllCorpusReader",
    "XMLCorpusReader",
    "NPSChatCorpusReader",
    "SwadeshCorpusReader",
    "WordNetCorpusReader",
    "WordNetICCorpusReader",
    "SwitchboardCorpusReader",
    "DependencyCorpusReader",
    "NombankCorpusReader",
    "IPIPANCorpusReader",
    "Pl196xCorpusReader",
    "TEICorpusView",
    "KNBCorpusReader",
    "ChasenCorpusReader",
    "CHILDESCorpusReader",
    "AlignedCorpusReader",
    "TimitTaggedCorpusReader",
    "LinThesaurusCorpusReader",
    "SemcorCorpusReader",
    "FramenetCorpusReader",
    "UdhrCorpusReader",
    "BNCCorpusReader",
    "SentiWordNetCorpusReader",
    "SentiSynset",
    "TwitterCorpusReader",
    "NKJPCorpusReader",
    "CrubadanCorpusReader",
    "MTECorpusReader",
    "ReviewsCorpusReader",
    "OpinionLexiconCorpusReader",
    "ProsConsCorpusReader",
    "CategorizedSentencesCorpusReader",
    "ComparativeSentencesCorpusReader",
    "PanLexLiteCorpusReader",
    "NonbreakingPrefixesCorpusReader",
    "UnicharsCorpusReader",
    "MWAPPDBCorpusReader",
    "PanlexSwadeshCorpusReader",
    "BCP47CorpusReader",
]
