class Algorithm2LFCO2025JCAP:
    def string_check(self, string_to_check: str) -> bool:
        stack = ['#']
        current_state = 'q0'

        i = 0
        while i <= len(string_to_check):
            top = stack[-1]

            # Handle empty string as special case
            if string_to_check == "":
                return True

            # End of input, check if we should accept
            if i == len(string_to_check):
                if current_state == 'q1' and top == '#':
                    return True
                else:
                    return False

            current_char = string_to_check[i]

            if current_state == 'q0' and current_char == 'a' and (top == '#' or top == 'A'):
                stack.append('A')
            elif current_state == 'q0' and current_char == 'b' and top == 'A':
                current_state = 'q1'
                stack.pop()
            elif current_state == 'q1' and current_char == 'b' and top == 'A':
                stack.pop()
            else:
                return False

            i += 1

        return False
