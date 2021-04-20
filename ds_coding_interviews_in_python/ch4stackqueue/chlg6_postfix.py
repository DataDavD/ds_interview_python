from ds_coding_interviews_in_python.ch4stackqueue.stack import Stack


def eval_post_fix(exp: str) -> int:
    """
    Evaluates postfix math expression.


    :param exp: postfix string expression to be evaluated, no whitespace
    :return: integer result of evaluated exp
    """
    stack = Stack()
    try:
        for char in exp:
            if char.isdigit():
                stack.push(char)
            else:
                right = stack.pop()
                left = stack.pop()
                stack.push(str(eval(left + char + right)))

        return int(float(stack.pop()))
    except TypeError as te:
        print("Invalid sequence provided")
        raise te
