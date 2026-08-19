class Solution:
    def restoreIpAddresses(self, s: str):
        res = []

        def backtrack(start, path):
            # If we already have 4 parts but haven't consumed all digits → invalid
            if len(path) == 4:
                if start == len(s):      # all digits used → valid IP
                    res.append(".".join(path))
                return

            # Each part can have length 1 to 3
            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start : start + length]

                # Rule 1: No leading zeros
                if part[0] == "0" and length > 1:
                    break

                # Rule 2: Value must be 0–255
                if int(part) > 255:
                    break

                backtrack(start + length, path + [part])

        backtrack(0, [])
        return res

        