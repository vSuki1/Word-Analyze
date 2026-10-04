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

    def process_file(self):
        translator = str.maketrans("", "", string.punctuation)
        try:
            print(self.__filepath.exists())
            file = self.__filepath.open("r", encoding="utf-8")
            for line in file:
                line = line.translate(translator)
                line = line.lower()
                word = line.split()
                print(line)
        except FileNotFoundError as e:
            print("File not found")
    

        
          