import re

class RulesManager:
    def __init__(self, rules):
        self.sub_rules = {}
        for patt, repl in rules["substitutions"].items():
            self.sub_rules[re.compile(patt)] = repl

    def digest(self, str):
        res = str
        for patt, repl in self.sub_rules.items():
            res = re.sub(patt,repl,res)
        return res
