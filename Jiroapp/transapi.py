# 提供翻译
baidu_transapi = 'http://fanyi.baidu.com/transapi'

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


# sug提供翻译单词
baidu_sug_api = 'http://fanyi.baidu.com/sug'

# sug的 data post方式
baidu_sug_data = {
    'kw': 'string'
}
'''
# 对应的输出格式
print(html.json()['data'][0]['v'])
'''


# 这个api需要验证签名 所以基本不用它
baidu_v2transapi = 'http://fanyi.baidu.com/v2transapi'

# http://fy.iciba.com
iciba_transapi = 'http://fy.iciba.com/ajax.php'

# data get方式
# 无需任何防爬策略
iciba_transapi_data = {
    'a': 'fy',
    'f': 'auto',
    't': 'auto',
    'w': '测试'
}
