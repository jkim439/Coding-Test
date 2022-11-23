# [1차] 캐시
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    time = 0
    cache = []
    cities = list(map(lambda x: x.lower(), cities))

    for city in cities:

        # Hit
        if city in cache:
            cache.pop(cache.index(city))
            cache.append(city)
            time += 1

        # Miss
        else:
            if cacheSize <= len(cache):
                cache.pop(0)
            cache.append(city)
            time += 5

    return time
