# import logging

# logging.basicConfig(level=logging.DEBUG, filename='test.log', filemode='w', format='We have a problem: %(asctime)s : %(levelname)s : %(message)s')
# logging.debug('debug')
# logging.info("info")
# logging.warning('warning')
# logging.error('error')
# logging.critical("critical")


# if 2+2 ==4:
#     print("так, дорівнює")

# assert 2+2 == 4, "nepravulno"


# """
# >>> 2+2
# 4
# """
#
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()


def adder(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for i in kwargs.values():
        result += i
    return result
