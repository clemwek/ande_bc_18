def data_type(arg):
    """
    This function take one argument. Compare 
    and return results, based on the 
    argument supplied to the function
    :param arg: any data type
    :return: vary depending on the input
    """
    try:
        if arg is None:
            return 'no value'
        elif type(arg) == list:
            if len(arg) >= 3:
                return arg[2]
            else:
                return None
        elif type(arg) == bool:
            return arg
        elif type(arg) == str:
            return len(arg)
        elif type(arg) == int:
            if arg < 100:
                return 'less than 100'
            elif arg == 100:
                return 'equal to 100'
            else:
                return 'more than 100'
    except Exception as e:
        raise e
