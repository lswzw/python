# 下载m3u8带窗口程序
# by:Lswzw... 20190920
# 程序未完善,未做错误判断,窗口无响应问题未处理.

# 数字长度模块
import math
# 系统操作模块
import os
# 正则模块
import re
# 删除目录模块
import shutil
# 消息窗口模块
import tkinter.messagebox
# 多线程模块
from concurrent.futures import ThreadPoolExecutor
# 窗口模块
from tkinter import *
# 进度条模块
from tkinter import ttk
# 下载模块
import requests

##############
###全局变量###
##############

# 反爬浏览器头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
}

# 存储完整下载地址
dow_list = []



##############
####主程序####
##############

# 下载ts片段文件
def dowload_data(data_url):
    data = requests.get(data_url)
    name = data_url[-9:]
    # 写入片段文件
    with open('.\\bak\\' + name, 'wb') as code:
        code.write(data.content)
    # 计算进度值，取整数
    per = math.floor(abs(int(name[:-3])) * 100 / int(len(dow_list)))
    return(int(per))


# 合并ts片段文件
def merge_movie(name, movie_name):
    name = name[-9:]
    # 读出片段
    with open('.\\bak\\' + name, 'rb') as code:
        data = code.read()
    # 拼接到新文件
    with open(movie_name+'.ts', 'ab') as code:
        code.write(data)
        # 清空变量
        data = None


# 主程序
def dow_m3u8(target, movie_name, pool_num):
    # 判断目录是否存在
    os.makedirs('bak') if os.path.exists('bak') == False else None
    # 下载分析文件
    index_req = requests.get(url=target, headers=headers)
    index_url = target[:-10] + index_req.text.split()[2]
    file_req = requests.get(url=index_url, headers=headers)
    # 分析文件
    file_name_list = re.findall(',([\W\w]*?).ts', file_req.text)
    for i in file_name_list:
        # 筛选有用的行
        file_name = str(i).replace('\n', '') + '.ts'
        # 拼接下载路径
        dowload_url = index_url[:-10] + file_name
        # 把路径传递到列表里面
        dow_list.append(dowload_url)
    # 创建线程池指定最大线程数
    pool = ThreadPoolExecutor(max_workers=int(pool_num))
    # 运行多线程下载
    for per in pool.map(dowload_data, dow_list):
        # 调用bar显示进度条
        bar(per)
    # 下载片段完成 顺序合并片段文件
    for i in dow_list:
        merge_movie(i, movie_name)
    # 删除片段文件目录
    shutil.rmtree('bak')


##############
###窗口程序###
##############


# 按钮事件
def button_click():
	# 让按钮失效
    b1.config(state=DISABLED,text = '正在下载中！')
    # 更新窗口
    window.update()
    # 获取文本框数据
    target = d_url.get()
    movie_name = m_name.get()
    pool_num = p_num.get()
    # 执行主程序
    dow_m3u8(target, movie_name, pool_num)
    # 完成弹出窗口提示
    messagebox.showinfo('提示', '下载完成！')
    # 重新激活按钮
    b1.config(state=tkinter.ACTIVE,text='开始下载')


# 进度条事件
def bar(per):
    # 更改进度值
    pb["value"] = +int(per)
    # 更新窗口
    window.update()

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
    name_tk.insert(0, '电影名')

    # 定义标签
    Label(window, text='进程数：', font=('Arial', 10), ).place(x=390, y=50)
    # 创建文本框变量
    p_num = StringVar()
    # 单行文本框
    pool_tk = Entry(window, textvariable=p_num, show=None, width=14)
    # 文本框位置
    pool_tk.place(x=452, y=50)
    # 文本框初始值
    pool_tk.insert(0, '44')

    #按钮（直接定义位置）
    b1 = Button(window, text='开始下载', width=15, height=1,command=button_click)
    b1.place(x=425, y=92)

    #进度条
    pb = ttk.Progressbar(window, length=380, mode="determinate", orient=HORIZONTAL)
    pb.grid(row=1, column=1)
    #进度条位置
    pb.place(x=25, y=95)
    #进度条进度值范围
    pb["maximum"] = 100
    pb["value"] = 0

    #显示窗口
    window.mainloop()

