def sleep_in(weekday, vacation):
    """
    The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep
    in if it is not a weekday or we're on vacation. Return True if we sleep in.
    :param weekday:
    :param vacation:
    :return:
    """

    return not weekday or vacation


def front3(str):
    """
    Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3,
    the front is whatever is there. Return a new string which is 3 copies of the front.
    :param str:
    :return:
    """
    front = str[:3]
    return front + front + front
