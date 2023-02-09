def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if not target_time:
        return None
    
    students = 0
    
    for entry, exit in permanence_period:
        if entry is None or exit is None:
            return None
        elif entry <= target_time <= exit:
            students += 1
    
    return students