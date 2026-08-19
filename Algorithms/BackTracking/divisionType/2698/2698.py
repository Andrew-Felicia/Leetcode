#generate all possible partion of n, with this output below:
#input: 296 
#output:  [[2,9,6],[296],[2,96],[29,6]]
def punishmentNumberRec(n):
    if n < 10:
        return [[n]]
    else:
        result = []
        s = str(n)
        first = int(s[0])
        remaning = int(s[1:])
        for elem in punishmentNumberRec(remaning):
            result.append([first] + elem)
            result.append([int(str(first)+str(elem[0]))] + elem[1:])
        return result
        
# s = punishmentNumberRec(96)
# print(s)

# s1 = punishmentNumberRec(2025)
# print(s1)
#[[2, 2, 5], [22, 5], [2, 25], [225]]
# int based recursive function is bad! write string based function instead!



#generate all possible partion of n, with this output below:
#input: '296' 
#output:  [[2,9,6],[296],[2,96],[29,6]]
def punishmentNumberRec(n):
    if not n:
        return []
    if len(n) == 1:
        return [[int(n)]]
    else:
        result = []
        first = n[0]
        for elem in punishmentNumberRec(n[1:]):
            result.append([int(first)] + elem)
            result.append([int(first+str(elem[0]))] + elem[1:])
        return result
# s2 = punishmentNumberRec("2025")
# print(s2)
# #[[2, 0, 2, 5], [20, 2, 5], [2, 2, 5], [22, 5], [2, 0, 25], [20, 25], [2, 25], [225]]

# s3 = punishmentNumberRec("025")
# print(s3)
#[[0, 2, 5], [2, 5], [0, 25], [25]]
#it's also bad!



#generate all possible partion of n, with this output below:
#input: '296' 
#output:  [['2','9','6'],['296'],['2','96'],['29','6']]
def punishmentNumberRec(n):
    if not n:
        return []
    if len(n) == 1:
        return [[n]]
    else:
        result = []
        first = n[0]
        for elem in punishmentNumberRec(n[1:]):
            result.append([first] + elem)
            result.append([first+elem[0]] + elem[1:])
        return result
s4 = punishmentNumberRec("2025")
print(s4)
#[['2', '0', '2', '5'], ['20', '2', '5'], ['2', '02', '5'], ['202', '5'],
#  ['2', '0', '25'], ['20', '25'], ['2', '025'], ['2025']]



class Solution:
    def punishmentNumber(self, n: int) -> int:
        #return true or flase, return if s can be partitioned and sum up to 
        #target
        def dfs(s, idx, cur_sum, target):
            # prune
            if cur_sum > target:
                return False

            # reached end
            if idx == len(s):
                return cur_sum == target

            num = 0
            for j in range(idx, len(s)):
                num = num * 10 + int(s[j])
                if dfs(s, j + 1, cur_sum + num, target):
                    return True
            return False

        result = 0
        for i in range(1, n + 1):
            sq = str(i * i)
            if dfs(sq, 0, 0, i):
                result += i * i

        return result
