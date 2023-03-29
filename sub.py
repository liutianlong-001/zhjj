import wx
import os

# 创建应用程序对象
app = wx.App()

# 创建窗口
frame = wx.Frame(None, title="删除程序", size=(300, 200),style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
# 创建窗口颜色
frame.SetBackgroundColour(wx.WHITE)
# 创建sizer
sizer = wx.BoxSizer(wx.VERTICAL)
sizer.AddSpacer(10)
# 创建垂直的sizer
text_box_sizer = wx.BoxSizer(wx.VERTICAL)
text_box_sizer.Add(wx.StaticText(frame, label="请输入需要删除的工具名称"), 0, wx.ALL | wx.EXPAND, 5)
text_box = wx.TextCtrl(frame, size=(200, -1))
text_box_sizer.Add(text_box, 0, wx.CENTER | wx.ALIGN_CENTER | wx.ALL, 5)
sizer.Add(text_box_sizer, 0, wx.CENTER | wx.ALIGN_CENTER | wx.ALL, 5)  # 将垂直sizer添加到主sizer中
sizer.AddSpacer(10)
# 创建确认按钮
confirm_button = wx.Button(frame, label="确认")
sizer.Add(confirm_button, 0, wx.CENTER | wx.TOP | wx.ALIGN_CENTER, 5)

# 定义全局变量
global shanchu

def on_confirm_button_click(event):
    # 将文本框中的内容赋值给全局变量shanchu
    global shanchu
    shanchu = text_box.GetValue()

    # 打开 main.py 文件并查找包含变量 shanchu 的行
    with open('main.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 定义一个空字符串用于保存匹配到的代码
    daima = ""

    for line in lines:
        if shanchu in line:
            daima += line  # 将匹配到的代码添加到 daima 中

    # 获取 daima 的第 5-20 个字符（不包含空格）
    result = daima[13:28].replace(" ", "")
    print(f"要查找的代码片段为：{result}")

    # 打开 main.py 文件并查找包含 result 的行
    with open('main.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(lines)

    # 保存删除后的代码
    new_lines = []

    for line in lines:
        if result in line:
            print(f"匹配到的代码为：{line.strip()}")
        else:
            new_lines.append(line)

    # 将删除后的代码保存回文件
    with open('main.py', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print("删除成功！")

    # 关闭当前窗口并打开 main.py 程序
    frame.Destroy()
    os.system("python main.py")


confirm_button.Bind(wx.EVT_BUTTON, on_confirm_button_click)

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
