class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        def dfs(a, ori_list, temp):
            ori_list.remove(a)
            for i in accounts[a][1:]:
                temp.add(i)
                for j in email_dict[i]:
                    if j in ori_list:
                        dfs(j, ori_list, temp)
            return ori_list, temp
        
        res = []
        email_dict = dict()
        for i in range(len(accounts)):
            for j in accounts[i][1:]:
                if j not in email_dict:
                    email_dict[j] = [i]
                else:
                    email_dict[j] += [i]               
        ori_list = list(range(len(accounts)))
        while len(ori_list)>0:           
            temp = set()
            res+=[[accounts[ori_list[0]][0]]]
            ori_list, temp = dfs(ori_list[0], ori_list, temp)
            res[-1]+=sorted(temp)
        return res
            
    
