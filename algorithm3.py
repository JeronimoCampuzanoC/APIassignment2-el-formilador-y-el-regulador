class Algorithm3LFCO2025JCAP:
    def sentential(self, string_to_check: str):
        steps = []
        builder = "S"
        half_length = len(string_to_check) // 2
        
        steps.append({"Rule": "", "Sentential": builder})  # Initial state

        # Handles the special case where the string is empty (ε)
        if string_to_check == "ε" :
            builder = "ε"
            steps.append({"Rule": "Rule 2", "Sentential": builder})

        for i in range(1, half_length + 1):

            builder = "a" + builder + "b"
            steps.append({"Rule": "Rule 1", "Sentential": builder})
            
            if i == half_length:
                builder = builder.replace("S", "")
                steps.append({"Rule": "Rule 2", "Sentential": builder})
        
        return steps

    def configurationM(self, string_to_check: str) -> list[dict]:
        steps = []  # This is a dicitonary, not a list
        stack = ['#']
        current_state = "q0"
        current_string = string_to_check

        # Initial state of EVERY string
        steps.append({
            "State": current_state,
            "String": current_string,
            "Stack": self.stack_to_string(stack)
        })

        # Handles the special case where the string is empty (ε)
        if string_to_check == "ε" :
            steps.append({
                "State": "q1",
                "String": "ε",
                "Stack": "ε"
            })
            return steps

        i = 0
        while i <= len(string_to_check):
            top = stack[-1] if stack else ''

            char = string_to_check[i] if i < len(string_to_check) else ''

            # Applies the transition rules acording to the state, current character and top of the stack
            if current_state == "q0" and char == 'a' and (top == '#' or top == 'A'):
                stack.append('A')
                current_string = current_string[1:]
                steps.append({
                    "State": current_state,
                    "String": current_string or "ε",
                    "Stack": self.stack_to_string(stack)
                })
            
            elif current_state == "q0" and char == 'b' and top == 'A':
                current_state = "q1"
                stack.pop()
                current_string = current_string[1:]
                steps.append({
                    "State": current_state,
                    "String": current_string or "ε",
                    "Stack": self.stack_to_string(stack)
                })
            
            elif current_state == "q1" and char == 'b' and top == 'A':
                stack.pop()
                current_string = current_string[1:]
                steps.append({
                    "State": current_state,
                    "String": current_string or "ε",
                    "Stack": self.stack_to_string(stack)
                })

            elif current_state == "q1" and char == '' and top == '#':
                stack.pop()
                steps.append({
                    "State": current_state,
                    "String": current_string or "ε",
                    "Stack": "ε"
                })
            
            i += 1

        return steps

    def stack_to_string(self, stack: list[str]) -> str:
        return ''.join(reversed(stack))
