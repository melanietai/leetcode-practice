class Solution:
    def wordPatternMatch(self, p: str, s: str) -> bool:
        
        def check_match(p, s, p_map, s_map):
            if not p and not s:
                return True
            if not p or not s:
                return False
            sub_p = p[0]

            for i in range(1, len(s)+1):
                sub_s = s[:i]
                cur_p_map = dict(p_map)
                cur_s_map = dict(s_map)
                if p not in cur_p_map:
                    cur_p_map[sub_p] = sub_s
                    print(cur_p_map)
                if sub_s not in cur_s_map:
                    cur_s_map[sub_s] = sub_p
                if cur_p_map[sub_p] != sub_s or cur_s_map[sub_s] != sub_p:
                    continue
                else:
                    if check_match(p[1:], s[i:], cur_p_map, cur_s_map):

                        return True
            return False
        
        return check_match(p, s, {}, {})