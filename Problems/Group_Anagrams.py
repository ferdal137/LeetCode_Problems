class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''
        n = []
        output = []
        aux = []
        
        for i in strs:
            n.append(tuple(sorted(i)))

        s = set(n)
        for tupla in s:
            for word in strs:
                if tupla == tuple(sorted(word)):
                    aux.append(word)
            output.append(aux)
            aux = []
        
        return output'''

        output = []
        groups = {}

        for word in strs:
            key = tuple(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        for group in groups.values():
            output.append(group)

        return output
