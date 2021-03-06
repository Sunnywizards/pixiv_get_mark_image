# pixiv_get_mark_image

This is an automation tool to get your favorite artworks on your pixiv mark page and this tool is based on Python 3.7 and Selenium.  

It is easy to use this tool, and the following is the guide for it.  

1. Before running it, make sure that the chrome driver in this tool can support your chrome. The current version of this chrome driver is 89 and you can replace it by the driver which is compatiable with your Chrome ([Driver Download Link](http://chromedriver.storage.googleapis.com/index.html)).  

2. Create a folder named "pixiv_img"  

3. Run the main.py `python main.py` and input your pixiv account and password to login it. And then the Selenium will do the image saving operation automatically in your pixiv mark page.  

这是一个可以存储你在pixiv收藏的绘画作品的小工具，其基于Python 3.7和Selenium实现。  

以下是使用指南：  

1. 第一次运行本工具前，需要确保在项目里的chrome driver的版本和当前系统所使用的chrome driver一致（当前仓库中放置的chromedriver版本为89）。如果不一致，则需要去[Google API](http://chromedriver.storage.googleapis.com/index.html)选择和当前chrome版本一致的driver，并替换原先的driver  
2. 在本项目根目录新建"pixiv_img"文件夹
3. 运行main.py文件`python main.py`并输入你的pixiv账号和密码以登录，之后Selenium会自动地存储你在pixiv收藏夹里的图片