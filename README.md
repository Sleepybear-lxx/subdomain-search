# subdomain-search
基于插件的子域名查询工具，支持插件扩展，自定义参数。目前完成了利用第三方网站和DNS A记录进行查询(以ichunqiu.com为例)。
# 文件说明
## config.py
config.py中包含了工具的基本参数配置，目前包含如下参数：
1. requests请求头
2. 目标网站域名
3. 子域名字典目录
4. 线程数
5. 其他参数
## common.py
common.py中包含了工具实现的通用功能支撑，方便后续插件扩展，目前包含如下功能：
1. 基于get方式的http请求，返回目标网站响应内容
2. 文件保存，将子域名结果保存到json文件
## utils
utils文件夹中包含了具体功能实现，可编写其他插件丰富工具实现，目前包含如下功能：
1. 基于第三方网站的子域名查询(diandian)
2. 基于DNS A记录的子域名查询
3. subdomain为子域名字典(submain含有5000条记录，submain1含有13条记录，submain2含有1000条记录)
## domain.py
domian.py为本工具主体，运行完成后，在result目录下生成域名对应文件夹，以json格式存储子域名查询结果
# 更新日志
* v1.0 20220329 基本功能完成
