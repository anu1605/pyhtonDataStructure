from stack import Stack


def print_result_of(equation_str):

    stackList = Stack(len(equation_str))
    operator = None
    first_operand = None
    second_operand = None
    result = None
    pair_found = False

    for letter in equation_str:
        if letter == "(":
            pair_found = False
            continue
        elif letter == ")":
            pair_found = True

        if not pair_found:
            if letter.isdigit():
                if letter.find(".") == -1:
                    stackList.push(int(letter))
                else:
                    stackList.push(float(letter))
            else:
                stackList.push(letter)

        else:
            second_operand = stackList.pop()

            operator = stackList.pop()
            first_operand = stackList.pop()

            if operator == "+":
                result = first_operand + second_operand
            elif operator == "-":
                result = first_operand - second_operand
            elif operator == "*":
                result = first_operand * second_operand
            elif operator == "/":
                result = first_operand / second_operand
            elif operator == "%":
                result = first_operand % second_operand

            stackList.push(result)
            pair_found = False
    return result


print(print_result_of("((6+((4*3)/3))/2)"))
