__version__ = "v2.3"

__author__ = "xzw <darkchii@qq.com>"

__language__ = {'英语': 'en', '中文': 'zh', '日语': 'jp', 'auto': 'en'}

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

    try:
        baidu_transapi_data = {
            'from': 'auto',
            'to': __language__[to],
            'query': text,
            'source': 'txt'
        }
    except KeyError:
        baidu_transapi_data = {
            'from': 'auto',
            'to': __language__['auto'],
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

            r = re.compile(r'.*?"voice":\[{.*?"(\[.+?])"}]')
            voice = r.findall(result)
            try:
                voice[0]
            except:
                pass
            else:
                phonic = ''
                for i in range(2):
                    try:
                        phonic += voice[i]
                        phonic += ' '
                    except:
                        break
                phonic = phonic.replace('"phonic"', '').replace('"en_phonic"', '').replace('"us_phonic"', '') \
                    .replace('"', '').replace(':', '').replace('{', '').replace('}', '') \
                    .replace(',', ' ')

                r = re.compile(r'{"src".*?"mean":.*?{(.+?)}}')
                results = r.findall(result)
                result = ''
                for i in range(31):
                    try:
                        result += results[i]
                    except:
                        break
                result = result.replace('"cont"', '').replace('"pre"', '').replace('"', '').replace(':', '') \
                    .replace('{', '').replace('}', '').replace('1,', '; ').replace('0,', '; ').replace(',', '') \
                    .replace('1', '').replace('0', '')
                return phonic + '\r\n' + result
    else:
        return html.json()['data'][0]['dst']
