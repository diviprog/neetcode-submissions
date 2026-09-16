class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(position[i], speed[i]) for i in range(len(position))]
        arr = sorted(arr, key=lambda e:e[0], reverse=True)
        time = [(target-position)/speed for position, speed in arr]
        stack = []
        for t in time:
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)