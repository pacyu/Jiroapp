from requests import Session
from bs4 import BeautifulSoup
import re

version = 'v0.0.8'

url = 'https://www.baidu.com/s'

User_Agent = 'Chrome/64.0.3282.168'  # 改为自己使用的浏览器

headers = {
    'User-Agent': User_Agent,
}

s = Session()

'''
利用百度搜索的特点：
把输入的词加上'百度翻译'进行关键字搜索
就可以翻译英文句子了
'''
def English2Chinese(word=''):
    params = {
        'wd': word + ' 百度翻译',
    }

    count = 20
    while count:
        try:
            html = s.get(url=url, params=params, headers=headers, timeout=2, )
        except TimeoutError:
            count -= 1
            continue
        break

    if count == 0:
        print('请求超时，可能是您当前网络环境不稳定，建议到网络良好的地方使用！')
        exit(4)

    soup = BeautifulSoup(html.text, 'lxml')

    # 单词的翻译在span标签中
    tags = soup.find_all('span')

    # 英文句子的翻译在html页面中的位置不一样 在p标签中
    p_tags = soup.find_all('p', attrs={'class': 'op_sp_fanyi_line_two'})

    r = re.compile(r'"(op_dict.+?)">')
    classAttributeList = r.findall(str(tags))  # 通过正则匹配tags中包含字符串‘op_dict’的字符串

    # 在所有的span标签下再通过 classAttributeList 缩小查找范围
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

    # 单词或短语的翻译
    r = re.compile(r'op_dict_text2">(.*?)</span>', re.S)
    translatorOfChinese = r.findall(str(taglist))

    # 长句子的中文翻译
    r = re.compile(r'op_sp_fanyi_line_two">(.*?)<', re.S)
    long_sentence_translatorOfChinese = r.findall(str(p_tags))

    print()
    print('原文:' + word)
    print()
    print('译文:')
    print()
    # 如果搜索结果页面没有翻译会出现数组溢出错误
    # 利用这一点来判断是否能翻译而进行异常处理
    try:
        translatorOfChinese[0]
    except:
        try:
            long_sentence_translatorOfChinese[0]
        except:
            print('------I am sorry!Can not translated!------')
            exit(2)
        else:
            print(long_sentence_translatorOfChinese[0].replace('\n', '').replace(' ', ''))

    else:
        # 多个词性
        for i in range(8):
            try:
                print(nature[i] + '  ' + translatorOfChinese[i].replace('\n', '').replace(' ', ''))
            except:
                break


'''
可翻译部分中文词语、短句
但没考虑到多音字的情况
虽然也可以输出多音字
但没有显示区分输出
'''
def Chinese2English(word=''):
    redundancy = ['双语例句','汉英大词典','中中释义','进行更多翻译']
    params = {
        'wd': word + ' 英文',
    }

    count = 20
    while count:
        try:
            html = s.get(url=url, params=params, headers=headers, timeout=2, )
        except TimeoutError:
            count -= 1
            continue
        break

    if count == 0:
        print('请求超时，可能是您当前网络环境不稳定，建议到网络良好的地方使用！')
        exit(4)

    soup = BeautifulSoup(html.text, 'lxml')
    # span_tags = soup.find_all('span', attrs={'class':'op_dict_exp'})

    a_tags = soup.find_all('a', attrs={'hidefocus': 'true'})
    p_tags = soup.find_all('p', attrs={'class': 'op_sp_fanyi_line_two'})

    '''
    # 获取单词出自
    r = re.compile(r'op_dict_exp">(.+?)<')
    wordfroms = r.findall(str(span_tags))
    '''

    # 字或词语翻译
    r = re.compile(r'<a.*?>(.+?)<')
    translatorOfEnglish = r.findall(str(a_tags))

    # 短句翻译
    r = re.compile(r'op_sp_fanyi_line_two">(.+?)<', re.S)
    short_sentence_translatorOfEnglish = r.findall(str(p_tags))

    print()
    print('原文:' + word)
    print()
    print('译文:')
    print()

    try:
        short_sentence_translatorOfEnglish[0]
    except:
        try:
            translatorOfEnglish[0]
        except:
            print('------对不起!无法翻译!------')
            exit(3)
        else:
            '''修改日志 原本这里是这样写的：
            # 单词类的会匹配到多余的最后3个：[双语例句 汉英大词典 中中释义] 所以截取掉
            if len(translatorOfEnglish) > 4:
                for i in range(len(translatorOfEnglish[:-4])):
                    print(translatorOfEnglish[i] + ';')
            else:
                print(translatorOfEnglish[0] + ';')
            '''
            # 有时会匹配到多余的几个：[双语例句 汉英大词典 中中释义 进行更多翻译]。所以截取掉
            for i in range(len(translatorOfEnglish)):
                if translatorOfEnglish[i] in redundancy:
                    break
                print(translatorOfEnglish[i] + ';')
    else:
        # 英文句子中含有一个空格 所以这里用两个以避免英文句子中的空格也被替换掉
        print(short_sentence_translatorOfEnglish[0].replace('\n', '').replace('  ', ''))


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
判断输入单词是否是合法的英文
'''
def is_English(word):
    flag = False
    for ch in word:
        if ' ' <= ch <= '~':
            flag = True
        else:
            flag = False
            break

    return flag


if __name__ == '__main__':
    word = input('Input:')

    if is_English(word):
        English2Chinese(word=word)
    elif is_Chinese(word):
        Chinese2English(word=word)
    else:
        print('输入有误!')
        exit(1)
