def study_schedule(permanence_period, target_time):
    """Retornará a quantidade de estudades no mesmo horários forncecido"""
    if not target_time:
        return None

    students = 0

    for entry, exit in permanence_period:
        if type(entry) != int or type(exit) != int:
            return None
        elif entry <= target_time <= exit:
            students += 1

    return students
