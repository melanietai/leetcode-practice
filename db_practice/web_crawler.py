# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        visited = set()
        visited.add(startUrl)
        
        def get_hostname(url):
            temp = url.split("//")[1]
            hostname = temp.split("/")[0]
            return hostname
        
        def dfs(url):
            urls = htmlParser.getUrls(url)
            for url in urls:
                if url not in visited and get_hostname(startUrl) == get_hostname(url):
                    visited.add(url)
                    dfs(url)
        
        dfs(startUrl)
        return visited
            