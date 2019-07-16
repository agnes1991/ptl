# coding:utf-8

import json


path = '/Users/agnes/Desktop/支付系统.postman_collection.json'



# 获取接口参数个数
file= open(path,'rb')
api_file = json.load(file)
api_name = api_file['item']
num= len(api_name)
print('num=',len(api_name))

i=0

def json(api_file,i):
    item = api_file['item'][i]
    p_name = item['name']
    req_method = item['request']['method']
    req_header = item['request']['header'][0]['value']
    p_body = item['request']['body']
    p_domain = 'http://'+item['request']['url']['host'][0]+'.'+item['request']['url']['host'][1]+'.'+item['request']['url']['host'][2]+'.'+item['request']['url']['host'][3]
    p_uri = item['request']['url']['path'][0]+"/"+item['request']['url']['path'][1]+item['request']['url']['path'][2]+"/"+item['request']['url']['path'][3]+"?"
    # print(p_body)
    # print(item)
    return (p_name,req_method,req_header,p_body,p_domain,p_uri)


def p_body(i):
    body = api_file['item'][i]['request']['body']
    print('body=',body)
    return body

print(p_body(i))

while i < num:
    print(json(api_file,i))
    i +=1