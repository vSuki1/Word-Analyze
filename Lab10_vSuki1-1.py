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
            """
            print(self.__filepath.exists())
            """
            file = self.__filepath.open("r", encoding="utf-8")
            for line in file:
                line = line.translate(translator)
                line = line.lower()
                word = line.split()
                
                for w in word:
                    if w in self.__frequencies:
                        self.__frequencies[w] += 1
                    else:
                        self.__frequencies[w] = 1
            file.close()
        except FileNotFoundError as e:
            print("File not found")
            return False
        return True
    def print_report(self):
        word_list = sorted(self.__frequencies.keys())
        
        for word in word_list:
            print(f"{word} :: {self.__frequencies[word]}")
        
    
"""
analyzer = WordAnalyzer("princess_mars.txt")
analyzer.process_file()
analyzer.print_report()
"""


def main():
    file_menu = {
        "1": Path("princess_mars.txt"),
        "2": Path("Tarzan.txt"),
        "3": Path("treasure_island.txt"),
        "4": Path("monte_cristo.txt")
    }
    print("Please select a file to analyze:")
    print("1. Princess of Mars")
    print("2. Tarzan")
    print("3. Treasure Island")
    print("4. The Count of Monte Cristo")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "5":
     print("exited")
    elif choice in file_menu:
        analyzer = WordAnalyzer(file_menu[choice])
        if analyzer.process_file():
            analyzer.print_report()
    else:
        print("Invalid")

main()