#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkiot.request.v20180120.QueryProductTopicRequest import QueryProductTopicRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-hangzhou')

request = QueryProductTopicRequest()
request.set_accept_format('json')

request.set_ProductKey("ProductKey")

response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
