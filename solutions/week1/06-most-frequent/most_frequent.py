def most_frequent(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1   # get returns 0 the first time we see an item

    best, best_count = None, 0                   # None is what an empty list returns
    for item in items:                           # loop over items (not counts) to keep list order
        if counts[item] > best_count:            # strict >, so a tie never replaces the leader
            best, best_count = item, counts[item]
    return best