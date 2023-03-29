#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###########################################################################
# Write  : 2023-03-05
# Author : 刘天龙
# File   : 中间件漏洞测试工具集
###########################################################################
import wx
import os
import wx.lib.buttons as buttons
import subprocess
from setting import java8_path
from setting import java11_path
from setting import java9_path


class jar_management_gui(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"中间件漏洞测试工具集", pos=wx.DefaultPosition,
                          size=wx.Size(490, 700), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetBackgroundColour(wx.WHITE)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetTransparent(510)
        gui_all = wx.BoxSizer(wx.VERTICAL)

        # 一、Tomcat漏洞测试工具
        gui_Tomcat = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Tomcat漏洞测试工具"), wx.VERTICAL)
        Tomcat = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)
        dingwei=100




        self.c20230327202501 = wx.Button(gui_Tomcat.GetStaticBox(), wx.ID_ANY, u"CNVD-2020-10487", wx.DefaultPosition,size=(220, 23))
        Tomcat.Add(self.c20230327202501, 0, wx.ALL, 4)
        self.c20230327202502 = wx.Button(gui_Tomcat.GetStaticBox(), wx.ID_ANY, u"CVE-2021-41773", wx.DefaultPosition,size=(220, 23))
        Tomcat.Add(self.c20230327202502, 0, wx.ALL, 4)
        gui_Tomcat.Add(Tomcat, 1, wx.EXPAND, 4)
        gui_all.Add(gui_Tomcat, 0, wx.EXPAND | wx.ALL, 4)

        # 二、Weblogic漏洞测试工具
        gui_Weblogic = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"WebLogic漏洞测试工具"), wx.VERTICAL)
        Weblogic = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)
        dingwei=200

        self.c20230327202503 = wx.Button(gui_Weblogic.GetStaticBox(), wx.ID_ANY, u"Weblogic-FrameWork",wx.DefaultPosition, size=(220, 23))
        Weblogic.Add(self.c20230327202503, 0, wx.ALL, 4)
        self.c20230327202504 = wx.Button(gui_Weblogic.GetStaticBox(), wx.ID_ANY, u"shell利用工具-by-21superman", wx.DefaultPosition,size=(220, 23))
        Weblogic.Add(self.c20230327202504, 0, wx.ALL, 4)
        self.c20230327202505 = wx.Button(gui_Weblogic.GetStaticBox(), wx.ID_ANY, u"JAVA反序列化-by-rebeyond",wx.DefaultPosition,size=(220, 23))
        Weblogic.Add(self.c20230327202505, 0, wx.ALL, 4)
        self.c20230327202506 = wx.Button(gui_Weblogic.GetStaticBox(), wx.ID_ANY, u"反序列化漏洞测试工具-by-shack2",wx.DefaultPosition,size=(220, 23))
        Weblogic.Add(self.c20230327202506, 0, wx.ALL, 4)
        gui_Weblogic.Add(Weblogic, 1, wx.EXPAND, 4)
        gui_all.Add(gui_Weblogic, 0, wx.EXPAND | wx.ALL, 4)

        # 三、Jboss漏洞测试工具
        gui_Jboss = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Jboss漏洞测试工具"), wx.VERTICAL)
        Jboss = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)
        dingwei=300


        self.c20230327202507 = wx.Button(gui_Jboss.GetStaticBox(), wx.ID_ANY, u"Jboss反序列化工具-by-6哥", wx.DefaultPosition,size=(220, 23))
        Jboss.Add(self.c20230327202507, 0, wx.ALL, 4)
        self.c20230327202508 = wx.Button(gui_Jboss.GetStaticBox(), wx.ID_ANY, u"Ysoserial-Master反序列化", wx.DefaultPosition,size=(220, 23))
        Jboss.Add(self.c20230327202508, 0, wx.ALL, 4)
        gui_Jboss.Add(Jboss, 1, wx.EXPAND, 4)
        gui_all.Add(gui_Jboss, 0, wx.EXPAND | wx.ALL, 4)

        # 四、Jenkins漏洞测试工具
        gui_Jenkins = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Jenkins漏洞测试工具"), wx.VERTICAL)
        Jenkins = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)
        dingwei=400

        self.c20230327202509 = wx.Button(gui_Jenkins.GetStaticBox(), wx.ID_ANY, u"CVE-2017-1000353", wx.DefaultPosition,size=(220, 23))
        Jenkins.Add(self.c20230327202509, 0, wx.ALL, 4)
        self.c20230327202510 = wx.Button(gui_Jenkins.GetStaticBox(), wx.ID_ANY, u"CVE-2018-1000861", wx.DefaultPosition,size=(220, 23))
        Jenkins.Add(self.c20230327202510, 0, wx.ALL, 4)
        gui_Jenkins.Add(Jenkins, 1, wx.EXPAND, 4)
        gui_all.Add(gui_Jenkins, 0, wx.EXPAND | wx.ALL, 4)

        # 五、Shiro漏洞测试工具
        gui_Shiro = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"shiro漏洞测试工具"), wx.VERTICAL)
        Shiro = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)
        dingwei=500

        self.c20230327202511 = wx.Button(gui_Shiro.GetStaticBox(), wx.ID_ANY, u"shiro反序列化利用工具v2.2", wx.DefaultPosition,size=(220, 23))
        Shiro.Add(self.c20230327202511, 0, wx.ALL, 4)
        self.c20230327202512 = wx.Button(gui_Shiro.GetStaticBox(), wx.ID_ANY, u"ShiroExp-by-Safe6Sec", wx.DefaultPosition,size=(220, 23))
        Shiro.Add(self.c20230327202512, 0, wx.ALL, 4)
        self.c20230327202513 = wx.Button(gui_Shiro.GetStaticBox(), wx.ID_ANY, u"Shiro反序列化回显工具v2.3", wx.DefaultPosition,size=(220, 23))
        Shiro.Add(self.c20230327202513, 0, wx.ALL, 4)
        self.c20230327202514 = wx.Button(gui_Shiro.GetStaticBox(), wx.ID_ANY, u"Shiro Exploit-by-天下大木头", wx.DefaultPosition,size=(220, 23))
        Shiro.Add(self.c20230327202514, 0, wx.ALL, 4)
        self.c20230327202515 = wx.Button(gui_Shiro.GetStaticBox(), wx.ID_ANY, u"Shiro反序列化检测工具", wx.DefaultPosition,size=(220, 23))
        Shiro.Add(self.c20230327202515, 0, wx.ALL, 4)
        self.c20230327202516 = wx.Button(gui_Shiro.GetStaticBox(), wx.ID_ANY, u"Shiro550-721-by-飞鸿", wx.DefaultPosition,size=(220, 23))
        Shiro.Add(self.c20230327202516, 0, wx.ALL, 4)
        self.c20230327202517 = wx.Button(gui_Shiro.GetStaticBox(), wx.ID_ANY, u"无CC链依赖利用工具-by-NoCC", wx.DefaultPosition,size=(220, 23))
        Shiro.Add(self.c20230327202517, 0, wx.ALL, 4)
        self.c20230327202518 = wx.Button(gui_Shiro.GetStaticBox(), wx.ID_ANY, u"增强版-by-SummerSec-by3", wx.DefaultPosition,size=(220, 23))
        Shiro.Add(self.c20230327202518, 0, wx.ALL, 4)
        gui_Shiro.Add(Shiro, 1, wx.EXPAND, 4)
        gui_all.Add(gui_Shiro, 0, wx.EXPAND | wx.ALL, 4)

        # 六、Struts2漏洞测试工具
        gui_Struts2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Struts2漏洞测试工具"), wx.VERTICAL)
        Struts2 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)
        dingwei=600

        self.c20230327202519 = wx.Button(gui_Struts2.GetStaticBox(), wx.ID_ANY, u"K8-Struts2-EXP",wx.DefaultPosition, size=(220, 23))
        Struts2.Add(self.c20230327202519, 0, wx.ALL, 4)
        self.c20230327202520 = wx.Button(gui_Struts2.GetStaticBox(), wx.ID_ANY, u"S2全版本漏洞检测工具-by-ABC_123", wx.DefaultPosition,size=(220, 23))
        Struts2.Add(self.c20230327202520, 0, wx.ALL, 4)
        self.c20230327202521 = wx.Button(gui_Struts2.GetStaticBox(), wx.ID_ANY, u"Struts2全版本漏洞测试工具17.6",wx.DefaultPosition, size=(220, 23))
        Struts2.Add(self.c20230327202521, 0, wx.ALL, 4)
        self.c20230327202522 = wx.Button(gui_Struts2.GetStaticBox(), wx.ID_ANY, u"Struts2漏洞检查工具V2.3-by-shack2",wx.DefaultPosition,size=(220, 23))
        Struts2.Add(self.c20230327202522, 0, wx.ALL, 4)
        gui_Struts2.Add(Struts2, 1, wx.EXPAND, 4)
        gui_all.Add(gui_Struts2, 0, wx.EXPAND | wx.ALL, 4)

        # 七、增加与删除程序
        gui_increase = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"增删程序"), wx.VERTICAL)
        increase = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)
        self.c20230327202523 = wx.Button(gui_increase.GetStaticBox(), wx.ID_ANY, u"+", wx.DefaultPosition,size=(220, 23))
        increase.Add(self.c20230327202523, 0, wx.ALL, 4)
        self.c20230327202524 = wx.Button(gui_increase.GetStaticBox(), wx.ID_ANY, u"-", wx.DefaultPosition,size=(220, 23))
        increase.Add(self.c20230327202524, 0, wx.ALL, 4)
        gui_increase.Add(increase, 1, wx.EXPAND, 4)
        gui_all.Add(gui_increase, 0, wx.EXPAND | wx.ALL, 4)


        self.SetSizer(gui_all)
        self.Layout()
        self.Centre(wx.BOTH)
        self.c20230327202503.Bind(wx.EVT_BUTTON, self.c20230327202503_click)
        self.c20230327202504.Bind(wx.EVT_BUTTON, self.c20230327202504_click)
        self.c20230327202505.Bind(wx.EVT_BUTTON, self.c20230327202505_click)
        self.c20230327202506.Bind(wx.EVT_BUTTON, self.c20230327202506_click)
        self.c20230327202507.Bind(wx.EVT_BUTTON, self.c20230327202507_click)
        self.c20230327202508.Bind(wx.EVT_BUTTON, self.c20230327202508_click)
        self.c20230327202501.Bind(wx.EVT_BUTTON, self.c20230327202501_click)
        self.c20230327202502.Bind(wx.EVT_BUTTON, self.c20230327202502_click)
        self.c20230327202509.Bind(wx.EVT_BUTTON, self.c20230327202509_click)
        self.c20230327202510.Bind(wx.EVT_BUTTON, self.c20230327202510_click)
        self.c20230327202511.Bind(wx.EVT_BUTTON, self.c20230327202511_click)
        self.c20230327202512.Bind(wx.EVT_BUTTON, self.c20230327202512_click)
        self.c20230327202513.Bind(wx.EVT_BUTTON, self.c20230327202513_click)
        self.c20230327202514.Bind(wx.EVT_BUTTON, self.c20230327202514_cilck)
        self.c20230327202515.Bind(wx.EVT_BUTTON, self.c20230327202515_click)
        self.c20230327202516.Bind(wx.EVT_BUTTON, self.c20230327202516_click)
        self.c20230327202517.Bind(wx.EVT_BUTTON, self.c20230327202517_click)
        self.c20230327202518.Bind(wx.EVT_BUTTON, self.c20230327202518_click)
        self.c20230327202519.Bind(wx.EVT_BUTTON, self.c20230327202519_click)
        self.c20230327202520.Bind(wx.EVT_BUTTON, self.c20230327202520_click)
        self.c20230327202521.Bind(wx.EVT_BUTTON, self.c20230327202521_click)
        self.c20230327202522.Bind(wx.EVT_BUTTON, self.c20230327202522_click)
        self.c20230327202523.Bind(wx.EVT_BUTTON, self.c20230327202523_click)
        self.c20230327202524.Bind(wx.EVT_BUTTON, self.c20230327202524_click)
        dingwei=700






        def __del__(self):pass
        def c20230327202503_click(self, event): event.Skip()
        def c20230327202504_click(self, event): event.Skip()
        def c20230327202505_click(self, event): event.Skip()
        def c20230327202506_click(self, event): event.Skip()
        def c20230327202507_click(self, event): event.Skip()
        def c20230327202508_click(self, event): event.Skip()
        def c20230327202501_click(self, event): event.Skip()
        def c20230327202502_click(self, event): event.Skip()
        def c20230327202509_click(self, event): event.Skip()
        def c20230327202510_click(self, event): event.Skip()
        def c20230327202511_click(self, event): event.Skip()
        def c20230327202512_click(self, event): event.Skip()
        def c20230327202513_click(self, event): event.Skip()
        def c20230327202514_click(self, event): event.Skip()
        def c20230327202515_click(self, event): event.Skip()
        def c20230327202516_click(self, event): event.Skip()
        def c20230327202517_click(self, event): event.Skip()
        def c20230327202518_click(self, event): event.Skip()
        def c20230327202519_click(self, event): event.Skip()
        def c20230327202520_click(self, event): event.Skip()
        def c20230327202521_click(self, event): event.Skip()
        def c20230327202522_click(self, event): event.Skip()
        def c20230327202523_click(self, event): event.Skip()
        def c20230327202524_click(self, event): event.Skip()
        dingwei=800







#############################################   分界线   ################################################


class MianWindow(jar_management_gui):
    # 一、Tomcat漏洞测试工具
    def c20230327202501_click(self, event): subprocess.Popen('cmd /k "cd Tomcat && python CNVD-2020-10487.py -h"', shell=True)
    def c20230327202502_click(self, event): subprocess.Popen('cd Tomcat && CVE-2021-41773.exe', shell=True)
    # 二、 weblogic漏洞测试工具
    def c20230327202503_click(self, event): subprocess.Popen("cd Weblogic && " + java8_path + ' -jar ' + 'weblogic-framework.jar',shell=True)
    def c20230327202504_click(self, event): subprocess.Popen("cd Weblogic && " + java8_path + ' -jar ' + 'weblogic_exploit-1.0-SNAPSHOT-all.jar',shell=True)
    def c20230327202505_click(self, event): subprocess.Popen("cd Weblogic && " + java8_path + ' -jar ' + 'JAVA反序列化漏洞测试工具-WebLogic.jar',shell=True)
    def c20230327202506_click(self, event): subprocess.Popen("cd Weblogic && " + java8_path + ' -jar ' + 'Java反序列化漏洞测试工具V1.7.jar',shell=True)
    # 三、Jboss漏洞测试工具
    def c20230327202507_click(self, event): subprocess.Popen("cd Jboss && " + java8_path + ' -jar ' + 'Java反序列化终极测试工具.jar',shell=True)
    def c20230327202508_click(self, event): subprocess.Popen("cd Jboss && " + java8_path + ' -jar ' + 'ysoserial-master-30099844c6-1.jar',shell=True)
    # 四、Jenkins漏洞测试工具
    def c20230327202509_click(self, event): subprocess.Popen("cd Jenkins/CVE-2017-1000353 && " + java8_path + ' -jar ' + 'CVE-2017-1000353-1.1-SNAPSHOT-all.jar',shell=True)
    def c20230327202510_click(self, event): subprocess.Popen('cmd /k "cd Jenkins/CVE-2018-1000861 && python exp.py -h"', shell=True)
    # 五、shiro漏洞测试工具
    def c20230327202511_click(self, event): subprocess.Popen("cd Shiro/shiro_attack_2.2 && " + java8_path + ' -jar ' + 'shiro_attack-2.2.jar',shell=True)
    def c20230327202512_click(self, event): subprocess.Popen("cd Shiro && " + java8_path + ' -jar ' + 'ShiroExp.jar', shell=True)
    def c20230327202513_click(self, event): subprocess.Popen("cd Shiro && " + java8_path + ' -jar ' + 'ShiroExploit-v2.3.jar', shell=True)
    def c20230327202514_cilck(self, event): subprocess.Popen("cd Shiro && " + java8_path + ' -jar ' + 'ShiroExploit.jar', shell=True)
    def c20230327202515_click(self, event): subprocess.Popen("cd Shiro && " + java8_path + ' -jar ' + 'ShiroScan-1.1.jar', shell=True)
    def c20230327202516_click(self, event): subprocess.Popen("cd Shiro/ShiroExploit.V2.51 && " + java8_path + ' -jar ' + 'ShiroExploit.jar',shell=True)
    def c20230327202517_click(self, event): subprocess.Popen("cd Shiro && " + java8_path + ' -jar ' + 'Shiro-550-with-NoCC.jar',shell=True)
    def c20230327202518_click(self, event): subprocess.Popen("cd Shiro/shiro_attack2 && " + java8_path + ' -jar ' + 'shiro_attack-4.5.2-SNAPSHOT-all.jar',shell=True)
    # 六、struts2漏洞工具
    def c20230327202519_click(self, event): subprocess.Popen('cd Struts2 && K8_Struts2_EXP.exe', shell=True)
    def c20230327202522_click(self, event): subprocess.Popen('cd Struts2 && Struts2漏洞检查工具2019版_V2.3.exe', shell=True)
    def c20230327202521_click(self, event): subprocess.Popen("cd Struts2 && " + java8_path + ' -jar ' + 'Struts2_Chek_BypassWAF[17-6].jar', shell=True)
    def c20230327202520_click(self, event): subprocess.Popen("cd Struts2 && " + java8_path + ' -jar ' + 'Struts_2_全版本漏洞检测工具_18.09_过waf版.jar',shell=True)
    dingwei=900







    # 七、增加程序
    def c20230327202523_click(self, event):
        subprocess.Popen('python add.py', shell=True)
        # 获取当前程序的进程ID
        pid = os.getpid()
        # 关闭当前程序
        os.system(f"taskkill /F /PID {pid}")
    def c20230327202524_click(self, event):
        subprocess.Popen('python sub.py', shell=True)
        # 获取当前程序的进程ID
        pid = os.getpid()
        # 关闭当前程序
        os.system(f"taskkill /F /PID {pid}")




if __name__ == '__main__':
    app = wx.App()
    frame = MianWindow(None)
    frame.Show()
    # 获取屏幕的尺寸
    screen_width, screen_height = wx.DisplaySize()

    # 获取窗口的尺寸
    frame_width, frame_height = frame.GetSize()

    # 计算窗口的位置
    frame_x = (screen_width - frame_width) // 2
    frame_y = (screen_height - frame_height) // 2

    # 设置窗口的位置
    frame.SetPosition((frame_x, frame_y))

    app.MainLoop()