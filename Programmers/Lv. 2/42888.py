# 오픈채팅방
def solution(record):
    record = [s.split() for s in record]
    name = dict()
    answer = []

    for i in range(len(record) - 1, -1, -1):
        if record[i][0] != "Leave" and record[i][1] not in name:
            name[record[i][1]] = record[i][2]

    for r in record:
        if r[0] == "Enter":
            answer.append(name[r[1]] + "님이 들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(name[r[1]] + "님이 나갔습니다.")

    return answer
