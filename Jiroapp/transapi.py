# 提供翻译
baidu_transapi = 'http://fanyi.baidu.com/transapi'

# sug提供翻译单词
baidu_sug_api = 'http://fanyi.baidu.com/sug'

# 这个api需要验证签名 所以我基本不用它
baidu_v2transapi = 'http://fanyi.baidu.com/v2transapi'

# sug的 data post方式
baidu_sug_data = {
    'kw': 'string'
}
'''
# 对应的输出格式
print(html.json()['data'][0]['v'])
'''

# data post方式
baidu_transapi_data = {
    'from': 'en',
    'to': 'zh',
    'query': 'string',
    'source': 'txt'
}
'''
# 对应的输出格式
print(html.json()['data'][0]['dst'])
'''
