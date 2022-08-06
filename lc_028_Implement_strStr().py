class Implement_strStr:
    def __main__(x, s):
        #special condition
        if len(s) < len(x):
            return -1

        for i in range(len(s)- len(x) + 1):
            if x[0] == s[i]:
                if x == s[i: i+ len(x)]:
                    return i
        return -1

s = "ptdangiunhattrendoi"
x = "dangiunhattrendoi"
print(Implement_strStr.__main__(x, s))
