from .basic import add, subtract, multiply, divide
from .history import History

OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def main():
    history = History()
    print("Calculator (type 'q' to quit)")
    while True:
        line = input("> ").strip()
        if line == "q":
            break
        try:
            a, op, b = line.split()
            result = OPERATIONS[op](float(a), float(b))
        except (ValueError, KeyError) as exc:
            print(f"Error: {exc}")
            continue
        history.record(line, result)
        print(result)


if __name__ == "__main__":
    main()
