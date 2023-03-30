class FA:
    def __init__(self, states, alphabet, transition_table, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_table = transition_table
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, s):
        current_state = self.start_state
        for c in s:
            if c not in self.alphabet:
                return False
            next_states = self.transition_table[current_state][c]
            if isinstance(next_states, list):
                current_state = next_states[0]
            else:
                current_state = next_states
        return current_state in self.accept_states
    
    def is_dfa(self):
        isnfa = 0
        for i in self.transition_table:
            for j in self.alphabet:
                if len(self.transition_table[i][j]) > 1:
                    isnfa += 1
                    break
        if isnfa > 0:
            return False
        else: 
            return True
    def epsilon_closure(self, states):
        # Compute the epsilon closure of a set of NFA states
        closure = set(states)
        stack = list(states)
        while stack:
            state = stack.pop()
            for next_state in self.transition_table[state].get(None, []):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure
    def nfa_to_dfa(self):
        # Start with the epsilon closure of the start state
        start_set = self.epsilon_closure( [self.start_state])
        dfa_states = {frozenset(start_set): 0}
        dfa_alphabet = self.alphabet
        dfa_transition_table = {}
        dfa_accept_states = set()

        # Queue of DFA states to process
        unprocessed_states = [start_set]

        while unprocessed_states:
            current_set = unprocessed_states.pop(0)
            current_state = dfa_states[frozenset(current_set)]

            # Check if the current set contains an accept state
            if any(state in self.accept_states for state in current_set):
                dfa_accept_states.add(current_state)

            # Build the transition table for the current state on each input symbol
            for symbol in dfa_alphabet:
                next_set = set()
                for state in current_set:
                    next_states = self.transition_table[state].get(symbol, [])
                    next_set.update(self.epsilon_closure(next_states))

                # Create a new DFA state for the next set if it doesn't already exist
                if next_set and frozenset(next_set) not in dfa_states:
                    dfa_states[frozenset(next_set)] = len(dfa_states)
                    unprocessed_states.append(next_set)

                # Add the transition from the current DFA state to the next DFA state
                if next_set:
                    next_state = dfa_states[frozenset(next_set)]
                    dfa_transition_table.setdefault(current_state, {})[symbol] = next_state

        # Build the DFA object
        dfa_states = list(range(len(dfa_states)))
        dfa_start_state = 0
        dfa_accept_states = list(dfa_accept_states)
        print(dfa_transition_table)
        return FA(dfa_states, dfa_alphabet, dfa_transition_table, dfa_start_state, dfa_accept_states)

    def visualize(self):
        for i in self.transition_table:
            for j in self.alphabet:
                if j in self.transition_table[i]:
                    if type(self.transition_table[i][j]) != int:
                        for x in self.transition_table[i][j]:
                            print('q',i, ' ---',j,'---> ',x)
                    elif type(self.transition_table[i][j]) == int:
                        print('q',i, ' ---',j,'---> ',self.transition_table[i][j])