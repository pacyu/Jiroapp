# Translator
> **This is a use `python` implemented translator.**

# Version update log
* 最初版本
 * [v0.0.1](translator.py)

* v0.0.6版
 * [v0.0.6](E2C&C2E.py)
增加了英文句子翻译、部分中文词语翻译、检测输入是否合法功能。
修改了异常处理、部分变量名。

* v0.0.8版
 * 修改日志:
原代码中166 ~ 172行:
```python
# 单词类的会匹配到多余的最后3个：[双语例句 汉英大词典 中中释义] 所以截取掉
if len(translatorOfEnglish) > 4:
    for i in range(len(translatorOfEnglish[:-4])):
        print(translatorOfEnglish[i] + ';')
else:
    print(translatorOfEnglish[0] + ';')
```
改为：
```python
# 有时会匹配到多余的几个：[双语例句 汉英大词典 中中释义 进行更多翻译]。所以截取掉
for i in range(len(translatorOfEnglish)):
    if translatorOfEnglish[i] in redundancy:
        break
    print(translatorOfEnglish[i] + ';')
```
其中redundancy是一个新添加的列表变量：`redundancy = ['双语例句','汉英大词典','中中释义','进行更多翻译']`
