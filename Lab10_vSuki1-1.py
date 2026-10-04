"""
Lab 10
Author: Disukhi Ahmed
"""


from pathlib import Path
import string

class WordAnalyzer:

    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.__frequencies = {}

    