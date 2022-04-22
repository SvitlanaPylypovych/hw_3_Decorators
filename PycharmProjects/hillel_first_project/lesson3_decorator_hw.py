"""Task 1"""
# import functools
# from collections import OrderedDict
#
# import requests
#
#
# value = 0
# counter = 1
#
#
# def cache(max_limit=64):
#     def internal(f):
#         @functools.wraps(f)
#         def deco(*args, **kwargs):   # args: https://google.com     kwargs:{}
#             # try to start with args
#             cache_key = (args, tuple(kwargs.items()))
#             if cache_key in deco._cache:
#                 deco._cache[cache_key][counter] += 1
#                 return deco._cache[cache_key][value]
#
#             result = f(*args, **kwargs)
#
#             if len(deco._cache) >= max_limit:
#                 key_to_delete = min(deco._cache,
#                                     key=lambda dict_key: deco._cache[dict.key][
#                                         counter])
#                 del deco._cache[key_to_delete]
#
#             deco._cache[cache_key] = [result, 1]
#             return result
#
#         deco._cache = OrderedDict()
#         return deco
#     return internal
#
#
# @cache(max_limit=2)
# def fetch_url(url, first_n=100):
#     """Fetch a given url"""
#     res = requests.get(url)
#     return res.content[:first_n] if first_n else res.content
#
#
# print(fetch_url("https://google.com"))
# print(fetch_url("https://youtube.com"))
# print(fetch_url("https://google.com"))


"""Task 2"""
import functools
import os
import psutil

import requests


def memory(msg):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            process = psutil.Process(os.getpid())
            before = process.memory_info().rss
            result = f(*args, **kwargs)
            print(msg, f'({f.__name__}): {process.memory_info().rss - before} bytes')
            return result
        return deco
    return internal


@memory(msg="Used memory")
def fetch_url(url, first_n=1000):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


fetch_url("https://google.com")