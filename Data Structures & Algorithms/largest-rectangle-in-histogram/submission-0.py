class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        area = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                popped_index = stack.pop()
                if not stack:
                    length = i
                else:
                    length = i - stack[-1]-1
                    
                area = max(length*heights[popped_index], area)
            stack.append(i)
        return area