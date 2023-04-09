# News Player v1.0 by Wang Zhiyu
# 2023/04/05
# 这个程序依赖于 ChromeDriver.exe nircmd.exe, 放于该目录下即可
# 假如你是下一届的学生而且打开了这个文件, 不要以为这是病毒, 这玩意是2020届的学生写的用来晚上7点钟自动打开CCTV13播放的答辩代码, 如果你们不需要看新闻联播了, 删除此文件即可, 系统不会寄掉。
# 附带: 我知道这个文件的hash值, 并做了线上备份, 如果有人动了这个文件我是知道的哦~
# 另: 如果你想改改代码和功能, 可以看看答辩注释
# 如果改烂了可以访问 https://pastebin.ubuntu.com/p/CdhgQqf7j9/ 源代码

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyttsx3
from selenium.webdriver.common.action_chains import ActionChains
import getpass
welcome_char_image = """
ANP v1.2
LOG:
"""
bye_char_image = """
ANP v1.2
"""
print(welcome_char_image)
# 设置Chromium浏览器路径(答辩代码)
a = r"C:\Users\\"
b = r"\AppData\Local\Chromium\Application\chrome.exe"
chrome_path = a + getpass.getuser() + b


engine = pyttsx3.init()
os.system("nircmd.exe setsysvolume 40000")
# 启动Chromium浏览器并打开CCTV13网站
options = webdriver.ChromeOptions()
# 设置启动参数，模拟人类用户的行为(关闭沙比浏览器受控制横幅)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.binary_location = chrome_path
driver = webdriver.Chrome(options=options)
driver.get("http://tv.cctv.com/live/cctv13/")
time.sleep(5)  # 等待页面加载完成
# 自动点击播放按钮
play_button = driver.find_element(By.XPATH,'//*[@id="play_or_pause_play_player"]')
play_button.click()
time.sleep(3)

# 切换到全屏模式
fullscreen_button = driver.find_element(By.XPATH,'//*[@id="player_fullscreen_no_player"]')
fullscreen_button.click()

time.sleep(3)  # 等待切换完成
# 调整电脑音量为15%
# 注: 100% 为 65535
os.system("nircmd.exe setsysvolume 9830")
# 实例化ActionChains类，并传入驱动程序对象
actions = ActionChains(driver)

# 将指针移动到其他位置 (随便找了个元素)
actions.move_to_element(driver.find_element(By.XPATH,'//*[@id="search"]/div/div[1]/div/span[3]/input[1]')).perform()
# 播放30分钟后关闭浏览器
# time.sleep(5)
time.sleep(1760)
driver.quit()
# 调整电脑音量为75%
os.system("nircmd.exe setsysvolume 49151")
os.system("cls")
print(bye_char_image)

os.system("explorer.exe")