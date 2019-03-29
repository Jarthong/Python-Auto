
from selenium import webdriver
dr = webdriver.Chrome()
dr.get('http://www.baidu.com')
# dr.find_element_by_xpath('//input[@id="kw"]').send_keys('jarthong')

# 爷爷标签定位
# dr.find_element_by_xpath('//form[@id="form"]/span/input').send_keys('jarthong')

# # 逻辑运算符（加强元素唯一性）
# dr.find_element_by_xpath('//input[@id="kw" and @autocomplete="off"]').send_keys('jarthong')
# dr.find_element_by_xpath('//input[@value="百度一下"]').click()
# # dr.quit()

# css
# dr.find_element_by_css_selector('form#form>span>input.s_ipt').send_keys('jarthong')

# is_displayer() 查看元素是否可见
# m = dr.find_element_by_id('kw').is_displayed()
# print(m)


# 显示等待
from selenium import webdriver
# 显示等待需要导入下面三个方法（类），
from selenium.webdriver.support import expected_conditions as EC   # 判断元素是否出现的类
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待需要结合WebDriverWait这个类使用
from selenium.webdriver.common.by import By  # 元素定位的另外一种写法

dr = webdriver.Chrome()
dr.get('http://www.baidu.com')
# WebDriverWait这个类需要传三个参数，第一个参数是浏览器驱动，第二个参数是整个判断的总时长，第三个是代表多久判断一次（单位是秒）
WebDriverWait(dr,5,0.5).until(EC.presence_of_element_located((By.ID,"kw"))).send_keys('jathong')



# By类使用方法
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   # 键盘事件
from time import sleep
dr = webdriver.Chrome()
dr.get('http://www.baidu.com')
dr.maximize_window()  # 窗口最大化
dr.find_element(By.ID,'kw').send_keys('jarthong')  # 定位到百度输入框，输入内容
dr.find_element(By.CSS_SELECTOR,'[value="百度一下"]').click()  # 点击“百度一下”

sleep(3)
dr.find_element(By.ID,'kw').send_keys(Keys.BACK_SPACE)
sleep(3)
dr.find_element(By.ID,'kw').send_keys('hong')
sleep(3)
dr.find_element(By.CSS_SELECTOR,'[value="百度一下"]').send_keys(Keys.ENTER)

sleep(3)
# 调用javascript方法来执行滚动条
# 以下这条命令，除了把纵向滚动条从上往下拉之外，也同时会把横向滚动条从右往左拉，若横向本身就在左边，则不动
dr.execute_script('window.scrollTo(0,2500)')  # 纵向拉动滚动条，从上往下拉
sleep(3)
# dr.execute_script('window.scrollTo(2500,0)')  # 从下往上拉
# 定位一组元素，通过数组下标来确定第几个元素
dr.find_elements(By.CLASS_NAME,'pc')[1].click()
sleep(3)
# 设置窗口大小,为了调出横向滚动条
dr.set_window_size(600,480)
sleep(3)
dr.execute_script('window.scrollTo(0,800)')
sleep(3)
# 这条命令，除了把横向滚动条从左往右拉之外，也同时会把纵向滚动条从下往上拉
dr.execute_script('window.scrollTo(2500,0)')



# 鼠标悬停
from selenium import webdriver
# 导入ActionChains鼠标悬停模块
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
dr = webdriver.Chrome()
dr.get('http://www.baidu.com')
sleep(2)
# 先获取要悬停的元素
# 注意：百度登录账号状态和未登录账号，元素属性不一样
name = dr.find_element_by_link_text('设置')
# ActionChains需要传入驱动参数...移动到要悬停的元素...执行操作
ActionChains(dr).move_to_element(name).perform()
sleep(3)
dr.find_element_by_link_text('高级搜索').click()



from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get('https://www.baidu.com/')
dr.find_element_by_id('kw').send_keys('渗透吧')
dr.find_element_by_id('su').click()
sleep(3)
dr.find_element_by_xpath('//*[@id="1"]/h3/a').click()  # 点击搜索出来的第一个贴吧
print(dr.window_handles)  # 打印看一下句柄，（实际操作时省去），以数组的形式存在
sleep(3)
# 切换到第二个窗口（即新打开的窗口），第二个页面的句柄dr.window_handles[1]
dr.switch_to.window(dr.window_handles[1])
# 点击第一个帖子
dr.find_element_by_xpath('//*[@id="thread_top_list"]/li[1]/div/div[2]/div/div[1]/a').click()
sleep(3)
# 切换到第三个窗口，（即帖子打开的窗口）
dr.switch_to.window(dr.window_handles[2])
# 返回第一个窗口
dr.switch_to.window(dr.window_handles[0])
dr.find_element_by_id('kw').clear()  # 清空输入框
sleep(2)
dr.find_element_by_id('kw').send_keys('jarthong')
sleep(2)
dr.find_element_by_id('su').click()  # 点击‘百度一下’



















