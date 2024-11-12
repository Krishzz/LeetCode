class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        sorted_items = sorted(items, key=lambda x:x[1], reverse=True)
        arr = []
        for query in queries:
            for item in sorted_items:
                if item[0] <= query:
                    arr.append(item[1])
                    break
            else:
                arr.append(0)
        return arr