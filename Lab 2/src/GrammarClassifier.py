import re

class GrammarClassifier:
    
    def is_regular_grammar(self, grammar):
        """
        Check if a grammar is a regular grammar.
        """
        for left in grammar:
            for right in grammar[left]:
                if len(left) > 1:
                    return False
                if re.search(r"[A-Z]{2,}", right):
                    return False
                if re.search(r"[A-Z][a-z]*[A-Z]", right):
                    return False
                if re.search(r"^[a-z]*[A-Z]?[a-z]*$", right):
                    continue
                if right == "ε":
                    continue
                return False
        return True

    def is_context_free_grammar(self, grammar):
        """
        Check if a grammar is a context-free grammar.
        """
        nonterminals = set(grammar.keys())
        for left in grammar:
            for right in grammar[left]:
                if not re.match(r"^([a-z]|[A-Z])+|ε$", right):
                    if len(left) != 1 or not left.isupper():
                        return False
                    for symbol in right:
                        if symbol.isupper() and symbol not in nonterminals:
                            return False
        return True

    def is_context_sensitive_grammar(self, grammar):
        """
        Check if a grammar is a context-sensitive grammar.
        """
        for left in grammar:
            for right in grammar[left]:
                if len(left) < len(right):
                    continue
                if len(left) == len(right) and left.isupper():
                    continue
                nonterminals = set(grammar.keys())
                for symbol in right:
                    if symbol.isupper() and symbol not in nonterminals:
                        return False
        return True

    def is_unrestricted_grammar(self, grammar):
        """
        Check if a grammar is an unrestricted grammar.
        """
        return True


    def check_grammar(self, grammar):
        if self.is_regular_grammar(grammar):
            return "Type 3: The grammar is a regular grammar."
        elif self.is_context_free_grammar(grammar):
            return "Type 2: The grammar is a context-free grammar."
        elif self.is_context_sensitive_grammar(grammar):
            return "Type 1: The grammar is a context-sensitive grammar."
        elif self.is_unrestricted_grammar(grammar):
            return "Type 0: The grammar is an unrestricted grammar."
        else:
            return "The grammar is not recognized."