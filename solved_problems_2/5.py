def leg_count_in_longest_sequence(legs):
    maximum, result, counter = -1, -1, 1
    for i in range(0, len(legs) - 1):
        if legs[i] == legs[i + 1]:
            counter += 1
        elif counter > maximum:
            maximum = counter
            result = legs[i]
            counter = 1
        else:
            counter = 1
    if counter > maximum:
        result = legs[-1]
    return result
