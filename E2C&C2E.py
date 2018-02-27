from requests import get
from bs4 import BeautifulSoup
import re

url = 'https://www.baidu.com/s'

User_Agent = '' # 改为自己使用的浏览器

headers = {
    'User-Agent': User_Agent,
}

def English2Chinese(word=''):
    params = {
        'wd': word,
    }

    html = get(url, params=params, headers=headers, timeout=2, )
    # print(html.status_code)

    soup = BeautifulSoup(html.text, 'lxml')
    # print(soup.prettify())

    tags = soup.find_all('span')  # 找到所有span标签

    r = re.compile(r'"(op_dict.+?)">')
    classAttributeList = r.findall(str(tags))  # 通过正则匹配tags中包含字符串‘op_dict’的字符串

    taglist = soup.find_all('span', attrs={
        'class': classAttributeList
    })
    '''
    # 查看获取的标签
    for tag in taglist:
        print(tag)
    '''

    # 国家
    r = re.compile(r'"op_dict3_font14 op_dict3_gap_small">(.+?)</span>')
    nation = r.findall(str(taglist))

    # 发音
    r = re.compile(r'"op_dict3_font16 op_dict3_gap_small">(.+?)</span>')
    pronunciation = r.findall(str(taglist))

    # 词性
    r = re.compile(r'"op_dict_text1 c-gap-right">(.+?)</span>')
    nature = r.findall(str(taglist))

    # 中文翻译
    r = re.compile(r'op_dict_text2">(.*?)</span>', re.S)
    translatorOfChinese = r.findall(str(taglist))

    print()
    print(word)
    print()

    # 如果搜索结果页面没有翻译会出现数组溢出错误
    # 利用这一点来判断是否能翻译而退出程序
    try:
        print(nation[0] + ' ' + pronunciation[0] + ' ' + nation[1] + ' ' + pronunciation[1])
    except:
        print('------Sorry!The word can not be translated!------')
        exit(2)

    # 多个词性
    for i in range(8):
        try:
            print(nature[i] + '  ' + translatorOfChinese[i].replace('\n','').replace(' ',''))
        except:
            break

def Chinese2English(word=''):
    params={
        'wd':word + ' 英文',
    }

    html = get(url, params=params, headers=headers, timeout=2, )

    soup = BeautifulSoup(html.text, 'lxml')
    # span_tags = soup.find_all('span', attrs={'class':'op_dict_exp'})
    a_tags = soup.find_all('a',attrs={'hidefocus':'true'})[:-4]

    '''
    # 获取单词出自
    r = re.compile(r'op_dict_exp">(.+?)<')
    wordfroms = r.findall(str(span_tags))
    '''

    # 英文翻译
    r = re.compile(r'<a.*?>(.+?)<')
    translatorOfEnglish = r.findall(str(a_tags))

    print()
    print(word)
    print()

    try:
        translatorOfEnglish[0]
    except:
        print('------对不起!这个词语无法翻译!------')
        exit(3)

    for i in range(len(translatorOfEnglish)):
        print(translatorOfEnglish[i] + ';')

'''
判断输入词是否是合法的中文词语
'''
def is_Chinese(word):
    flag = False
    for ch in word:
        if u'\u4e00' <= ch <= u'\u9fff':
            flag = True
        else:
            flag = False
            break

    return flag

'''
判断输入单词是否是合法的英文单词
'''
def is_English(word):
    flag = False
    for ch in word:
        if 'A' <= ch <= 'z':
            flag = True
        else:
            flag = False
            break

    return flag

if __name__ == '__main__':
    word = input('Input an English word:')

    if is_English(word):
        English2Chinese(word=word)
    elif is_Chinese(word):
        Chinese2English(word=word)
    else:
        print('输入有误!')
        exit(1)
