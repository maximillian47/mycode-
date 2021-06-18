#!/usr/bin/env

import csv

print("""
        Welcome, let's do it.
      """)

with open("brett_comics.txt", "r") as comicfile:
    comicDoc = csv.reader(comicfile, delimiter=",")
    userChoice = input("""Choose 
                    1.
                    2. 
                    3.
                    >""").title()
    
    for line in comicDoc:    
        if author in line.lower():
                filename = "pokepoke.txt"

                with open(filename, "w") as pkfile:
                print(f'{line}', file=comicD)


