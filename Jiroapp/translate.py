__version__ = "v2.0"

__author__ = "xzw <darkchii@qq.com>"

__language__ = {'英语': 'en', '中文': 'zh', '日语': 'jp', '': 'zh', 'auto': 'zh'}

from requests import Session
from Jiroapp import transapi
import re


s = Session()


def baidu_translate(text='', to=''):
    """
    :param text: type content
    :param to: auto Chinese
    :return: translate result
    """
    global html

    baidu_transapi_data = {
        'from': 'auto',
        'to': __language__[to],
        'query': text,
        'source': 'txt'
    }

    count = 20
    while count:
        try:
            html = s.post(transapi.baidu_transapi, data=baidu_transapi_data, timeout=2)
        except TimeoutError:
            count -= 1
            continue
        break

    if count == 0:
        return '您当前的环境网络不稳定，建议到网络良好的环境下使用！'

    try:
        html.json()['data']
    except (IndexError, ValueError, KeyError):
        try:
            html.json()['result']
        except (IndexError, ValueError, KeyError):
            return '翻译失败！'
        else:
            result = html.json()['result']
            r = re.compile(r'{"src".+?"mean":.*?"cont":{(.*?)}}')
            result = r.findall(result)
            return result[0].replace('"', '').replace(':1,', '; ').replace(':0,', '; ') \
                .replace(':0', '').replace(':1', '')
    else:
        return html.json()['data'][0]['dst']
