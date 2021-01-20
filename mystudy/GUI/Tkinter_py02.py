#!/usr/bin/env python 
#-*- coding:utf-8 -*-

from tkinter import *
import json,base64,time,pyperclip
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("文本处理工具_v1.2")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="待处理数据")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="商户私钥")
        self.log_label.grid(row=12, column=0)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=12)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=67, height=35)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=10, columnspan=10)
        self.mch_data_Text = Text(self.init_window_name, width=66, height=9)  # 商户私钥输入框
        self.mch_data_Text.grid(row=13, column=0, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=12, columnspan=10)
        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="ts加签名", bg="lightblue", width=10,command=self.str_trans_to_ts)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=2, column=11)

        self.str_trans_to_ts_button = Button(self.init_window_name, text="ts加签名_list", bg="lightblue", width=10,command=self.str_trans_ts_list)
        self.str_trans_to_ts_button.grid(row=3, column=11)

        self.str_trans_copy_button = Button(self.init_window_name, text="复制结果", bg="lightblue", width=10,command=self.result_copy)
        self.str_trans_copy_button.grid(row=5, column=11)

    def result_copy(self):
        pyperclip.copy(self.result_data_Text.get(1.0,END))

    #功能函数
    def str_trans_to_ts(self):
        rsa_private_key = self.mch_data_Text.get(1.0,END)
        src = json.loads(self.init_data_Text.get(1.0,END).strip().replace("\n",""))
        if src:
            try:
                singn = tng_signdata_rsa(private_key=rsa_private_key, sign_data=src)
                #输出到界面
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,singn)
                self.write_log_to_Text("INFO:str_trans_to_ts success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"ts加签失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_ts failed")

    def str_trans_ts_list(self):
        rsa_private_key = self.mch_data_Text.get(1.0,END)
        src = json.loads(self.init_data_Text.get(1.0,END).strip().replace("\n",""))
        if src:
            try:
                singn = tng_signdata_rsa_List(private_key=rsa_private_key, sign_data=src,redata_list='txnList')
                #输出到界面
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,singn)
                self.write_log_to_Text("INFO:str_trans_to_ts success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"ts加签失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_ts failed")


    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)

def tng_signdata_rsa(private_key,sign_data):
    sign_data.pop('sign')  #删除字段sign
    data_sort = dict(sorted(sign_data.items(),key=lambda x:x[0],reverse=False))  #对字典进行从小到大排序
    #sign_data_url = urlencode(data_sort).encode('utf-8')
    sign_data_1 = dictstr(data_sort).encode('utf-8')   #把待加密数据转成QueryString的格式
    private_keyBytes = base64.b64decode(private_key)
    priKey = RSA.importKey(private_keyBytes)
    signer = PKCS1_v1_5.new(priKey)
    hash_obj = SHA256.new()
    hash_obj.update(sign_data_1)
    #hash_obj.update(sign_data_url)
    signature = base64.b64encode(signer.sign(hash_obj))
    sign = signature.decode("utf-8")
    sign_data['sign'] = sign
    return json.dumps(sign_data,sort_keys=True, indent=2)   #格式化输出json数据

#带内嵌列表的参数加签
def tng_signdata_rsa_List(private_key,sign_data,redata_list):
    listda = sign_data[redata_list]
    sign_data_1 = dictstr_List(sign_data[redata_list][0])
    sign_data[redata_list] = sign_data_1
    sign_data.pop('sign')  #删除字段sign
    data_sort = dict(sorted(sign_data.items(),key=lambda x:x[0],reverse=False))  #对字典进行从小到大排序
    sign_data_2 = dictstr(data_sort).encode('utf-8')
    private_keyBytes = base64.b64decode(private_key)
    priKey = RSA.importKey(private_keyBytes)
    signer = PKCS1_v1_5.new(priKey)
    hash_obj = SHA256.new()
    hash_obj.update(sign_data_2)
    signature = base64.b64encode(signer.sign(hash_obj))
    sign = signature.decode("utf-8")
    sign_data['sign'] = sign
    sign_data[redata_list] = listda
    return json.dumps(sign_data,sort_keys=True, indent=2)

def dictstr(dict1):
    ss = []
    for key,value in dict1.items():
        if value == "":
            pass
        else:
            k = key
            v = str(value)
            a = k + '=' + v
            ss.append(a)
            ss.append('&')
    del ss[-1]
    return "".join(ss)

def dictstr_List(dict1):
    data_sort = dict(sorted(dict1.items(), key=lambda x:x[0], reverse=False))
    ss = []
    for key,value in data_sort.items():
        if value == "":
            pass
        else:
            k = key
            v = str(value)
            a = k + '=' + v
            ss.append(a)
            ss.append('&')
    del ss[-1]
    return "[{" + "".join(ss) + "}]"


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()