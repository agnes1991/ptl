# coding:utf-8

import locust
from locust import TaskSet, task, HttpLocust
# from locust.contrib.fasthttp import FastHttpLocust
import random
import json
import requests
import orignalfile_par

path = '/Users/agnes/Desktop/支付系统.postman_collection.json'

def api01(self):
    headers = {"Content-Type":orignalfile_par.par_json(path)[3]}

    param=orignalfile_par.par_json(6)
    with self.client.post(orignalfile_par.par_json(path)[2], orignalfile_par.par_json(path)[4], headers=headers) as response:
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
    host = orignalfile_par.par_json(path)[4]
    #       host = 'http://10.10.0.3:9067'
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 1000
