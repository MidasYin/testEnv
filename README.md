# 基于python 3 + requests + pytest实现的自动化框架


整体框架思路如下：

在company项目下有 configure、Log、Model、Result、testcase、other（请忽略，只是测试model模块功能的脚本）
1、configure目录主要存放配置文件，如.ini存放临时文件，.yml存放大批返回值的数据（复杂json数据），excel文件用来处理用例
2、Log文件用于存放运行过程的日志（封装了logging模版的方法）
3、Model 模块，主要是把每个用例共有方法封装，如访问redis，mongoDB，requests库封装等
4、testcase就是放入测试用例，通过调用Model模版的共有方法进行请求，并用assert确定返回值的正确性
5、Result主要存放执行结果，使用了requets-html库，很好的在网页中查看到结果

最后使用run.py脚本来执行需要执行的用例

