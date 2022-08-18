class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_map = {}
        for p in paths:
            d = p.split(" ")
            root = d[0]
            files = d[1:]
            for f in files:
                file_name, content = f.split("(")[0], f.split("(")[1][:-1]
                if content not in file_map:
                    file_map[content] = []
                file_map[content].append(root+"/"+file_name)
        res = []
        for v in file_map.values():
            if len(v) > 1:
                res.append(v)
        return res