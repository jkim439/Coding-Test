def kmp(s, f):
    table = [0] * len(f)
    i = 0
    for j in range(1, len(f)):
        while i > 0 and f[i] != f[j]:
            i = table[i - 1]

        if f[i] == f[j]:
            i += 1
            table[j] = i

    answer = []
    i = 0
    for j in range(len(s)):
        while i > 0 and f[i] != s[j]:
            i = table[i - 1]

        if f[i] == s[j]:
            i += 1
            if i == len(f):
                answer.append(j - i + 1)
                i = table[i - 1]

    return answer


print(kmp("xabxxbaxbaxbaxbaxabxbaxbabx", "abx"))
print(kmp("abababab", "abab"))
