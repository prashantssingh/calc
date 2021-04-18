# Prashant Singh
# 1001773374
# 04/06/2021
# macOS Mojave v10.14.6

# NOTE that I have implemented unary operation -- negation(!) and modulo division(%) below.
# dictionary of operands to function:
operator_dict = {
    "+": (lambda op1, op2: op2 + op1),
    "-": (lambda op1, op2: op1 - op2),
    "*": (lambda op1, op2: op1 * op2),
    "/": (lambda op1, op2: op1 / op2),
    "!": (lambda op: -op),
    "%": (lambda op1, op2: op2 % op1)
}

def convert_to_rpn(expr):
    precedence = {
        "(": 0,
        "!": 1,
        "+": 2,
        "-": 2,
        "*": 3,
        "/": 3,
        "%": 3
    }

    operand_stack = list()
    rpn = list()
    tokens = expr.split()

    for token in tokens:
        if token.isnumeric():
            rpn.append(token)
        elif token == '(':
            operand_stack.append(token)
        elif token == ')':
            stack_top = operand_stack.pop()
            while stack_top != '(':
                rpn.append(stack_top)
                stack_top = operand_stack.pop()
        else:
            while operand_stack and (precedence[operand_stack[-1]] >= precedence[token]):
                rpn.append(operand_stack.pop())
            operand_stack.append(token)

    while operand_stack:
        rpn.append(operand_stack.pop())
    
    return " ".join(rpn)

def tokenize(rpn):
    return rpn.split()

def calculate(rpn):
    tokens = tokenize(rpn)
    stack = list()
    try:
        for token in tokens:
            if token in operator_dict:
                if token == "!":
                    result = operator_dict[token](stack.pop())
                    stack.append(result)
                else:
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

def get_expr():
    try:
        exprs = []
        with open('input_RPN_EC.txt') as expr_files:
            for line in expr_files:
                exprs.append(line)

        return exprs

    except Exception as ex:
        print(f"Exception: {ex}")

def main():
    exprs = get_expr()
    for expr in exprs:
        rpn = convert_to_rpn(expr)
        result = calculate(rpn)
        print(f"RPN expression: {rpn}")
        print(f"Result: {result}")

if __name__ == "__main__":
    main()