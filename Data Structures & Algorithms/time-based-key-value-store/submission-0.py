class TimeMap:

    def __init__(self):
        self.mydict = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mydict:
            self.mydict[key] = []
        self.mydict[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mydict:
            return ""
        arr = self.mydict[key]
        right = len(arr)-1
        left = 0
        saved =-1
        while left <= right:
            mid = (right + left)//2
            if arr[mid][0] <= timestamp:
                saved = mid
                left = mid+1
            elif arr[mid][0] > timestamp:
                right = mid-1
        if saved == -1:
            return ""
        return arr[saved][1]

        

        
