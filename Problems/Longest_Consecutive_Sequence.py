class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        '''if len(nums)==1:
            return 1
        elif len(set(nums))==1:
            return 1
        else:
            s_nums = sorted(nums)
            n_return = []
            print(s_nums)

            for i in range(len(s_nums)-1):
                if s_nums[i] == s_nums[i+1]:
                    pass
                elif s_nums[i] + 1 == s_nums[i+1]:
                    n_return.append(s_nums[i])
                    if i+1 == len(s_nums)-1:
                        n_return.append(s_nums[i+1])
                else:
                    n_return.append(s_nums[i])
                    break

            print(n_return)
            return len(n_return)'''

        set_nums = set(nums)
        print(set_nums)
        longest_seq = 0

        for num in set_nums:
            if num-1 not in set_nums:
                current_num = num
                long_seq = 1

                while current_num + 1 in set_nums:
                    current_num += 1
                    long_seq += 1
                
                longest_seq = max(long_seq, longest_seq)

        return longest_seq
