# coding:utf-8

import locust
from locust import TaskSet, task, HttpLocust
# from locust.contrib.fasthttp import FastHttpLocust
import random
import json
import requests
import import_json

path = '/Users/agnes/Desktop/支付系统.postman_collection.json'

def api01(self):
    headers = {"Content-Type":import_json.par_json(path)[3]}

    param='{"params": {"albums": [{"uniqueKey": "1_channel_live_4986","sourceId": 1,"type": "channel_live"},{"uniqueKey":"1_channel_live_398","sourceId": 1,"type": "channel_live"},{"uniqueKey": "1_channel_live_4995","sourceId": 1,"type": "channel_live"}],"userId": "test","collectFlag": 1}}'
    with self.client.post(import_json.par_json(path)[2],import_json.par_json(path)[6],data=json.dumps(param),headers = headers) as response:
        result=(response.content)
        Result = str(result,encoding='utf-8')
        if response.status_code !=200:
            print (result)
            response.failure("Failed!")
        else:
                #       print ("returncode:0,expect Result equal to the acutal Result",Result)
            pass



class UserBehavior(TaskSet):
        tasks = {api01:1}


class UserBehavior(HttpLocust):
    host = import_json.par_json(path)[6]
    #       host = 'http://10.10.0.3:9067'
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 1000
