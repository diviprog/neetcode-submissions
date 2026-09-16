class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = list()
        operations = ['+', '-', '*', '/']

        for ch in tokens:
            if ch in operations:
                b = nums.pop()
                a = nums.pop()
                if ch == '+':
                    ans = a + b
                elif ch == '-':
                    ans = a - b
                elif ch == '*':
                    ans = a * b
                else:
                    ans = a / b
                nums.append(int(ans))
            else:
                nums.append(int(ch))
        return nums[-1]