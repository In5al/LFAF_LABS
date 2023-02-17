from src.grammer.grammer import *
from src.automaton.automaton import *
# Define the regular grammar
grammar = {
    "S": ["aD"],
    "D": ["bE"],
    "E": ["cF", "dL"],
    "F": ["dD"],
    "L":["aL","bL","c"]

}
grammar1 = [("S","D","a"),("D","E","b"),("E","F","c"),("E","L","d"),("F","D","d"),
            ("L","L","a"),("L","L","b"),("L","","c")]



automaton = create_automaton(grammar1)
print(automaton)

print("here are 5 words from given grammer")
for _ in range(5):
    word = generate_word(grammar,"S")
    print(word)
print("")

accepts(automaton,"abdbc")
accepts(automaton,"ohno")