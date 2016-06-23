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

#### 文件系统
我们可以把一个磁盘分成一个或者多个分区，每个分区可以包含一个文件系统，文件系统mount在根文件系统下，`i`节点是固定长度的记录项，它包含有关文件系统的大部分信息。每一个`i`节点都有一个链接计数，表示有多少个目录项指向该文件，只有计数为0时才能删除该文件。在stat结构中，链接计数包含在st_nlink中，这种链接类型称为硬链接。还有一种链接是符号链接（软链接），在软链接中包含了实际指向的文件的名字，stat中大多数信息都来自`i`节点。只有文件名和i节点编号存在目录项中，需要注意的是目录项中的`i`节点编号指向同一个文件系统中的相应`i`节点，这也是ln创建的硬链接不能跨越文件系统的原因。

#### LINK操作
任何一个文件可以有多个目录项指向其`i`节点，创建一个指向现有文件的链接方法是用link和linkat函数，相关操作具体如下
```
#include<unistd.h>

int link(const char *existngpath, const char *newpath);
int linkat(int efd, chonst char * existngpath, int nfd, const char *newpath, int flag);
int ulink(const char *pathname);
int ulinkat(int fd, const char *pathname, int flag);
int remove(const char *pathname);
//成功返回0，出错返回－1
```
对于文件remove等于ulink，对于目录，remove等雨rmdir


#### 文件目录重命名
```
#include<stdio.h>

int rename(const char *oldname, const char *newname);
int renameat(int oldfd,const char *oldname, int newfd, const char *newname);
//成功返回0，出错返回－1
```

#### 符号链接
符号链接是对一个文件的间接指针，而硬链接直接指向文件得`i`节点，两者区别如下：
- 硬链接通常要求文件和链接位于同一个文件系统中。
- 只有超级用户才能创建指向目录的硬链接，需要底层文件系统支持，但是这样会带来循环的隐患。
- 对符号链接以及它指向何种对象和文件系统并没有限制，一般用于将文件和目录移到系统的另一个位置。我开发的时候经常会用到这个操作。多种方案共用一个符号链接指向不同的目录。

```
#include<unistd.h>

int symlink(const char *actualpath, const char *sympath);
int symlinkat(const char *actualpath, int fd, const cahr *sympath);
//成功返回0，出错返回－1
```
由于open跟随符号链接，打开链接会打开实际的目录或者文件所以需要一个方法打开链接本身并读取链接中的名字

```
#include<unistd.h>

ssize_t readlink(const char *restrict pathname, char *restrict buf, size_t bufsize);
ssize_t readlinkat(int fd, const char *restrict pathname, char *restrict buf, size_t bufsize);
//成功返回读取的字节数，失败返回－1
```
#### 文件时间
对于每个文件维护三个时间段，如图所示：

| 字段 | 说明 | 例子 | ls选项 |
| ----- | ----- | ----- | ----- |
| st_atim | 文件数据的最后访问时间 | read | -u |
| st_mtim | 文件数据的最后修改时间 | write | 默认 |
| st_ctim | i节点状态的最后修改时间 | chmod,chown | -c |

相关操作函数如下：

```
#include<sys/stat.h>

int futimens(int fd, const struct timespec times[2]);
int utimensat(int fd, const char *path, const struct timespec times[2], int flags);
//成功返回0，出错返回－1
```

```
#include<sys/time.h>

struct timeval{
  time_t tv_sec;/* seconds */
  long tv_usec;
};

int utime(const char *pathname, const struct timeval times[2]);
//成功返回0，出错返回－1
```

#### 目录操作
目录需要执行权限，以允许访问该目录中的文件名。`.`,`..`目录项自动创建。

```
＃include<sys/stat.h>
int mkdir(const char *pathname, mode_t mode);
int mkdirat(int fd, const char *pathname, mode_t mode);
//成功返回0，出错返回－1

#inlcude<unistd.h>
int rmdir(const char *pathname);
//成功返回0，出错返回－1

#include<dirent.h>
DIR opendir(const cahr *pathname);
DIR fdopendir(int fd);
//成功返回指针，出错返回NULL

struct dirent *readdir(DIR *dp);
//成功返回指针，若在目录尾或出错返回NULL

void rewinddir(DIR *dp);

int closedir(DIR *dp);
//成功返回0，出错返回－1

long telldir(DIR *dp);
//返回与dp关联的目录中的当前位置

void seekdir(DIR *dp, long loc);
```

每个进程都有一个当前工作目录，可以通过chdir和fchdir更改，注意当前工作目录是进程的一个属性，修改不会影响其他进程。这也是cd命令内建在shell中的原因。

```
#include<unistd.h>

int chdir(const char *pathname);
int fchdir(int fd);
//成功返回0，出错返回－1
```

内核不保存完整的路径名，但是Linux可以确定完整的路径名，我们需要一个函数来获取获取绝对路径

```
＃include<unistd.h>

char *getcwd(cahr *buf, size_t size);
//成功返回buf，出错返回NULL，buf必须足够大，否则返回出错。
```

##### 设备特殊文件
每个文件系统的存储设备都有主次设备号表示，可以用major和minor宏命令获取，st_dev和st_rdev经常容易混淆，前者表示的是文件系统的设备号，后者只有字符和块设备才有，包含了实际设备的设备号。对同一磁盘的不同文件系统，通常主设备号相同，次设备号不同。







