# [카카오 인턴] 수식 최대화
from itertools import permutations
import copy


def solution(expression):
    nums = [""]
    for i, c in enumerate(expression):
        if c in ["+", "-", "*"]:
            nums.append(c)
            nums.append("")
        else:
            nums[-1] += c

    exps = set([e for e in expression if e.isdigit() is False])
    exps = list(permutations(exps, len(exps)))

    ans = []

    for exp in exps:
        temp1 = copy.deepcopy(nums)
        temp2 = []
        for e in exp:

            while temp1:
                poped = str(temp1.pop(0))

                if poped == e:
                    evalstr = str(temp2.pop()) + str(poped) + str(temp1.pop(0))
                    temp2.append(eval(evalstr))
                else:
                    temp2.append(poped)

            temp1 = copy.deepcopy(temp2)
            temp2 = []

        ans.append(abs(temp1[0]))

    return max(ans)
