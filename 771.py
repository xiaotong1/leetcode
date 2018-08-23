#给定J代表宝石，S表示石头
#J中字符为各不相同的，区分大小写
#输出S中含有多少个J中出现的字符
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        num=0
        for s in S:
            if s in J:
                num+=1
        return num