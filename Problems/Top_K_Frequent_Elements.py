class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        o = []

        print(nums)
        for i in nums:
            if i not in d:
                d[i] = nums.count(i)
            else:
                pass
        
        d = dict(sorted(d.items(), key=lambda x: x[1],reverse = True))

        ky = list(d.keys())
        print(ky)

        for j in range(k):
            o.append(ky[j])
            

        return o
