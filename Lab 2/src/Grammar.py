import random

class Grammar:
    
    def __init__(self, rules):
        self.rules = rules
    
    def check_string(self, string):
        for i in range (len(string)):
            if string[i] in self.rules.keys():
                return "false"
        return "true"
    
    def generate_string(self):
        new_str = "S"
        j = len(new_str) - 1
        while (self.check_string(new_str) == "false"):
            if new_str[j] in self.rules.keys():
                new_str = new_str[0:j] + random.choice(self.rules[new_str[j]])
                j = len(new_str) - 1
        return new_str