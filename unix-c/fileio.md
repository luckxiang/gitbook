# 文件IO
---
UNIX的文件IO常被称为不带缓冲的IO，与之相对应的是标准IO，不带缓冲不是指不经过缓存区，而是说每一个read和write都调用内核中的系统调用，对于内核而言，所有打开的文件都通过文件描述符引用，文件描述符是一个非负整数，没打开或者创建一个文件，内核就会返回一个文件描述符，后续的操作都需要使用这个描述符来标记文件。

#### 打开文件
```
#include<fcntl.h>

int open(const char *path, int oflag, .../*mode_t mode*/);
int openat(int fd, const char *path, int oflag, .../*mode_t mode*/);
//两函数的返回值，成功返回文件描述符的值，错误返回－1
```    
fd参数把openat和open区别开来     
- 当path是绝对路径名的时候，open等于openat。
- 当path是相对路径名的时候，fd指出来相对路径名在文件系统中的开始位置，其中fd通过打开相对路径名所在的路径来获取。
- 当path是相对路径名，fd的值是特殊值AT_FDCWD时，路径名在当前工作目录中获取。
openat主要是为了解决两个问题，第一个问题是让线程可以使用相对路径来打开文件，而不再只能打开当前工作目录，同一进程的线程共享同一个工作目录，很难让他们工作在不同的目录中，如果要用绝对路径的话，使用上又会受到很多限制。第二个问题是解决TOCTTOU(time-of-check-to-time-of-use)问题，提高程序的安全性。   
当文件名或路径名超出了系统规定的最大长度时，是截断还是返回出错由常量_POSIX_NO_TRIUNC决定。

#### 创建文件
```
#include<fctl.h>

int creat(const char *path, mode_t mode);
//成功返回只写打开的文件描述符，出错返回－1
```
等同于函数      
`open(path, O_WRONLY | O_CREAT | O_TRUNC, mode);`       
因为可以用open替代，于是也不用需要单独的open函数了。

#### 关闭文件
```
#include<unistd.h>

int close(fd);
//成功返回0，出错返回－1
```
关闭一个文件还会释放加在该文件上的所有记录锁，当一个进程关闭时，内核自动关闭它打开的所有文件，因此可以利用这一功能而不用显式的调用close函数。

#### 设置偏移
```
#include<unistd.h>

off_t lseek(int fd, off_t offset, int whence);
//成功返回新的文件偏移量，出错返回－1
```
whence可取的值为`SEEK_SET`,`SEEK_CUR`,`SEEK_END`,如果fd指向的是一个管道，FIFO或者网络套接字，则返回－1，并将errno设置为ESPIPE,利用这一点可以测试文件是否可以设置偏移量，某些设备也可能允许负的偏移量，所以不能测试lseek的返回值是否小于0，lseek不会引起任何IO操作，他把偏移量记录在内核中，在下一次读或者写的时候生效，假如偏移量大于文件，则会在文件中形成一个空洞，有趣的是这个空洞并不要求占用存储区。具体实现和文件系统有关，但是新写的数据则会分配内存块。

#### 读文件
```
#include<unistd.h>

ssize_t read(int fd, void *buf, size_t nbytes);
//返回读到的字节数，若到文件尾，返回0，出错返回－1
```

#### 写文件
```
#include<unistd.h>

ssize_t write(int fd, void *buf, size_t nbytes);
//成功返回已写的字节数，出错返回－1
```

#### IO效率
当一次读取文件的BUFF_SIZE大小等于磁盘块长度的时候，IO的效率达到最大值。


#### 文件共享的方式

在内核中打开文件会维护三张表，一张进程表，一张文件表，一张节点表，不同的进程打开相同的文件，他们的进程表，文件表都不一样，但是节点表是一样的，相当于是一个实体的不同引用。

#### 复制文件描述符
```
#include<unistd.h>

int dup(fd);
int dup2(int fd, int fd2);
//成功返回新的描述符，出错返回－1
```
这两个函数可以实现重定向，他们返回的描述符和原来的描述符指向同一个文件节点，`dup`返回的是当前可用的描述符中的最小值，`dup2`函数则可以用fd2指定新描述符的值，如果fd2打开，则先把他关闭，如果fd2等于fd，则不关闭该文件直接返回fd2。

#### 改变打开文件的属性
```
#include<unistd.h>

int fcntl(int fd, int cmd, .../*int arg*/);
```
这个函数有五种功能，
- 复制已有描述符，cmd=F_DUPFD | cmd=F_UDUPFD_CLOEXEC
- 获取／设置文件描述符标志 cmd=F_GETFD | cmd=F_SETFD
- 获取／设置文件状态标志 cmd=F_GETFL |cmd=F_SETFL
- 获取／设置异步IO所有权 cmd=F_GETTOWN |cmd=F_SETTOWN
- 获取／设置记录锁 cmd=F_GETLK |cmd=F_SETLK |cmd=F_SETLKW

#### ioctl
ioctl，用来扩展其他IO操作，每个设备驱动都可以定义一组自己专用的ioctl命令。

####/dev/fd
打开`/dev/fd/n`等效于复制描述符n。且他拥有的模式是原来描述符n的子集或等于原来描述符的mode，具体和系统实现有关。这种文件操作方式主要提供给shell用。






