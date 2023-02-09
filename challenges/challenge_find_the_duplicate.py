def find_duplicate(nums):
    """Retorna o número que esta duplicado...se acredita?"""
    sorted_numbers = sorted(nums)

    if len(sorted_numbers) < 2:
        return False

    for index in range(len(sorted_numbers) - 1):
        if type(sorted_numbers[index]) != int or sorted_numbers[index] < 1:
            return False

        if sorted_numbers[index] == sorted_numbers[index + 1]:
            return sorted_numbers[index]

    return False
