# UNIX标准及其实现

---
标准化主要是为了方便程序在不同版本之间移植，了解这一部分可以帮助我们写出可移植的C程序，对交叉编译也能有更深一步的认识。这里简要介绍三个标准，ISO C，POSIX，Single UNIX Specification。

#### ISO C
ISO C 标准的意图是提供C程序的可移植性，使其能适合大量的操作系统，而不仅仅是UNIX，此标准不仅定义了C语言的语法和语义，还定义了C标准库，现在所有的UNIX系统都提供C标准中定义的库函数，所以该标准库非常重要，按照这个标准定义的头文件可将ISO C库分为24个区，下边要介绍的POIX.1标准包含了这些头文件以及另外一些头文件，因此可以说POIX.1兼容ISO C。需要注意的是ISO C头文件依赖于操作系统所配置的版本。下面是这24四个头文件的列表：   

|头文件 |说明 |
|----- |-----|
| &lt;assert.h> | 验证程序断言 |
| &lt;complex.h> | 复数算术运算支持 |
| &lt;ctype.h> | 字符分类和映射支持 |
| &lt;error.h> | 出错码 |
| &lt;fenv.h> | 浮点环境 |
| &lt;float.h> | 浮点常量及特性 |
| &lt;inttypes.h> | 整型格式变换 |
| &lt;iso646.h> | 赋值，关系及一元操作宏符 |
| &lt;limits.h> | 实现常量 |
| &lt;locale.h> | 本地化类别及相关定义 |
| &lt;math.h> | 数学函数，类型声明及常量 |
| &lt;setjump.h> | 非局部goto |
| &lt;signal.h> | 信号 |
| &lt;stdarg.h> | 可变长度参数表 |
| &lt;stdbool.h> | 布尔类型和值 |
| &lt;stddef.h> | 标准定义 |
| &lt;stdinit.h> | 整型 |
| &lt;stdio.h> | 标准IO库 |
| &lt;stdlib.h> | 实用函数 |
| &lt;string.h> | 字符串操作 |
| &lt;tgmath.h> | 通用类型数学宏 |
| &lt;time.h> | 时间和日期 |
| &lt;wchar.h> | 扩充的多字节和宽字符支持 |
| &lt; wctype.h> | 宽字符分类和映射支持 |

#### POSIX

POSIX指的是可移植操作系统接口，他有多个标准，本书采用的是1003.1(POSIX.1)，这个标准的目的就是提升应用程序在各种UNIX环境之间的可移植性，它定义了符合POSIX的操作系统必须提供的各种服务，除了UNIX和类UNIX系统，还有其他一些操作系统也兼容POSIX标准。下面是POSIX的必选头文件，可选头文件后续补充。此外POSIX还定义了很多涉及操作系统的限制常量，这在实际使用中需要注意的。

#####必选头文件
|头文件 |说明 |
|----- |-----|
| &lt;aio.h> | 异步IO |
| &lt;cpio.h> | cpio归档值 | 
| &lt;dirent.h> | 目录项 |
| &lt;dlfcn.h> | 动态链接 |
| &lt;fcntl.h> | 文件控制 |
| &lt;fnmatch.h> | 文件名匹配类型 |
| &lt;glob.h> | 路径名模式匹配与生成 |
| &lt;grp.h> | 组文件 |
| &lt;iconv.h> | 代码集变换实用程序 |
| &lt;langinfo.h> | 语言信息常量 |
| &lt;monetary.h> | 货币类型与函数 |
| &lt;netdb.h> | 网络数据库操作 |
| &lt;nl_type.h> | 消息类 |
| &lt;poll.h> | 投票函数 |
| &lt;pthread.h> | 线程 |
| &lt;pwd.h> | 口令文件 |
| &lt;regex.h> | 正则表达式 |
| &lt;sched.h> | 执行调度 |
| &lt;semaphore.h> | 信号量 |
| &lt;string.h> | 字符串操作 |
| &lt;tar.h> | tar归档值 |
| &lt;termios.h> | 终端IO |
| &lt;unistd.h> | 符号常量 |
| &lt;wordexp.h> | 字扩充类型 |
| &lt;arpa/inet.h> | 英特网定义 |
| &lt;net/if.h> | 套接字本地接口 |
| &lt;netinet/in.h> | 英特网地址族 |
| &lt;netinet/tcp.h> | 传输控制协议定义 |
| &lt;sys/mman.h> | 存储管理声明 |
| &lt;sys/select.h> | select 声明 |
| &lt;sys/socket.h> | 套接字接口 |
| &lt;sys/stat.h> | 文件状态 |
| &lt;sys/statvfs.h> | 文件系统信息 |
| &lt;sys/time.h> | 进程时间 |
| &lt;sys/types.h> | 基本系统数据类型 |
| &lt;sys/un.h> | UNIX套接字定义 |
| &lt;sys/utsname.h> | 系统名 |
| &lt;sys/wait.h> | 进程控制 |

#### Single UNIX Specification

这是POSIX.1的超集


---  
百日践行第2天
