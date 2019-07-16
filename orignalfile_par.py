# coding:utf-8

import json


path = '/Users/agnes/Desktop/支付系统.postman_collection.json'



# 获取接口参数个数
file= open(path,'rb')
api_file = json.load(file)
api_name = api_file['item']
num= len(api_name)
print(len(api_name))
print(api_file)


# for i in len(api_name):
#     print(i)
n=0
def par_json(path,n):
    j_file = open(path,'rb')
    j_content = json.load(j_file)
    info = j_content['info']
    p_name = info['name']  # 项目名称
    # print(p_name)


    """
    对原始json进行解析，从中将接口名称、接口请求方式，请求头，请求body，请求域名，请求路径分别取出来
    并对域名和路径进行拼接
    """
    item = j_content['item'][0]
    api_name = item['name']     # 接口名称
    api_reqmethod = item['request']['method']       # 接口请求方式
    api_contenttype = item['request']['header'][0]['value']         # content_type
    body = item['request']['body']['urlencoded']              # body
    # aug_key = api_body['key']
    # aug_value = api_body['value']
    api_domain = 'http://'+item['request']['url']['host'][0]+'.'+item['request']['url']['host'][1]+'.'+item['request']['url']['host'][2]+'.'+item['request']['url']['host'][3]         # url
    api_path = item['request']['url']['path'][0]+"/"+item['request']['url']['path'][1]+item['request']['url']['path'][2]+"/"+item['request']['url']['path'][3]+"?"

    """
    循环取请求参数key和value，并分别赋值给aug_key,aug_value
    """

    # i =0
    aug_key = []
    aug_value = []
    while n < 5:
        aug_key.append(body[n]['key'])
        aug_value.append(body[n]['value'])
        n = n+1
    # print(aug_value,aug_key)
    # print(aug_key[0],aug_value[0])

    """
    循环将上面所取的key和value，组合成所需要的参数形式
    body=key1+value1&key2=value2&......
    """

    param = []
    api_body = ""
    while n < 5:
        # print(aug_key,aug_value)
        param.append((aug_key[n],aug_value[n]))
        # print("param=",param)
        body_signal = param[n][0]+"="+param[n][1]+"&"
        api_body = body_signal+api_body
        n +=1
    # body = param[0][0]+"="+param[0][1]+"&"+param[1][0]+"="+param[1][1]
    # print("param=",param)
    # print("body=",body_total)


    # print(p_name,api_name,api_reqmethod,api_contenttype,api_url)

    return (p_name,api_name,api_reqmethod,api_contenttype,api_domain,api_path,api_body)

# par_json(path)


while n < num:
    print(par_json(path,n))
    n+=1