from requests import Session

version = 'v1.0'

baiduapi = 'http://fanyi.baidu.com/sug'
s = Session()

def baidu_translate(string):
    baidu_data = {
        'kw':string
    }
    count = 20
    while count:
        try:
            html = s.post(baiduapi,data=baidu_data,timeout=2)
        except TimeoutError:
            count -= 1
            continue
        break
    print()
    print(string)
    print()
    print('译文：')

    try:
        print(html.json()['data'][0]['v'])
    except IndexError:
        print('------抱歉！无法翻译！------')
        exit(1)

if __name__ == '__main__':
    string = input('Input:')
    baidu_translate(string=string)
