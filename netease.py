import sys
import webbrowser
sys.path.append("libs")
print("网易云真实外链自动获取工具\n\nMade By Vincent\n\n")
print("请输入网易云链接：\n")
url = input()
id = str(url.split("=")[1])
url_front="http://music.163.com/song/media/outer/url?id="
url_real=url_front+id+".mp3"
print("\n真实的链接为：\n\n"+url_real+"\n")
while(True):
    print("是否直接访问。按Y/N\n")
    in_content = input("请输入：")
    if in_content == "Y":
        print("已打开！")
        webbrowser.open(url_real)
        exit(0)
    elif in_content == "N":
        print("你已退出了该程序！")
        exit(0)
    else:
        print("你输入的内容有误，请重输入！")
