# coding:utf-8

import json


path = '/Users/agnes/Desktop/支付系统.postman_collection.json'

def par_json(path):
    j_file = open(path,'rb')
    j_content = json.load(j_file)
    info = j_content['info']
    p_name = info['name']  # 项目名称
    # print(p_name)


    item = j_content['item'][0]
    api_name = item['name']     # 接口名称
    api_reqmethod = item['request']['method']       # 接口请求方式
    api_contenttype = item['request']['header'][0]['value']         # content_type
    api_body = item['request']['body']['urlencoded'][0]              # body
    aug_key = api_body['key']
    aug_value = api_body['value']
    api_url = item['request']['url']['raw']         # url

    # print(p_name,api_name,api_reqmethod,api_contenttype,aug_key,aug_value,api_url)

    return (p_name,api_name,api_reqmethod,api_contenttype,aug_key,aug_value,api_url)

# par_json(path)
print(par_json(path))