#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkiot.request.v20180120.RegisterDeviceRequest import RegisterDeviceRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-shanghai')

request = RegisterDeviceRequest()
request.set_accept_format('json')

request.set_ProductKey("ProductKey")
request.set_DeviceName("DeviceName")
request.set_DevEui("DevEui")
request.set_PinCode("PinCode")
request.set_Nickname("Nickname")

response = client.do_action_with_exception(request)
# python2:  print(response) 
print(response)
