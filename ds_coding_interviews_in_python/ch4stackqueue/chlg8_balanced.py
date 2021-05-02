from ds_coding_interviews_in_python.ch4stackqueue.stack import MyStack


def is_balanced(exp: str) -> bool:
    """
    Time complexity is O(n) since loop through list/expression once.

    :param exp: str: expression of open/closed paranthesis/brackets
    :return: bool
    """
    if len(exp) % 2 != 0:
        print("expression is not balanced because it doesn't have at least 1 closing parenthesis;")
        print("its not a balanced expression; the length is odd")
        return False

    if len(exp) == 0:
        print("empty expression, balance")
        return True

    open_list = ["[", "{", "("]
    closed_list = ["]", "}", ")"]
    s = MyStack()
    for i in range(len(exp) // 2):
        if exp[i] in open_list:
            s.push(exp[i])

    for i in range(len(exp) // 2, len(exp)):
        close_pos = closed_list.index(exp[i])
        open_pos = open_list.index(s.pop())
        if close_pos == open_pos:
            continue
        else:
            return False

    return True


def is_balanced_other_solution(exp):
    """Time complexity is O(n)"""
    closing = ["}", ")", "]"]
    stack = MyStack()
    for character in exp:
        if character in closing:
            if stack.is_empty():
                return False
            top_element = stack.pop()
            if character == "}" and top_element != "{":
                return False
            if character == ")" and top_element != "(":
                return False
            if character == "]" and top_element != "[":
                return False
        else:
            stack.push(character)
    if not stack.is_empty():
        return False
    return True
