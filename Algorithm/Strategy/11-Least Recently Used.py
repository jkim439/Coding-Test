def lru(cache, cache_size, reference):
    for ref in reference:

        # Hit
        if ref in cache:
            cache.remove(ref)
            cache.append(ref)

        # Miss
        else:
            if cache_size <= len(cache):
                cache.pop(0)
            cache.append(ref)

    return cache


print(lru([1, 2, 3, 4, 5], 5, [3, 7, 2]))
