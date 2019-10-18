import time
import tkinter.messagebox
from tkinter import *
from tkinter import ttk



# 按钮事件
def button_click():
    # 按钮失效
    b1.config(state=DISABLED,text = "疯狂跑！！！")
    for i in range(11):
        bar(i*10)
    #下面是获取文本框值
    target = d_url.get()
    name = m_name.get()
    
    # 执行主程序
    #dow(target, name)
    # 完成弹出窗口提示
    messagebox.showinfo('提示', '进度条跑完啦！')
    # 激活按钮
    b1.config(state=tkinter.ACTIVE,text='让进度条跑起来')


# 进度条事件
def bar(per):
    # 更改进度值
    pb["value"] = +int(per)
    # 更新窗口
    window.update()
    # 停止0.2秒
    time.sleep(0.2)

# 程序入口
if __name__ == '__main__':
    # 程序开始窗口
    window = Tk()
    # 定义窗口名
    window.title('M3U8下载 By: Lswzw...')
    # 定义窗口大小
    window.geometry('560x140')

    # 定义标签
    Label(window, text='下载地址：', font=('Arial', 10), ).place(x=10, y=20)
    # 创建文本框变量
    d_url = StringVar()
    # 单行文本框
    url_tk = Entry(window, textvariable=d_url, show=None, width=66,)
    # 文本框位置
    url_tk.place(x=88, y=20)

    # 定义标签
    Label(window, text='文件名称：', font=('Arial', 10), ).place(x=10, y=50)
    # 创建文本框变量
    m_name = StringVar()
    # 单行文本框
    name_tk = Entry(window, textvariable=m_name, show=None, width=41)
    # 文本框位置
    name_tk.place(x=88, y=50)
    # 文本框初始值
    name_tk.insert(0, '文本框初始值')


    #按钮（直接定义位置）
    b1 = Button(window, text='让进度条跑起来', width=15, height=1,command=button_click)
    #按钮位置
    b1.place(x=425, y=50)
    
    #进度条
    pb = ttk.Progressbar(window, length=510, mode="determinate", orient=HORIZONTAL)
    pb.grid(row=1, column=1)
    #进度条位置
    pb.place(x=25, y=95)
    #进度条进度值范围
    pb["maximum"] = 100
    pb["value"] = 0

    #显示窗口
    window.mainloop()


