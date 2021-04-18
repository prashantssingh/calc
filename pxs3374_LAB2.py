# Prashant Singh
# 1001773374
# 04/06/2021
# macOS Mojave v10.14.6

# dictionary of operands to function:
operator_dict = {
    "+": (lambda a, b: b + a),
    "-": (lambda a, b: b - a),
    "*": (lambda a, b: b * a),
    "/": (lambda a, b: b / a)
}

def tokenize(rpn):
    return rpn.split()

def calculate(rpn):
    tokens = tokenize(rpn)
    stack = list()
    try:
        for token in tokens:
            if token in operator_dict:
                if len(stack) < 2:
                    raise f"Expression: {rpn} \nError: insufficient values in expression"
                
                operand1, operand2 = stack.pop(), stack.pop()
                result = operator_dict[token](operand1, operand2)
                stack.append(result)
            else:
                stack.append(float(token))

        return stack.pop()

    except Exception as ex:
        print(ex)

def get_RPN():
    try:
        rpns = []
        with open('input_RPN.txt') as rpn_files:
            for line in rpn_files:
                rpns.append(line)

        return rpns

    except Exception as ex:
        print(f"Exception: {ex}")

def main():
    rpns = get_RPN()
    print(rpns)

    for rpn in rpns:
        result = calculate(rpn)
        print(f"Expression: {rpn}, Result: {result}")

if __name__ == "__main__":
    main()