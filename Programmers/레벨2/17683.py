# [3차] 방금그곡
def melody(melodies):
    dic = {
        "C": "a",
        "C#": "b",
        "D": "c",
        "D#": "d",
        "E": "e",
        "F": "f",
        "F#": "g",
        "G": "h",
        "G#": "i",
        "A": "j",
        "A#": "k",
        "B": "l",
        "E#": "i",
    }
    converted = ""
    for i in range(len(melodies)):
        if i + 1 != len(melodies) and melodies[i + 1] == "#":
            converted += str(dic[melodies[i] + melodies[i + 1]])
        elif melodies[i] == "#":
            continue
        else:
            converted += str(dic[melodies[i]])
    return converted


def timer(time1, time2):
    time1 = time1.split(":")
    time2 = time2.split(":")

    h = int(int(time2[0]) - int(time1[0]))
    m = int(int(time2[1]) - int(time1[1]))

    if m < 0:
        h -= 1
        m += 60

    return int((h * 60) + m)


def solution(m, musicinfos):
    answer = []

    for i in range(len(musicinfos)):
        musicinfos[i] = musicinfos[i].split(",")

        time = timer(musicinfos[i][0], musicinfos[i][1])
        melodies = melody(musicinfos[i][3])

        while len(melodies) < time:
            if len(melodies) + len(melody(musicinfos[i][3])) < time:
                melodies += melody(musicinfos[i][3][:time])
            else:
                melodies += melody(musicinfos[i][3])
        else:
            melodies = melodies[:time]

        if melody(m) in melodies:
            answer.append([time, i])

    if len(answer) == 0:
        return "(None)"
    elif len(answer) == 1:
        return musicinfos[answer[0][1]][2]
    else:
        answer = sorted(answer, key=lambda x: (-x[0], x[1]))
        return musicinfos[answer[0][1]][2]
