# 一、如何安装和启动
- 安装：
pip install flask
- 启动：
python app.py

# 二、代码介绍
app.py文件是项目启动的文件，所有路由都定义在这里
config目录：本项目配置文件目录
model目录：定义了每个路由api的业务逻辑
tool目录：被model目录调用的一些方法
mock目录：放了一点模拟的数据，用来开发调试

