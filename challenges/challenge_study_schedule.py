def study_schedule(permanence_period, target_time=None):
    try:
        valid(target_time)

        counter = 0
        for period in permanence_period:
            valid(period[0])
            valid(period[1])

            if period[0] <= target_time <= period[1]:
                counter += 1
        return counter

    except TypeError:
        return None


def valid(hour):
    if not (type(hour) == int and 0 <= hour < 24):
        raise TypeError
