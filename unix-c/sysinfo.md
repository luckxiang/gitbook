# 系统文件和信息

UNIX系统运行离不开数据文件的支持，如口令文件，组文件等，系统每次开机以及执行ls －l都需要调用口令文件。

#### 口令文件
口令文件是/etc/passwd，由于历史原因，这是一个ASCII文件，口令文件中的字段包含在<pwd.h>的passwd中，这些字段的格式基本上如下：

```
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
用户名：加密口令：数值用户ID：数值组ID：注释字段：初始工作目录：初始shell
```

关于这些登陆项，需要注意以下几点
-  通常有一个用户名为root的登陆项，其用户ID是0，0代表超级用户。
-  加密口令字段包含了一个占位符，早期的系统用这个字段存放加密口令字，但是这样会带来一个安全漏洞，所以现在把加密口令字存放在另一个文件中。
-  口令文件项的某些字段可能会为空，如果加密口令字段为空，则意味着该用户没有口令。
-  shell字段包含了一个可执行程序名，它被用作该用户的登陆shell，如果该字段为空的话，则采用系统默认值，通常是/bin/sh。
-  阻止一个特定用户登陆系统，可以把shll字段设为`/dev/null`，还可以用其他方式替代，如把shell字段设为`/bin/false`。
-  使用nobody用户名的目的是使任何人都可以登陆系统，其用户ID（65534）和组ID（65534）不提供任何特权，该用户ID和组ID只能访问人人皆可读写的文件。

POSIX.1定义了两个获取口令文件项的函数，再给出用户登陆ID名或数值用户ID后，就能查看相关项：

```
#include<pwd.h>

struct passwd *getpwuid(uid_t uid);
struct passwd *getpwnam(const char *name);
//成功返回指针，出错返回NULL
```

如果要查看整个口令文件，则可以使用下列函数：

```
#include<pwd.h>

struct passwd *getpwent(void);
void setpwent(void);
void endpwent(void);
```

#### 阴影口令
加密口令是经过单向加密算法处理过的用户口令副本，由于是不可逆的，所以无法从加密口令推导出用户口令，但是我们可以对口令进行猜测，将猜测的口令经过加密算法得出一个值，然后把这个值同用户的加密口令比较，这样痛过试探，就有可能获取到用户的密码，为了保护加密口令，现在某些系统把加密口令存放在另一个称为阴影口令的文件中，这个文件至少包含用户名和加密口令。与口令相关的其它信息也可以存放在该文件中。阴影口令文件不是普通用户可以访问的，只有少数几个程序需要访问加密口令，而这些程序通常是设置用户ID为root的程序，有了阴影口令文件，普通的口令文件就可以由各用户自由读取。相关的函数如下：

```
#include<shadow.h>

struct spwd *getspnam(const char *name);
struct spwd *getspent(void);
void setspent(void);
void endspent(void);
```
#### 组文件







