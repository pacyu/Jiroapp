# Translator
> **这是一个使用 `python` 编写的翻译器.**

# 用到的技术
* 目前程序用到`requests`、`BeautifulSoup`包。
> 以后还会添加界面、程序打包.exe文件等功能，彼时我将添加上。
* 百度搜索引擎

# 声明
> 程序为个人学习、研究而开发，程序翻译结果皆来自百度搜索引擎，本人对产生的后果概不负责。

# Version update log
* 最初版本
  + [v0.0.1](translator.py)

* v0.0.6版
  + <sup>1</sup>[v0.0.6](E2C&C2E.py)
  增加了英文句子翻译、部分中文词语翻译、检测输入是否合法功能。
  修改了异常处理、部分变量名。

* [v0.0.8版](transApp.py)
  + 修改日志:
  原代码中165 ~ 171行:
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

# 旁注释义
[1]: 原文件名：E2C&C2E.py 已修改为 transApp.py
