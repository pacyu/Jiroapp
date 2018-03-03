from Jiroapp import translate
from tkinter.ttk import Combobox
from tkinter import *

__copyright_info__ = '©2018 darkchii'


class JiroApplication(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        self.pack()
        self.create_window()

    def create_window(self):
        # 在窗口中创建子窗口
        type_content_box = Text(self.master, width=54, height=10, font=('微软雅黑', 12), )
        type_content_box.insert(END, '在此处输入文字、网址 即可翻译', )
        type_content_box.pack(side=LEFT)

        # 控制编辑区域显示的滚动条
        scb = Scrollbar(self.master, )
        scb.pack(side=RIGHT, fill=Y, expand=True)
        scb.config(command=type_content_box.yview)

        # 子窗口的兄弟窗口
        trans_result_box = Label(self.master, width=56, height=11, bg='#D3D3D3',
                                 font=('consolas', 11), )
        trans_result_box.pack(side=RIGHT)

        # 自动检测语言
        auto_language = Button(self.master, text='    自动检测语言    ', state='disabled', relief='flat',
                               bg='#ffffff', fg='#000000', font=('微软雅黑', 11), )
        auto_language.place(x=5, y=90)

        # 选择语言
        language = StringVar()
        language_chosen = Combobox(self.master, width=12, textvariable=language, )
        language_chosen['values'] = ['中文', '英语', '日语']  # 设置下拉列表的值
        language_chosen.place(x=25 * 7, y=100)
        language_chosen.current(0)

        # 显示翻译结果
        def show_trans_result():
            global translate_result

            # 运行结果按钮状态:正在翻译
            runtime_after = Button(self.master, text='正在翻译', state=DISABLED, width=10, relief='flat', bg='#ffffff',
                                   fg='#000000', font=('微软雅黑', 11), )
            runtime_after.place(x=72 * 7 - 7, y=90)

            if type_content_box.count('1.0', 'end-1c') > tuple([0]):
                translate_result = translate.baidu_translate(text=type_content_box.get('1.0', 'end-1c'), to=language.get())

            # 在翻译结果区域显示结果
            trans_result_box.configure(text=translate_result)

            # 运行结果按钮状态:运行结果
            runtime_after.config(text='运行结果')

        # 翻译按钮
        translate_button = Button(self.master, text='翻   译', width=10, bg='#6495ED', fg='#ffffff',
                                  relief='flat', command=lambda: show_trans_result(),
                                  font=('微软雅黑', 11), )
        translate_button.place(x=55 * 7 + 5, y=90)

        # 底部版权信息
        copyright = Label(self.master, text=__copyright_info__, font=('consolas', 11), )
        copyright.place(x=(960 - len(__copyright_info__) * 7.5) / 2,
                        y=480 - 22)


WIDTH = 960
HEIGHT = 480

app_name = 'Jiro ' + translate.__version__ + ' ' + translate.__author__

root = Tk()

# 窗口标题
root.title(app_name)

# 设置窗口透明度 第二个参数数值越小则越透明
root.attributes('-alpha', 0.90)

# 窗口大小、居中
root.geometry('{}x{}+{}+{}'.format(str(WIDTH), str(HEIGHT), str(int((root.winfo_screenwidth() - WIDTH) / 2)),
                                   str(int((root.winfo_screenheight() - HEIGHT) / 2))))
root.deiconify()

# 固定窗口大小
root.resizable(0, 0)

app = JiroApplication(root)

app.mainloop()
