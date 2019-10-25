# -*- coding: utf-8 -*-
"""
*****************************************************
The purpose of the module: Connection for MAPP API
*****************************************************
"""
import http.client
import urllib.parse

# Essential Parameters
Account = "api_lcd5"
APIkey = "FBA5C1C4-C736-0729-5599-D0941022A680"
Chat_No = 31414
Content_Type = 1
Message = "Python Test"

# ---Send Message---
URL = "http://mapp.innolux.com/teamplus_innolux/API/IMService.ashx?ask=sendChatMessage"
HEADER = {"Content-type":"application/x-www-form-urlencoded"}
PostData = {"account":Account, "api_key":APIkey, "chat_sn":Chat_No, "content_type":Content_Type, "msg_content":Message}
Encode_PostData = urllib.parse.urlencode(PostData)

reqconn=http.client.HTTPConnection("mapp.innolux.com")
reqconn.request(method="POST", url=URL, body=Encode_PostData, headers=HEADER)

respo=reqconn.getresponse()

#print (respo.status,  respo.reason)
#print (respo.msg)
print (respo.read())