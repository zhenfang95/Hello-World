#!/usr/bin/env python
'''
一、pytest简介:
pytest是python的一种单元测试框架，与python自带的unittest测试框架类似，但是比unittest框架使用起来更简洁，效率更高。根据pytest的官方网站介绍，它具有如下特点：
1、非常容易上手，入门简单，文档丰富，文档中有很多实例可以参考
2、能够支持简单的单元测试和复杂的功能测试
3、 支持参数化
4、 执行测试过程中可以将某些测试跳过（skip），或者对某些预期失败的case标记成失败
5、支持重复执行(rerun)失败的case
6、 支持运行由nose, unittest编写的测试case
7、 可生成html报告
8、 方便的和持续集成工具jenkins集成
9、 可支持执行部分用例
10、 具有很多第三方插件，并且可以自定义扩展

二、运行：
1、.打开test_*.py所在的文件夹，cmd窗口输入：pytest（或者输入py.test也可以）
2、pytest运行规则：查找当前目录及其子目录下以test_*.py或*_test.py文件，找到文件后，在文件中找到以test开头函数并执行
3、pytest----运行文件夹下所有test_*.py模块
4、py.test -q test_class.py-----指定模块运行

三、pytest用例规则：
1、测试文件夹以test_开头（以_test结尾也可以）
2、测试类以Test开头，并且不能带有init方法
3、测试函数以test_开头
4、断言使用assert

四、执行用例规则
1、执行某个目录下所有的用例
pytest 文件名/

2、执行某一个py文件下用例
pytest 脚本名称.py

3、-k按关键词匹配
pytest -k "MyClass and not method"

4、按节点运行
运行.py模块里面的某个函数
pytest test_mod.py(模块)::test_func(函数)
运行.py模块里面,测试类里面的某个方法
pytest test_mod.py::TestClass::test_method

5、标记表达式
pytest -m slow
将运行用@ pytest.mark.slow装饰器修饰的所有测试

6、从包里面运行
pytest --pyargs pkg.testing
这将导入pkg.testing并使用其文件系统位置来查找和运行测试

7、-x 遇到错误时停止测试
pytest -x test_class.py

8、--maxfail=num
pytest --maxfail=1
当用例错误个数达到指定数量时，停止测试

五、pycharm运行三种方式
在cmd运行，打印运行方法下面的print要在后面加“-s”
1、以xx.py脚本方式直接执行，当写的代码里面没用到unittest和pytest框架时，并且脚本名称不是以test_开头命名的，此时pycharm会以xx.py脚本方式运行
2.当脚本命名为test_xx.py时，用到unittest框架，此时运行代码，pycharm会自动识别到以unittest方式运行
3.以pytest方式运行，需要改该工程设置默认的运行器：file->Setting->Tools->Python Integrated Tools->项目名称->Default test runner->选择py.test
pytest是可以兼容unittest脚本的，之前写的unittest用例也能用pytest框架去运行

'''

"""
（test_fixt.py）
用例运行级别

    模块级（setup_module/teardown_module）开始于模块始末，全局的

    函数级（setup_function/teardown_function）只对函数用例生效（不在类中）

    类级（setup_class/teardown_class）只在类中前后运行一次(在类中)

    方法级（setup_method/teardown_method）开始于方法始末（在类中）

    类里面的（setup/teardown）运行在调用方法的前后
"""

'''
fixture之conftest.py:
1、firture相对于setup和teardown来说应该有以下几点优势:
    命名方式灵活，不局限于setup和teardown这几个命名
    conftest.py 配置里可以实现数据共享，不需要import就能自动找到一些配置
    scope="module" 可以实现多个.py跨文件共享前置, 每一个.py文件调用一次
    scope="session" 以实现多个.py跨文件使用一个session来完成多个用例

2、conftest.py配置
conftest.py配置需要注意以下点：
    conftest.py配置脚本名称是固定的，不能改名称
    conftest.py与运行的用例要在同一个pakage下，并且有__init__.py文件
    不需要import导入 conftest.py，pytest用例会自动查找

fixture之yield实现teardown：
1、fixture参数scope="module"，module作用是整个.py文件都会生效，用例调用时，参数写上函数名称就行
2、既然有setup那就有teardown,fixture里面的teardown用yield来唤醒teardown的执行

'''
'''
pytest-html生成测试报告
安装：pip install pytest-html
1、执行方法
打开cmd，cd到需要执行pytest用例的目录，执行指令：pytest --html=report.html
执行完之后，在当前目录会生成一个report.html的报告文件
2、指定报告路径
pytest --html=./report/report.html

3、生成独立报告
pytest --html=report.html --self-contained-html

失败重跑
失败重跑需要依赖pytest-rerunfailures插件
安装：pip install pytest-rerunfailures
1、用例失败再重跑1次,命令行加个参数--reruns就行了
 py.test --reruns 1 --html=report.html
'''
"""
参数化parametrize
1、pytest.mark.parametrize装饰器可以实现测试用例参数化
2、参数组合：若要获得多个参数化参数的所有组合，可以堆叠参数化装饰器

"""
'''
命令行传参
1、首先需要在conftest.py添加命令行选项,命令行传入参数”--cmdopt“, 用例如果需要用到从命令行传入的参数，就调用cmdopt函数
2、cmd打开，输入指令启动，也可以在pycharm里面右键执行上面代码
带参数启动
1、如果不带参数执行，那么传默认的default="type1"，接下来在命令行带上参数去执行
pytest -s test_sample.py --cmdopt=type2
2、命令行传参数有两种写法，还有一种分成2个参数也可以的,参数和名称用空格隔开
pytest -s test_case1.py --cmdopt type2
'''