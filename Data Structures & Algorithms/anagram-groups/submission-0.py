class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_list = [{} for _ in range(len(strs))]

        for i in range(len(strs)):
            for char in strs[i]:
                if char in hash_list[i]:
                    hash_list[i][char] += 1
                else:
                    hash_list[i][char] = 1
        seen_hashes = []
        solution = []
        for j in range(len(hash_list)):
            if hash_list[j] not in seen_hashes:
                temporary_list = []
                temporary_list.append(strs[j])
                seen_hashes.append(hash_list[j])
                for k in range(j+1, len(hash_list)):
                    if hash_list[j] == hash_list[k]:
                        temporary_list.append(strs[k])
                solution.append(temporary_list)
        return solution






