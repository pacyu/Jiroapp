from requests import Session
from Jiroapp import transapi
import re

version = 'v1.2'

s = Session()

language = {'英语':'en','中文':'zh','日语':'jp','':'zh'}

def baidu_translate(string,to='中文'):
    '''
    :param string: 通过输入接收
    :return: void
    '''

    baidu_transapi_data = {
        'from':'auto',
        'to':language[to],
        'query':string,
        'source':'txt'
    }

    count = 20
    while count:
        try:
            html = s.post(transapi.baidu_transapi,data=baidu_transapi_data,timeout=2)
        except TimeoutError:
            count -= 1
            continue
        break

    if count == 0:
        print('您当前的环境网络不稳定，建议到网络良好的环境下使用!')
        exit(1)

    print()
    print(string)
    print()
    print('译文：')
    print()

    try:
        html.json()['data']
    except:
        try:
            html.json()['result']
        except (IndexError,ValueError,KeyError):
            print('------抱歉！无法翻译！------')
            exit(1)
        else:
            result = html.json()['result']
            r = re.compile(r'{"src".+?"mean":.*?"cont":{(.*?)}}')
            result = r.findall(result)
            print(result[0].replace('"','').replace(':1,','; ').replace(':0','; '))
    else:
        print(html.json()['data'][0]['dst'])

if __name__ == '__main__':
    string = input('输入:')
    if string != '':
        to = input('选择输出语言 [\'英语\',\'中文\',\'日语\']:')
        baidu_translate(string=string,to=to)
