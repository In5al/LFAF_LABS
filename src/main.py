from src.grammer.grammer import *
from src.automaton.automaton import *
# Define the regular grammar
grammar = {
    "S": ["aP", "bQ"],
    "P": ["bP", "cP","dQ","e"],
    "Q": ["eQ", "fQ","a"]
}
grammar1 = [("S","P","a"),("S","Q","b"),("P","P","b"),("P","P","c"),("P","Q","d"),
            ("P","","e"),("Q","Q","e"),("Q","Q","e"),("Q","Q","f"),("Q","","a")]


automaton = create_automaton(grammar1)
print(automaton)

print("here are 5 words from given grammer")
for _ in range(5):
    word = generate_word(grammar,"S")
    print(word)
print("")

accepts(automaton,"ace")
accepts(automaton,"ohno")