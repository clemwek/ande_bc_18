def find_max_min(list_in):
    """
    Takes in a list and returns a list of maximum and minimum 
    elements
    :param list_in: list of int
    :return: list of max and min or length else returns error
    """
    try:
        max_item = max(list_in)
        min_item = min(list_in)
        if max_item != min_item:
            return [min_item, max_item]
        else:
            return [max_item]
    except Exception as e:
        return e
