# Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be closed in the correct order, for
# example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.

class solution:
    def validParenthesis(self, str1):
        stack, pchar = [], {"(": ")", "[": "]", "{": "}"}

        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0


print(solution().validParenthesis("({})[[]]"))
print(solution().validParenthesis("({})[[]"))
