#coding=utf-8
# import re
#
# # names = ["name1", "_name", "2_name", "__name__"]
# #
# # for name in names:
# #     ret = re.match("[a-zA-Z_]+[\w]*",name)
# #     if ret:
# #         print("变量名 %s 符合要求" % ret.group())
# #     else:
# #         print("变量名 %s 非法" % name)
# ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
# print(ret.group())

import time

def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    return str(environ) + '==Hello world from a simple WSGI application!--->%s\n' % time.ctime()

