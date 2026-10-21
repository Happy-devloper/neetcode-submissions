class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        stack = []
        for i in range(len(position)):
            pair.append((position[i],speed[i]))

        pair.sort(reverse=True)

        for pos,speed in pair:
            time = (target-pos)/speed
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)