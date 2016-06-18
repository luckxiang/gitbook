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

#### 用户ID和组ID
和一个进程相关联的ID至少有6个

| ID | 作用 |
| ----- | ----- |
| 实际用户ID和实际组ID | 我们是谁，取自口令文件登录项，只有超级进程可以改变 |
| 有效用户ID和有效组ID | 用于文件访问权限检查 |
| 保存的设置用户ID和组ID | 由exec函数保存 |
当执行一个程序文件的时候，进程的有效ID通常就是实际ID，但是在st_mode中有两个位被称为设置用户ID和设置组ID，可以由S_ISUID和S_ISGID测试，他们在进程执行时，可以把进程的有效ID设置为文件所有者的ID。所以编写这样的函数需要特别小心，

#### 文件访问权限
一个文件有9个访问权限位，分为user,group,other。如｀drwxr-xr-x｀，第一位表示他是一个目录。
`S_IEUSR|S_IWUSR|S_IXUSR,S_IEGRP|S_IWGRP|S_IXGRP,S_IEOTH|S_IWOTH|S_IXOTH`

#### 访问权限测试
```
#include<unistd.h>

int access(const char *pathname, int mode);//mode=R_OK | W_OK | X_OK
int faccess(ingt fd, const char *pathname, int mode, int flag);
//成功返回0 ，出错返回－1
```

#### 创建文件屏蔽字
```
#include<sys/stat.h>

mode_t umask(mode_t cmask);／／cmask=S_IRUSR|S_IWUSR...等或成
//返回之前的文件模式创建屏蔽字
```
进程创建新文件一定会使用umask，open和creat都有一个mode参数，

#### 文件权限修改
改变文件的权限，进程必须是超级用户权限或者有效用户ID等于文件的所有者ID
```
#include<sys/stat.h>

int chmod(const char *pathname, mode_t mode);
int fchmod(int fd, mode_t mode);
int fchmodat(int fd , const char *pathname, mode_t mode,int flag);
//成功返回0 ，出错返回－1
```

#### 更改文件的用户ID和组ID
```
#include<unistd.h>

int chown(const char *pathname, uid_t owner, gid_t group);
int fchown(int fd, uid_t owner, gid_t group);
int fchownat(int fd, const char *pathname, uid_t owner, git_t group, int flag);
int lchown(const char *pathname, uid_t owner, git_t group);
//成功返回0 ，出错返回－1
```
这四个函数操作类似，在符号链接情况下，lchown，fchownat(flag=AT_SYMLINK_NOFOLLOW)更改符号链接本身的所有者，而不是指向该符号链接所指向的文件的所有者。
基于BSD的系统只允许超级用户更改文件的所有者，而System V允许任一用户更改他所拥有的文件的所有者，POSIX.1允许在这两种操作中选用一种，由宏`_POSIX_CHOWN_RESTRICTED`控制，它可以用pathconf和fpathconf函数查询，还可以在每个文件系统基础上，使该选项起作用或不起作用。

#### 文件长度
stat的结构成员st_size表示以字节为单位的文件长度，此字段只对普通文件，目录文件和符号链接有意义。此外，大多数UNIX系统还提供st_blocksize,st_blocks,第一个是对文件IO较合适的块长度，第二个是所分配的实际xx字节字节块块数。xx由系统制定。st_blocksize用于读写操作时，读写一个文件所需的时间最少。

#### 文件的空洞
文件的空洞是由所设置的偏移量超过文件尾端照成的，除非写入数据，空洞可能不会占用实际物理内存，但是如果复制这个文件，那么新文件的空洞都会被0填满。

#### 文件截断
O_TRUNC可以把文件截断为0，此外截断文件还可以调用下面的函数
```
#include<unistd.h>

int truncate(const char *pathname, off_t length);
int ftruncate(int fd, off_t length);
//成功返回0，出错返回－1
```


