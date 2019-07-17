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
    # 接口名称
    p_name = item['name']
    # 请求方式
    req_method = item['request']['method']
    # 请求头
    req_header = item['request']['header'][0]['value']
    # 域名
    p_domain = 'http://'+item['request']['url']['host'][0]+'.'+item['request']['url']['host'][1]+'.'+item['request']['url']['host'][2]+'.'+item['request']['url']['host'][3]
    # 路径
    p_uri = item['request']['url']['path'][0]+"/"+item['request']['url']['path'][1]+item['request']['url']['path'][2]+"/"+item['request']['url']['path'][3]+"?"
    # print(p_body)
    # print(item)


    # 循环取参数的key和value，分别存在数组中
    body = item['request']['body']['urlencoded']
    l_body = len(body)
    y=0
    aug_key = []
    aug_value = []
    while y < l_body:
        aug_key.append(body[y]['key'])
        aug_value.append(body[y]['value'])
        y = y + 1


    # 将上面取出的参数key和value加起来，成为完整的接口参数所需形式
    param = []
    p_body = ""
    x=0
    while x < l_body:
        # print(aug_key,aug_value)
        param.append((aug_key[x], aug_value[x]))
        # print("param=",param)
        body_signal = param[x][0] + "=" + param[x][1] + "&"
        p_body = body_signal + p_body
        x += 1

    return (p_name,req_method,req_header,p_domain,p_uri,p_body)



while i < num:
    print(json(api_file,i))
    i +=1