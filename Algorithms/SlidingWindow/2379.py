#

# 本题可以看成一个长度固定为 k 的滑动窗口，我们需要计算窗口内 ‘W’ 的出现次数的最小值。
# 窗口初始位于 blocks 的长为 k 的前缀上，那么初始化 cntW 为这个前缀的 ‘W’ 的个数。然后不断向右滑动窗口，
# 如果窗口内少了 ‘W’，则 cntW 减一；如果窗口内多了 ‘W’，则 cntW 加一。
# 取滑动中的 cntW 的最小值，即为答案。

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = cur = blocks[:k].count("W")
        for in_, out in zip(blocks[k:], blocks):
            cur += (in_ == "W") - (out == "W")   #cur 记录窗口内的W个数，净出入
            ans = min(ans, cur)
        return ans       




#another way, it works but a little bit slow.
def minimumRecolors(blocks, k):
        ans = cur = k
        for i, v in enumerate(blocks):
            left = i - k + 1
            if left < 0:
                continue
            cur = blocks[left:i + 1].count("W")
            if cur < ans:
                ans = cur
            if ans == 0:
                break
        return ans

def main():
     minimumRecolors("WBBWWBBWBW", 7)

if __name__ == "__main__":
     main()
     