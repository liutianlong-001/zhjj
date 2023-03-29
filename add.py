import wx
import datetime
import shutil
import os

# 创建应用程序对象
app = wx.App()

# 创建窗口
frame = wx.Frame(None, title="新增程序",size=(490, 450), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

# 创建窗口颜色
frame.SetBackgroundColour(wx.WHITE)

# 创建sizer
sizer = wx.BoxSizer(wx.VERTICAL)
sizer.AddSpacer(10)
# 创建文本框（用于输入标题）
text_ctrl = wx.TextCtrl(frame)
sizer.Add(wx.StaticText(frame, label="请输入工具名称"), 0, wx.ALL | wx.EXPAND, 5)
sizer.Add(text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
sizer.AddSpacer(10)
# 创建单选按钮1（用于选择中间件）
radio_box1 = wx.RadioBox(frame, label="请选择中间件", choices=["Tomcat", "Weblogic",'Jboss','Jenkins','Shiro','Struts2'])
sizer.Add(radio_box1, 0, wx.ALL | wx.EXPAND, 5)

sizer.AddSpacer(10)

# 创建单选按钮2（用于选择语言）
radio_box2 = wx.RadioBox(frame, label="请选择所用语言", choices=["python", "java"])
sizer.Add(radio_box2, 0, wx.ALL | wx.EXPAND, 5)
sizer.AddSpacer(10)
# 创建文件选择对话框（用于选择文件）
def on_choose_file(event):
    dlg = wx.FileDialog(frame, "新增程序")
    if dlg.ShowModal() == wx.ID_OK:
        file_path = dlg.GetPath()

        # 设置全局变量
        global wenjian
        wenjian = file_path
        # 显示选择的文件地址
        file_path_text.SetLabel(file_path)
    dlg.Destroy()



choose_file_btn = wx.Button(frame, label="选择文件")
choose_file_btn.SetSize((10, -1))
choose_file_btn.Bind(wx.EVT_BUTTON, on_choose_file)
sizer.Add(wx.StaticText(frame, label="请选择工具文件",pos=(10, 10)), 0, wx.ALL | wx.EXPAND, 5)
sizer.Add(choose_file_btn, 0, wx.ALL | wx.EXPAND, 5)


# 创建静态文本控件（用于显示选择的文件地址）
file_path_text = wx.TextCtrl(frame, pos=(10, 70), size=(270, -1))
sizer.Add(file_path_text, 0, wx.ALL | wx.EXPAND, 5)


# 创建确认按钮（用于设置全局变量并在1.py中打印）
def on_confirm(event):
    # 设置全局变量
    global biaoti, loudong, yuyan
    biaoti = text_ctrl.GetValue()
    loudong = radio_box1.GetStringSelection()
    yuyan = radio_box2.GetStringSelection()

    # 获取当前时间并将其格式化为纯数字形式
    now = datetime.datetime.now()
    shijian = now.strftime("%Y%m%d%H%M%S")


    #####################################################
    ###########在这里添加代码###############################
    #####################################################

    # 获取当前工作目录的绝对路径
    current_dir = os.getcwd()

    # 拼接得到 loudong 目录的绝对路径
    loudong_dir = os.path.join(current_dir, loudong)

    # 拼接得到目标地址的绝对路径
    dest_dir = os.path.join(loudong_dir, os.path.basename(wenjian))

    # 复制文件
    shutil.copy(wenjian, dest_dir)

    # 将相对地址赋值给 dizhi
    dizhi = os.path.relpath(dest_dir, current_dir)

    # 获取目标文件的文件名并赋值给 dizhi2
    dizhi2 = os.path.basename(dest_dir)

    ## 这里是第一处修改
    if loudong == "Tomcat":
        with open("main.py", "r",encoding="utf-8") as file:
            lines = file.readlines()
        index = 0
        for i in range(len(lines)):
            if "dingwei=100" in lines[i]:
                index = i + 1
                break
        lines.insert(index,
                     f"        self.c{shijian} = wx.Button(gui_{loudong}.GetStaticBox(), wx.ID_ANY, u\"{biaoti}\", wx.DefaultPosition, size = (220, 23))\n        {loudong}.Add(self.c{shijian}, 0, wx.ALL, 4)\n\n")
        with open("main.py", "w",encoding="utf-8") as file:
            file.writelines(lines)

    elif loudong == 'Weblogic':
        with open("main.py", "r",encoding="utf-8") as file:
            lines = file.readlines()
        index = 0
        for i in range(len(lines)):
            if "dingwei=200" in lines[i]:
                index = i + 1
                break
        lines.insert(index,
                     f"        self.c{shijian} = wx.Button(gui_{loudong}.GetStaticBox(), wx.ID_ANY, u\"{biaoti}\", wx.DefaultPosition, size = (220, 23))\n        {loudong}.Add(self.c{shijian}, 0, wx.ALL, 4)\n\n")
        with open("main.py", "w",encoding="utf-8") as file:
            file.writelines(lines)

    elif loudong == 'Jboss':
        with open("main.py", "r",encoding="utf-8") as file:
            lines = file.readlines()
        index = 0
        for i in range(len(lines)):
            if "dingwei=300" in lines[i]:
                index = i + 1
                break
        lines.insert(index,
                     f"        self.c{shijian} = wx.Button(gui_{loudong}.GetStaticBox(), wx.ID_ANY, u\"{biaoti}\", wx.DefaultPosition, size = (220, 23))\n        {loudong}.Add(self.c{shijian}, 0, wx.ALL, 4)\n\n")
        with open("main.py", "w",encoding="utf-8") as file:
            file.writelines(lines)

    elif loudong == 'Jenkins':
        with open("main.py", "r",encoding="utf-8") as file:
            lines = file.readlines()
        index = 0
        for i in range(len(lines)):
            if "dingwei=400" in lines[i]:
                index = i + 1
                break
        lines.insert(index,
                     f"        self.c{shijian} = wx.Button(gui_{loudong}.GetStaticBox(), wx.ID_ANY, u\"{biaoti}\", wx.DefaultPosition, size = (220, 23))\n        {loudong}.Add(self.c{shijian}, 0, wx.ALL, 4)\n\n")
        with open("main.py", "w",encoding="utf-8") as file:
            file.writelines(lines)

    elif loudong == 'Shiro':
        with open("main.py", "r",encoding="utf-8") as file:
            lines = file.readlines()
        index = 0
        for i in range(len(lines)):
            if "dingwei=500" in lines[i]:
                index = i + 1
                break
        lines.insert(index,
                     f"        self.c{shijian} = wx.Button(gui_{loudong}.GetStaticBox(), wx.ID_ANY, u\"{biaoti}\", wx.DefaultPosition, size = (220, 23))\n        {loudong}.Add(self.c{shijian}, 0, wx.ALL, 4)\n\n")
        with open("main.py", "w",encoding="utf-8") as file:
            file.writelines(lines)

    elif loudong == 'Struts2':
        with open("main.py", "r",encoding="utf-8") as file:
            lines = file.readlines()
        index = 0
        for i in range(len(lines)):
            if "dingwei=600" in lines[i]:
                index = i + 1
                break
        lines.insert(index,
                     f"        self.c{shijian} = wx.Button(gui_{loudong}.GetStaticBox(), wx.ID_ANY, u\"{biaoti}\", wx.DefaultPosition, size = (220, 23))\n        {loudong}.Add(self.c{shijian}, 0, wx.ALL, 4)\n\n")
        with open("main.py", "w",encoding="utf-8") as file:
            file.writelines(lines)

    ## 这里是第二处修改
    with open("main.py", "r", encoding="utf-8") as file:
        lines = file.readlines()
    index = 0
    for i in range(len(lines)):
        if "dingwei=700" in lines[i]:
            index = i + 1
            break
    lines.insert(index,
                 f"        self.c{shijian}.Bind(wx.EVT_BUTTON, self.c{shijian}_click)\n\n")
    with open("main.py", "w", encoding="utf-8") as file:
        file.writelines(lines)

    ## 这里是第三处修改
    with open("main.py", "r", encoding="utf-8") as file:
        lines = file.readlines()
    index = 0
    for i in range(len(lines)):
        if "dingwei=800" in lines[i]:
            index = i + 1
            break
    lines.insert(index,
                 f"        def c{shijian}_click(self, event): event.Skip()\n\n")
    with open("main.py", "w", encoding="utf-8") as file:
        file.writelines(lines)


    ## 这里是第四处修改
    if yuyan == "java":
        with open("main.py", "r", encoding="utf-8") as file:
            lines = file.readlines()
        index = 0
        for i in range(len(lines)):
            if "dingwei=900" in lines[i]:
                index = i + 1
                break
        lines.insert(index,
                     f"    def c{shijian}_click(self, event): subprocess.Popen(\"cd {loudong} && \" + java8_path + \' -jar \' + \'{dizhi2}\',shell=True)\n\n")
        with open("main.py", "w", encoding="utf-8") as file:
            file.writelines(lines)

    elif yuyan == "python":
        with open("main.py", "r", encoding="utf-8") as file:
            lines = file.readlines()
        index = 0
        for i in range(len(lines)):
            if "dingwei=900" in lines[i]:
                index = i + 1
                break
        lines.insert(index,
                     f"    def c{shijian}_click(self, event): subprocess.Popen(\'cmd /k \"cd {loudong} && python {dizhi2} -h\"\', shell=True)\n\n")
        with open("main.py", "w", encoding="utf-8") as file:
            file.writelines(lines)



    frame.Close()
    os.system("python main.py")
    #####################################################
    ###########在这里添加代码###############################
    #####################################################


confirm_btn = wx.Button(frame, label="确认")
confirm_btn.Bind(wx.EVT_BUTTON, on_confirm)
sizer.Add(confirm_btn, 0, wx.ALL | wx.EXPAND, 5)

# 设置窗口sizer
frame.SetSizer(sizer)

# 显示窗口
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

# 运行应用程序
app.MainLoop()
