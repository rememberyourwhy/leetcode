"""
num =
s = ""
count = 1
s_num = str(num)
for i in range(1, len(s_num)):
    if s_num[i] == s_num[i - 1]:
        count += 1
    elif s_num[i] != s_num[i - 1]:
        s += str(count) + str(s_num[i - 1])
        count = 1

s += str(count) + str(s_num[len(s_num) - 1])
s_num = s
print(s)
"""
class Solution:
    def count_and_say(n):
        if n != 1:
            return Solution.next_count_and_say(Solution.count_and_say(n - 1))
        else:
            return 11
    def next_count_and_say(num):
        s_num = str(num)
        count = 1
        s = ""
        for index in range(1, len(s_num)):
            if s_num[index] == s_num[index - 1]:
                count += 1
            else:
                s += str(count) + str(s_num[index - 1])
                count = 1
        s += str(count) + str(s_num[-1])
        return int(s)
n = 9
print(Solution.count_and_say(n))
for i in range(1, 20):
    input()
    print(Solution.count_and_say(i))
