class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        arr = []
        for path in folder:
            if not arr or not path.startswith(arr[-1]+'/'):
                arr.append(path)
        return arr        