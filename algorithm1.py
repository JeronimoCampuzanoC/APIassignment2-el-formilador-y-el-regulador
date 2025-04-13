import random
from algorithm2 import Algorithm2LFCO2025JCAP  # or however you structured the class import

class Algorithm1LFCO2025JCAP:
    def __init__(self):
        self.algorithm2 = Algorithm2LFCO2025JCAP()

    def generate_grammar_strings(self) -> str:
        string_to_push = ""
        length_string = random.randint(0, 5) * 2  # ensure even number

        string_to_push += 'a' * (length_string // 2)
        string_to_push += 'b' * (length_string // 2)

        if string_to_push == "" :
            return "ε"

        return string_to_push

    def generate_non_grammar_strings(self) -> str:
        while True:
            length_string = random.randint(1, 10)
            string_to_push = ''.join(random.choice(['a', 'b']) for _ in range(length_string))

            if not self.algorithm2.string_check(string_to_push):
                return string_to_push