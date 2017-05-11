"""binary search """


class BinarySearch(list):
    """
    Binary search class
    """
    def __init__(self, a, b):
        """
        sets up the class when its created
        :param a: int
        :param b: int
        """
        data = [b]
        list_len = 1
        while list_len < a:
            data.append(data[list_len - 1] + b)
            list_len += 1
        super(BinarySearch, self).__init__(data)
        self.length = len(data)

    def search(self, number):
        """
        take in an argument and searches through the list
        :param number: int
        :return: dictionary
        """
        count = 0
        first = 0
        self.length = len(self)
        last = self.length - 1
        mid_point = int((last) / 2)
        obj_location = {'count': '', 'index': ''}
        while first < mid_point:

            if (first == mid_point) and (self[first] > number):
                index = -1
                obj_location["count"] = self.length
                obj_location["index"] = index
                return obj_location

            elif self[first] == number:
                index = first
                obj_location["count"] = count
                obj_location["index"] = index
                return obj_location
            elif self[last] == number:
                index = last
                obj_location["count"] = count
                obj_location["index"] = index
                return obj_location
            elif self[mid_point] == number:
                index = mid_point
                obj_location["count"] = count
                obj_location["index"] = index
                return obj_location
            else:
                if self[mid_point] > number:
                    last = mid_point - 1
                    first = first + 1
                    mid_point = (last + first) // 2
                else:
                    first = mid_point + 1
                    last = last - 1
                    mid_point = ((last + first) // 2) + 1
            count += 1
        obj_location = {'count': count, 'index': -1}
        return obj_location
