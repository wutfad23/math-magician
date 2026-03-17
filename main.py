#
# Math Magician Main File
# usage: math operator operand1 operand2
def add(a, b):
    return a + b



def main():
    import sys
    print("Welcome to Math Magician!")

    if len(sys.argv) != 4:
        print("usage: math operator operand1 operand2")
        sys.exit(1)

    op = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])

    if op == "add" or op == "+":
        print(f"Result: {add(a, b)}")
    else:
        print(f"Unknown operator: {op}")

if __name__ == "__main__":
    main()
