class MyCalendarTwo:

    def __init__(self):
        self.arr = []
    def book(self, start: int, end: int) -> bool:
        flg = 0
        for st, en in self.arr:
            if start<en and end>st:
                new_start = max(st, start)
                new_end = min(en, end)
                if self.find(new_start, new_end):
                    return False
        self.arr.append((start,end))
        return True
    
    def find(self, start, end):
        ct = 0
        for sat,ed in self.arr:
            if start<ed and end>sat:
                ct+=1
                if ct==2:
                    return True
        return False

        
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)