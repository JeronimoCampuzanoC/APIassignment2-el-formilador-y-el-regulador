class Algorithm3LFCO2025JCAP:
    def sentential(self, string_to_check: str):
        builder = "S"
        half_length = len(string_to_check) // 2

        print(f"{'Rule':<10}{'Sentential':<20}")
        
        for i in range(half_length + 1):
            if i == 0:
                print(f"{'':<10}{builder:<20}")
                continue

            builder = "a" + builder + "b"
            print(f"{'Rule 1':<10}{builder:<20}")

            if i == half_length:
                builder = builder.replace("S", "")
                print(f"{'Rule 2':<10}{builder:<20}")

        if string_to_check == "":
            print(f"{'':<10}{builder:<20}")
            print(f"{'Rule 2':<10}{'':<20}")

    def configurationM(self, string_to_check: str):
        stack = ['#']
        current_state = "q0"
        current_string = string_to_check

        print("Accepting computation of M on input x\n")
        print(f"{'State':<10}{'String':<10}{'Stack':<10}")
        print(f"{current_state:<10}{current_string:<10}{self.stack_to_string(stack):<10}")

        i = 0
        while i <= len(string_to_check):
            top = stack[-1] if stack else ''
            
            if string_to_check == "":
                break

            # End of input
            if i == len(string_to_check) and current_state == "q1" and top == '#':
                stack.pop()
                print(f"{current_state:<10}{'ε':<10}{self.stack_to_string(stack):<10}")
                return

            char = string_to_check[i] if i < len(string_to_check) else ''

            if current_state == "q0" and char == 'a' and (top == '#' or top == 'A'):
                stack.append('A')
                current_string = current_string[1:]
                print(f"{current_state:<10}{current_string or 'ε':<10}{self.stack_to_string(stack):<10}")
            elif current_state == "q0" and char == 'b' and top == 'A':
                current_state = "q1"
                stack.pop()
                current_string = current_string[1:]
                print(f"{current_state:<10}{current_string or 'ε':<10}{self.stack_to_string(stack):<10}")
            elif current_state == "q1" and char == 'b' and top == 'A':
                stack.pop()
                current_string = current_string[1:]
                print(f"{current_state:<10}{current_string or 'ε':<10}{self.stack_to_string(stack):<10}")
            else:
                break

            i += 1

    def stack_to_string(self, stack: list[str]) -> str:
        return ''.join(reversed(stack))
