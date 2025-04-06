from algorithm1 import Algorithm1LFCO2025JCAP
from algorithm2 import Algorithm2LFCO2025JCAP
from algorithm3 import Algorithm3LFCO2025JCAP

def main():
    print("Generating strings")
    print("------------------")

    p1 = Algorithm1LFCO2025JCAP()
    strings = []

    for i in range(16):
        if i % 2 == 0:
            strings.append(p1.generate_grammar_strings())
        else:
            strings.append(p1.generate_non_grammar_strings())

    for s in strings:
        print("⩼ String:", s)

    print("\n\nPDA")
    print("✓ Q = {q0,q1}")
    print("✓ Sigma = {a,b}")
    print("✓ Gamma = {A,#}")
    print("✓ Delta = \n"
          "{((q0,a,#),(q0,A#))\n"
          " ((q0,a,A),(q0,AA))\n"
          " ((q0,b,A),(q1,ε))\n"
          " ((q1,b,A),(q1,ε))\n"
          " ((q1,ε,#),(q1,ε))}")
    print("✓ Starting state = q0")
    print("✓ Initial stack symbol = #")
    print("✓ Acceptance states = {q1}\n\n")

    print("Checking the strings")
    print("---------------------")

    valid_strings = []
    p2 = Algorithm2LFCO2025JCAP()

    for s in strings:
        if p2.string_check(s):
            valid_strings.append(s)
            print(f"✅ The String: {s} is accepted by the PDA.")
        else:
            print(f"❌ The String: {s} is rejected by the PDA.")

    print("\n\nSentential Form and Configuration of the valid strings")
    print("------------------------------------------------------")
    print("Rule 1 - S -> aSb")
    print("Rule 2 - S -> ε\n")

    p3 = Algorithm3LFCO2025JCAP()
    for s in valid_strings:
        print("------------------------------------------------------")
        print(f"String: {s}\n")
        p3.sentential(s)
        print()
        p3.configurationM(s)
        print("------------------------------------------------------\n\n")

if __name__ == "__main__":
    main()
