from collections import defaultdict
class Solution:
    paths = []
    def dist_check(self, a, b):
        dist = 0
        for i in range(len(a)):
            if a[i] != b[i] and dist == 0:
                dist = 1
            elif a[i] != b[i] and dist == 1:
                return False
        if dist == 1:
            return True
    
    def get_shortest_paths(self, graph, start, goal, path = []):
        
        if start not in path:
            if goal in graph[start]:
                new_path = path+[start]+[goal]
                if len(self.paths) == 0 or (len(self.paths[-1]) == len(new_path) and self.paths[-1] != new_path):
                    self.paths.append(new_path)
                else:
                    if len(self.paths[-1]) > len(new_path):
                        self.paths = [new_path]
                
                # print(path+[start]+[goal])
                return
            else:
                for neighbor in graph[start]:
                    if neighbor not in path:
                        self.get_shortest_paths(graph, neighbor, goal, path+[start])
                    
        else:
            return
        
                
         
            
        
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        ladder_adj_list = defaultdict(set)
        res_list = wordList
        print(res_list)
        if beginWord not in res_list:
            res_list.insert(0,beginWord)
        # if endWord not in res_list:
        #     res_list.append(endWord)
        for word in res_list:
            for word2 in res_list:
                if word != word2:
                    if self.dist_check(word, word2):
                        ladder_adj_list[word].add(word2)
        # print(ladder_adj_list)
        self.get_shortest_paths(ladder_adj_list, beginWord, endWord)
        return self.paths