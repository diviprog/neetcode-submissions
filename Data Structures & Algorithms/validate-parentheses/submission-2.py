class Solution:
    def isValid(self, s: str) -> bool:
        brackets = list()
        for char in s:
            if char == "(" or char == "[" or char == "{":
                brackets.append(char)
            if char == ")":
                if not brackets or brackets[-1] != "(":
                    return False
                else:
                    brackets.pop(-1)
            elif char == "}":
                if not brackets or brackets[-1] != "{":
                    return False
                else:
                    brackets.pop(-1)
            elif char == "]":
                if not brackets or brackets[-1] != "[":
                    return False
                else:
                    brackets.pop(-1)
        if not brackets:
            return True
        else:
            return False