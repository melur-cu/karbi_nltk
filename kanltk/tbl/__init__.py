# Natural Language Toolkit: Transformation-based learning
#
# Copyright (C) 2001-2025 NLTK Project
# Author: Marcus Uneson <marcus.uneson@gmail.com>
#   based on previous (nltk2) version by
#   Christopher Maloof, Edward Loper, Steven Bird
# URL: <https://www.nltk.org/>
# For license information, see  LICENSE.TXT

"""
Transformation Based Learning

A general purpose package for Transformation Based Learning,
currently used by kanltk.tag.BrillTagger.

isort:skip_file
"""

from kanltk.tbl.template import Template

# API: Template(...), Template.expand(...)

from kanltk.tbl.feature import Feature

# API: Feature(...), Feature.expand(...)

from kanltk.tbl.rule import Rule

# API: Rule.format(...), Rule.templatetid

from kanltk.tbl.erroranalysis import error_list
