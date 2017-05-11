def find_missing(list1, list2):
    """
    takes in two lists and compares 
    :param list1: list
    :param list2: list
    :return: int
    """
    if len(list1) == 0 and len(list2) == 0:
        return 0
    elif len(list1) == len(list2):
        return 0
    else:
        if len(list1) > len(list2):
            for i in list2:
                list1.remove(i)
            return list1[0]
        else:
            for i in list1:
                list2.remove(i)
            return list2[0]
