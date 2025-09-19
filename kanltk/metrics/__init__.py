# Natural Language Toolkit: Metrics
#
# Copyright (C) 2001-2025 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
# URL: <https://www.nltk.org/>
# For license information, see LICENSE.TXT
#

"""
NLTK Metrics

Classes and methods for scoring processing modules.
"""

from kanltk.metrics.agreement import AnnotationTask
from kanltk.metrics.aline import align
from kanltk.metrics.association import (
    BigramAssocMeasures,
    ContingencyMeasures,
    NgramAssocMeasures,
    QuadgramAssocMeasures,
    TrigramAssocMeasures,
)
from kanltk.metrics.confusionmatrix import ConfusionMatrix
from kanltk.metrics.distance import (
    binary_distance,
    custom_distance,
    edit_distance,
    edit_distance_align,
    fractional_presence,
    interval_distance,
    jaccard_distance,
    masi_distance,
    presence,
)
from kanltk.metrics.paice import Paice
from kanltk.metrics.scores import (
    accuracy,
    approxrand,
    f_measure,
    log_likelihood,
    precision,
    recall,
)
from kanltk.metrics.segmentation import ghd, pk, windowdiff
from kanltk.metrics.spearman import (
    ranks_from_scores,
    ranks_from_sequence,
    spearman_correlation,
)
