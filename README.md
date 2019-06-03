HN-Tools平台运营部工具集
==

## 信用数据查询工具使用说明及注意事项

* 本工具使用Selenium的Chromedriver驱动实现登录【国家交通运输物流公共信息平台】的功能，所以务必确保机器上已安装了Chrome浏览器。
* Chrome应使用74.0.3729.6，否则可能会无法正常运行。
* 为了将所有代码打包进单独EXE文件的关系，启动速度会略慢（视机器性能而定），此为正常现象，不是BUG！
* 工具停止使用后，请点击右上角【X】键正常退出，因为此时会执行一个清除Chrome内存占用的行为，会产生短暂卡顿，这也不是BUG！
--
## 信用数据查询更新记录

### V1.2
* 修正某些字段名使其更符合实际情况。
* 添加图标。

### V1.1
* 修改车辆载重字段。
* 增加所有人字段。
* 增加车牌号字段。
* 添加窗口置前功能。
* 输入框添加简单的空格字符剔除功能。从能运平台复制的司机名或车牌号里带有空格的话，无需手动删除即可正确识别。
--

## 验证码提取工具使用说明及注意事项
没什么好说的...已经根据目前采用的新验证码接口进行了修正，功能正常，并且删除了查询信息里过多的冗余字符，精简表达。这个工具在目前短信验证已经正常的情况下使用率应该不高。
