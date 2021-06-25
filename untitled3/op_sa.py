import tkinter
import tkinter.filedialog

def FileOpen():
    r= tkinter.filedialog.askopenfilename(title = "python",filetypes = [('python','*.py*.pyw'),('all files',"*")])
    print(r)
def FileSave():
    r = tkinter.filedialog.askopenfilename(title = 'python',initialdir = r'D')
    print(r)

root = tkinter.Tk()
botton1 = tkinter.Button(root,text ="打开文件",command = FileOpen)
botton1.pack(side = 'left')
button2 = tkinter.Button(root,text = '保存文件',command = FileSave)
button2.pack(side = 'left')
root.mainloop()