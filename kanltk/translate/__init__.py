# Natural Language Toolkit: Machine Translation
#
# Copyright (C) 2001-2025 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>, Tah Wei Hoon <hoon.tw@gmail.com>
# URL: <https://www.nltk.org/>
# For license information, see LICENSE.TXT

"""
Experimental features for machine translation.
These interfaces are prone to change.

isort:skip_file
"""

from kanltk.translate.api import AlignedSent, Alignment, PhraseTable
from kanltk.translate.ibm_model import IBMModel
from kanltk.translate.ibm1 import IBMModel1
from kanltk.translate.ibm2 import IBMModel2
from kanltk.translate.ibm3 import IBMModel3
from kanltk.translate.ibm4 import IBMModel4
from kanltk.translate.ibm5 import IBMModel5
from kanltk.translate.bleu_score import sentence_bleu as bleu
from kanltk.translate.ribes_score import sentence_ribes as ribes
from kanltk.translate.meteor_score import meteor_score as meteor
from kanltk.translate.metrics import alignment_error_rate
from kanltk.translate.stack_decoder import StackDecoder
from kanltk.translate.nist_score import sentence_nist as nist
from kanltk.translate.chrf_score import sentence_chrf as chrf
from kanltk.translate.gale_church import trace
from kanltk.translate.gdfa import grow_diag_final_and
from kanltk.translate.gleu_score import sentence_gleu as gleu
from kanltk.translate.phrase_based import extract
from kanltk.translate.lepor import sentence_lepor as lepor, corpus_lepor
