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

POSIX指的是可移植操作系统接口，他有多个标准，本书采用的是1003.1(POSIX.1)，这个标准的目的就是提升应用程序在各种UNIX环境之间的可移植性，它定义了符合POSIX的操作系统必须提供的各种服务，除了UNIX和类UNIX系统，还有其他一些操作系统也兼容POSIX标准。下面是POSIX指定的必需的和可选的头文件：

#### Single UNIX Specification

这是POSIX.1的超集


---  
百日践行第2天
