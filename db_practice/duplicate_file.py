"""
609. Find Duplicate File in System
"""

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        content_path = {}
        res = []
        
        for path in paths:
            directory_pathways = path.split(" ")
            directory, pathways = directory_pathways[0], directory_pathways[1:]
        
            for p in pathways:
                file, remainder = p.split("(")
                contents = remainder[:-1]
                if contents not in content_path:
                    content_path[contents] = []
                content_path[contents].append(directory+"/"+file)
        
        for v in content_path.values():
            if len(v) > 1:
                res.append(v)
        return res