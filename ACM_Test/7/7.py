TABLE_SIZE = 20011



hash_table = [[] for _ in range(TABLE_SIZE)]

def string_hash(s):
    """字符串哈希函数（64-bit rolling hash）"""
    h = 0
    P = 131
    for c in s:
        h = h * P + ord(c)
    return h  # Python int 自动溢出，相当于 mod 2^64

def insert_string(s):
    h = string_hash(s)
    idx = h % TABLE_SIZE
    BUCKET = hash_table[idx]

    for i in BUCKET:
        if i == s:
            return False
    BUCKET.append(s)
    return True

def main():
    n = int(input())
    cnt = 0

    for _ in range(n):
        s = input().strip()
        if insert_string(s):
            cnt += 1

    print(cnt)



if __name__ == '__main__':
    main()



############################################################################################

def main():
    n = int(input())
    tmp = set()

    for _ in range(n):
        s = input().strip()
        tmp.add(s)
    print(len(tmp))



if __name__ == '__main__':
    main()



