# 基于python 3 + requests + pytest实现的自动化框架


整体框架思路如下：

在company项目下有 configure、Log、Model、Result、testcase、other（请忽略，只是测试model模块功能的脚本）

1、configure目录主要存放配置文件，如.ini存放临时文件，.yml存放大批返回值的数据（复杂json数据），excel文件用来处理用例

2、Log文件用于存放运行过程的日志（封装了logging模版的方法）

3、Model 模块，主要是把每个用例共有方法封装，如访问redis，mongoDB，requests库封装等

4、testcase就是放入测试用例，通过调用Model模版的共有方法进行请求，并用assert确定返回值的正确性

5、Result主要存放执行结果，使用了requets-html库，很好的在网页中查看到结果

最后使用run.py脚本来执行需要执行的用例

PS：由于开发脚本时间较短，后续还需优化的：
1、还有部分冗余的代码，进行提炼

2、还未进行到对比数据库，当前只判断了status为200的情况，应该是返回值与数据库进行assert

3、需要考虑通过配置文件后，能否自动生成部分常用代码（高阶操作），这样才是框架的最高境界，就是代码是根据配置的部分参数自动生成，只需要添加一个http请求后台自己生成对应默认请求代码

所以姑且当此框架为一个可运行的Demo，希望对大家有用
