import tkinter
from tkinter import *

top = tkinter.Tk()# 生成一个主窗口对象
menu = tkinter.Menu(top)
submenu = tkinter.Menu(menu,tearoff = 0)
submenu.add_command(label = '打开')
submenu.add_command(label = '保存')
submenu.add_command(label = '关闭')
menu.add_cascade(label = '文件',menu = submenu)
submenu = tkinter.Menu(menu,tearoff = 0)
submenu.add_command(label = '复制')
submenu.add_command(label = '粘贴')
submenu.add_command(label = '剪切')
submenu.add_separator()
menu.add_cascade(label = '编辑',menu = submenu)
submenu = tkinter.Menu(menu,tearoff = 0)
submenu.add_command(label = '关于')
menu.add_cascade(label = '帮助',menu = submenu)
top.config(menu = menu)
class Mainwindow:
    def __init__(self):
        self.frame = Tk()

        self.label_name = Label(self.frame,text= 'name:')
        self.label_age =Label(self.frame,text = 'age:')
        self.label_sex = Label(self.frame, text='sex:')

        self.text_name = Text(self.frame,height = '1',width='30')
        self.text_age  = Text(self.frame,height = '1',width = '30')
        self.text_sex = Text(self.frame,height = '1',width = '30')

        self.label_name.grid(row = 0 ,column = 0)
        self.label_age.grid(row = 1,column = 0)
        self.label_sex.grid(row = 2,column = 0)

        self.text_name.grid(row = 0 ,column = 1)
        self.text_age.grid(row = 1 ,column = 1)
        self.text_sex.grid(row = 2 ,column = 1)
        self.button_ok = Button(self.frame,text = "ok",width = 10)
        self.button_cancel = Button(self.frame,text = 'cancel',width =10)
        self.button_ok.grid(row = 3,column = 0)
        self.button_cancel.grid(row = 3,column = 1)


        self.frame.mainloop()


frame = Mainwindow()
# 实例化组件

label = tkinter.Label(top ,text= "python,tkinter")
label.pack() # 将标签添加到窗口中
button1 = tkinter.Button(top,text='按钮1' )
button2 = tkinter.Button(top,text='按钮2')
button2.pack(side = tkinter.RIGHT)
# 添加至左右2端
button1.pack(side = tkinter.LEFT)
















# 进入循环
top.mainloop()