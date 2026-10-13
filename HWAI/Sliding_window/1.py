import sys



def main():
    s = sys.stdin.readline().strip()
    #print(s)
    n = len(s)
    if n < 1:
        return
    if n == 1:
        print(1)
        return

    window = set()
    ans = 0
    left = 0
    # for i in range(n):
    #     if s[i] not in window:
    #         window.add(s[i])
    #     else:
    #         while s[i] in window:
    #             window.remove(s[left])
    #             left += 1
    #         window.add(s[i])
    #     ans = max(ans, i - left + 1)
    for i in range(n):
        while s[i] in window:
            window.remove(s[left])
            left += 1
        window.add(s[i])
        ans = max(ans, i - left + 1)
    print(ans)






if __name__ == "__main__":
    main()