class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped_index = stack.pop()
                difference = i - popped_index
                result[popped_index] = difference
            
            stack.append(i)

        return result

