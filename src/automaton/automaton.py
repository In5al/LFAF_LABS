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

    # Check if the final state is accepting


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
