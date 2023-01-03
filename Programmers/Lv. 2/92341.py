# 주차 요금 계산
def solution(fees, records):
    default_min, default_fee, add_min, add_fee = fees
    cars_time = dict()
    cars_fee = dict()

    for r in records:
        time, number, _ = r.split()
        if number not in cars_time:
            cars_time[number] = [time]
            cars_fee[number] = 0
        else:
            cars_time[number].append(time)

    for number, time in cars_time.items():
        final = 0
        for i in range(len(time)):
            if i % 2 == 1:
                hour = int(time[i][:2]) - int(time[i - 1][:2])
                minute = int(time[i][3:]) - int(time[i - 1][3:])
                if minute < 0:
                    hour -= 1
                    minute += 60
                total = (hour * 60) + minute
                final += total
            if i % 2 == 0 and i == len(time) - 1:
                hour = int(23) - int(time[i][:2])
                minute = int(59) - int(time[i][3:])
                if minute < 0:
                    hour -= 1
                    minute += 60
                total = (hour * 60) + minute
                final += total
        cars_time[number] = final

        fee = default_fee
        if (final - default_min) > 0:
            if (final - default_min) % add_min != 0:
                final += add_min - ((final - default_min) % add_min)
            fee += (final - default_min) // add_min * add_fee

        cars_fee[number] = fee

    return [i[1] for i in sorted(cars_fee.items())]
