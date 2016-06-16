# 文件属性
---
#### 文件类型
UNIX下有七种文件类型：  
- **普通文件**，普通文件包含某种数据，无论是文本还是二进制数据，对于内核并无区别，对普通文件内容的解释由应用程序来完成，但是可执行程序是个例外，内核必需理解其格式。
- **目录文件**，这种文件包含了其他文件的名字以及指向这些文件的有关信息，进程只要对目录具有读权限就可以读取目录的内容，但是只有内核才可以直接写目录文件。
- **块特殊文件**，提供对设备带缓冲的访问，每次读取长度固定。
- **字符特殊文件**，提供对设备不带缓冲的访问，每次访问长度可变。
- **FIFO**, 用于进程间通信，有时也称为命名管道。
- **套接字**,用于进程间网络通信。
- **符号链接**,这种文件指向另一个文件。
文件类型信息包含在stat结构的st_mode,中可以用下面的宏来确定文件类型，这些宏的参数都是st_mode数据。
| 宏 | 文件类型 |
| ----- | ----- |
| S_ISREG| 普通文件 |
| S_ISDIR | 目录文件 |
| S_ISBLK |块特殊文件 |
| S_ISCHR | 字符特殊文件 |
| S_ISFIFO | FIFO或命名管道 |
| S_ISLINK | 符号链接 |
| S_ISSOCK| 套接字 |

#### 文件stat
stat的实际定义可能随具体实现有所不同，但其基本形式如下：
```
struct stat {
mode_t st_mode; //
ino_t st_ino; //
dev_t st_dev; //
dev_t st_rdev; //
nlink_t st_nlink; //
uid_t st_uid; //
gid_t st_gid; //
off_t st_size; //
struct timespec st_atime; //
struct timespec st_mtime; //
struct timespec st_ctime; //
blksize_t st_blksize; //
blkcnt_t st_blocks; //
```
stat 的四个操作函数定义如下
```
#include<sys/stat.h>

int stat(const char *restrict pathname, struct stat *restrict buf);
int fstat(int fd, struct *buf);
int lstat(const char *restrict pathname, struct stat *restrict buf);
int fstatat(int fd, const char *restrict pathname, struct stat *restrict buf, int flag);
//成功返回0 出错返回－1
```
使用stat函数最多的应该是`ls －l`命令，用ls可以获取一个文件的所有信息。














