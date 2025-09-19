# Natural Language Toolkit: Inference
#
# Copyright (C) 2001-2025 NLTK Project
# Author: Dan Garrette <dhgarrette@gmail.com>
#         Ewan Klein <ewan@inf.ed.ac.uk>
#
# URL: <https://www.kanltk.org/>
# For license information, see LICENSE.TXT

"""
Classes and interfaces for theorem proving and model building.
"""

from kanltk.inference.api import ParallelProverBuilder, ParallelProverBuilderCommand
from kanltk.inference.discourse import (
    CfgReadingCommand,
    DiscourseTester,
    DrtGlueReadingCommand,
    ReadingCommand,
)
from kanltk.inference.mace import Mace, MaceCommand
from kanltk.inference.prover9 import Prover9, Prover9Command
from kanltk.inference.resolution import ResolutionProver, ResolutionProverCommand
from kanltk.inference.tableau import TableauProver, TableauProverCommand
