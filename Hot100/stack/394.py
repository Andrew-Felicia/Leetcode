class Solution:
    def decodeString(self, s: str) -> str:
        tmp = [] #used to handle with string
        stack = []
        num = ""
        for i in s:
            if i.isdigit():
                stack.append(i)
            elif i == "[":
                stack.append(i)
            elif i.isalpha():
                stack.append(i)
            else:
                while stack and stack[-1] != "[":
                    tmp.append(stack.pop())

                stack.pop() #pop out '['

                while stack and stack[-1].isdigit():
                    num += stack.pop()
                num = num[::-1]

                #tmp = tmp.reverse() reverse method won't return anything
                tmp.reverse()
                stack.append(''.join(tmp) * int(num))
                tmp = []
                num = ""
        return ''.join(stack)
