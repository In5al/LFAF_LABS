# The title of the work

### Course: Formal Languages & Finite Automata
### Author: Carp Dan-Octavian

----

## Theory
"regular grammar use" refers to the set of rules and conventions that govern the way words and phrases are structured and arranged in a language. These rules include guidelines for spelling, punctuation, capitalization, and sentence structure. The purpose of regular grammar use is to facilitate clear communication by providing a standardized system for organizing and conveying meaning through language. By following the rules of regular grammar use, speakers and writers can effectively convey their intended message and minimize confusion or ambiguity for their audience.

what do you need in a grammer ? first of all you need the alphabet(that's the symboles you'll use in your words) then you'll need to identify the terminal and non terminal variable, they're usually denoted by size so the big letters for non-terminal vars and the small for the terminal ones, next you'll need your production table in this table you need to put the rules and which non-terminal var goes to what terminal one and the different comboes that can be formed from this, you can try to imagine all the posabilites but usualy they're displayed in a derivation tree to be easly understood and modeled.

In summary, the point of an automaton is to create a machine that can perform a specific task or function autonomously, without requiring constant human intervention. The purpose of an automaton can vary depending on its intended application, with the goal of increasing efficiency, safety, or productivity in a given domain.


## Objectives:

* to create a git repository
* to choose a programming language
* create a prgrame that generates 5 word from the grammer 
* create a finite automaton that checks if a word belongs to the grammer


## Implementation description

* About 2-3 sentences to explain each piece of the implementation.


* Code snippets from your files.
the word generating function
```
grammar = { "S": ["aD"],
    "D": ["bE"],
    "E": ["cF", "dL"],
    "F": ["dD"],
    "L":["aL","bL","c"]
    
    }

def generate_word(grammar, start_symbol):
    word = "S"
    current_symbol = start_symbol
    while True:
        if current_symbol not in grammar:  # if current symbol is terminal
            word += current_symbol  # add to the word
            current_symbol = "end"
            if not word:  # if the word is empty, return None
                return None
            if len(word) > 10:  # if word is too long, return None
                return None
            if current_symbol == "end":  # if end symbol is reached, return the word
                word = word.replace("end","")
                return word[:-1]  # remove the end symbol

        else:
            rhs = random.choice(grammar[current_symbol])  # choose a random rule
            word = word.replace(current_symbol,rhs[0])
            for symbol in rhs[1:]:
                word += symbol
            current_symbol = word[-1]  # set current symbol to the last character in the word
 ```
 the automaton creating code 
 ```
 def create_automaton(grammar):
    # Step 1: Define the states of the automaton
    states = set([rule[0] for rule in grammar])

    # Step 2: Define the transitions between states
    transitions = {}
    for state in states:
        for rule in grammar:
            if rule[0] == state:
                if rule[1] == "":
                    # Epsilon transition
                    if state in transitions:
                        transitions[state].append((rule[2], None))
                    else:
                        transitions[state] = [(rule[2], None)]
                else:
                    # Regular transition
                    if state in transitions:
                        transitions[state].append((rule[2], rule[1]))
                    else:
                        transitions[state] = [(rule[2], rule[1])]

    # Step 3: Identify the start state of the automaton
    start_state = grammar[0][0]

    # Step 4: Identify the accepting states of the automaton
    accepting_states = set()
    for state in states:
        for rule in grammar:
            if rule[0] == state and rule[1] == "":
                accepting_states.add(state)

    # Construct the automaton
    automaton = {"states": states,
                 "transitions": transitions,
                 "start_state": start_state,
                 "accepting_states": accepting_states}

    return automaton
```
 
 
 the checking mechanism that checks the word to the automaton created
```
def accepts(automaton, word):
    current_state = automaton['start_state']
    for char in word:
        exists = False
        for symbol in automaton['transitions'][current_state]:
            if char == symbol[0]:
                current_state = symbol[1]
                exists = True

        if current_state is None:
            print(f"{word} is in this grammer")

        elif exists == False:
            # The current state does not have a transition on the current character
            print(f"{word} is not in this grammer")
            break
```



## Conclusions / Screenshots / Results
In conclusion, regular languages, such as regular expressions, are essential for creating programs that can process text input and extract specific patterns or words. By using regular expressions, programmers can define patterns of characters in a string and use them to identify and extract data from text inputs.

Overall, regular languages are a powerful tool for software development, and an understanding of regular languages is an essential skill for any programmer who wants to develop effective text processing applications.

## reuslts:
the automaton created for our grammer:
{'states': {'L', 'S', 'F', 'D', 'E'}, 'transitions': {'L': [('a', 'L'), ('b', 'L'), ('c', None)], 'S': [('a', 'D')], 'F': [('d', 'D')], 'D': [('b', 'E')], 'E': [('c', 'F'), ('d', 'L')]}, 'start_state': 'S', 'accepting_states': {'L'}}
here are 5 words from given grammer
abdc
abcdbdac
abdac
abdc
None

abdbc is in this grammer
ohno is not in this grammer

Process finished with exit code 0

