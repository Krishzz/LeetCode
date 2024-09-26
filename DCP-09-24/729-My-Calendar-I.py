class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> bool:
        for st,en in self.arr:
            if st<end and start<en:
                return False
        self.arr.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)