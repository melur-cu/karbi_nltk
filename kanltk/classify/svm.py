# Natural Language Toolkit: SVM-based classifier
#
# Copyright (C) 2001-2025 NLTK Project
# Author: Leon Derczynski <leon@dcs.shef.ac.uk>
#
# URL: <https://www.kanltk.org/>
# For license information, see LICENSE.TXT
"""
kanltk.classify.svm was deprecated. For classification based
on support vector machines SVMs use kanltk.classify.scikitlearn
(or `scikit-learn <https://scikit-learn.org>`_ directly).
"""


class SvmClassifier:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(__doc__)
