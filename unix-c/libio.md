# 标准IO库

---
标准IO库就是常说的C库，这个库由ISO C标准说明，标准IO库处理很多细节，如分配缓冲区，以优化的块长度执行IO等，它最终也需要调用文件IO。

#### 流和FILE对象
文件IO的所有IO函数都是围绕着文件描述符来的，打开一个文件的时候获得一个文件描述符，该描述符标记了这个文件。而标准IO库，则是围绕着流进行，当用标准IO打开或者创建一个文件的时候，我们就把一个流和一个文件相关联。对于ASCII字符集，一个字符用一个字节表示，对于国际字符集，一个字符可以用多个字节表示，即宽字符集。流的定向决定了读写的字符是字节流还是多字节流，创建一个流的时候并没有定向。若在未定向的流上使用单字节函数，则是字节定向，使用多字节函数，则是宽字节定向。只有两个函数可以改变流的定向，freopen和fwide
```
#include<stdio.h>
#include<wchar.h>

int fwide(FILE *fp, int mode);
//宽定向返回正值，字节定向返回负值，未定向返回0
```
fwide并不改变已经定向的流，而且也无出错返回。
当打开一个流时，我们打开了一个FILE对象，指向FILE对象的指针被叫做文件指针。FILE对象包含了管理该流所需要的所有信息，如实际IO的文件描述符，指向缓冲区的指针，缓冲区的长度，当前在缓冲区的字符数以及出错标志等。

#### 标准输入，标准输出，标准错误输出
对于一个进程来说，打开的时候和三个流自动绑定，就是标准输入，标准输出，标准错误输出。可以通过`stdin`,`stdout`,`stderr`引用。他们和文件IO的，`STDIN_FILENO`,`STDOUT_FILENO`,`STDERR_FILENO`对应。

#### 缓冲
文件IO不带缓冲，标准IO带有缓冲，标准IO带缓冲的目的主要是为了减少read和write调用，自动管理IO流的缓冲，从而使应用程序不需要考虑这一点。但是由于某些地方定义不够清楚，常常令人疑惑。IO提供三种缓冲机制，全缓冲，行缓冲，不带缓冲。
ISO C并没有详细的说明缓冲特征，很多系统入linux，mac OS X默认使用下列惯例：
- 标准错误是不带缓冲的。
- 若是指向终端设备的流，则是行缓冲，否则是全缓冲。
更改缓冲类型的函数如下：

```
#include<stdio.h>

void setbuf(FILE *restrict fp, char *restrict buf);
void setvbuf(FILE *restrict fp, char *restrict buf, int mode, size_t size);
//mode=_IOFBF | _IOLBF | _IONBF
//成功返回0 ，出错返回－1
```

调用函数fflush函数可以冲洗一个流，使该流所有未写的数据都被传送至内核，若fp＝NULL，则所有输出流都会被冲洗。

```
#include<stdio.h>

int fflush(FILE *fp);
//成功返回0，出错返回－1
```

#### 非格式化IO
IO操作一定要注意安全，不安全的函数十分危险，非格式化的IO操作有三种不同类型的操作：
- 每次一个字符的IO
- 每次一行的IO
- 直接IO

```
#include<stdio.h>

int getc(FILE *fp);
int fgetc(FILE *fp);
int getchar(void);
//成功返回下一个字符，出错或到达文件尾返回EOF

int putc(int c, FILE *fp);
int fputc(int c,FILE *fp);
int putchar(int c);
//成功返回次，出错返回EOF

char *fgets(char *restrict buf, FILE *restrict buf);
char *gets(char *buf);
//成功返回buf，出错或者到达文件尾部返回NULL

int fputs(const char *restrict str, FILE *restrict fp);
int puts(const char *buf);
//成功返回非负值，出错返回EOF
```

在FILE中维护了出错标志和文件结束标志，当返回EOF的时候并不能确定是出错还是到达文件尾部，可以用以下函数区分

```
#include<stdio.h>

int ferror(FILE *fp);
int feof(FILE *fp);
//条件为真返回真，否则返回0
void clearerr(FILE *fp);
```

还可以把读出来的字符又压回标准IO库的流缓冲区中，注意下次读出来的顺序和压回去相反。回送的字符，也不一定是上次读出来的字符，注意一次成功的ungetc会清除该流的文件结束标志

```
#include<stdio.h>

int ungetc(int c, FILE *fp);
//成功返回C，出错返回EOF
```
前边的都是字符操作，有时候我们想一次读写一个完整的结构或者二进制数组，标准IO库提供了读写二进制文件的操作函数。

```
#include<stdio.h>

size_t fread(void *restrist ptr, size_t size, size_t nobj, FILE *fp);
size_t fwrite(const void *restrist ptr, size_t size, size_t nobj, FILE *fp);
//返回读或者写的对象数
```

#### 格式化IO
```
#include<stdio.h>
int printf(const char *restrict format, ...);
int fprintf(FILE *restrict fp, const char *restrict format, ...);
int dprintf(int fd, const char *restrict format, ...);
//成功返回字符数，出错返回负值
int sprintf(char *restrict buf, const char *restrict format, ...);
成功返回存入数组的字符数，出错返回负值
int snprintf(char *restrict buf,size_t n, const cahr *restrict format, ...);
//若缓冲区足够大，返回存入数组的字符数，出错返回负值
```

```
#include<stdio.h>
int scanf(const cahr *restrict format);
int fscanf(FILE *restrict fp, const char *restrict format, ...);
int sscanf(const char *restrict buf, const char *restrict format, ...);
//返回负值的输入项数，出错或者到达文件尾返回EOF
```

```
#include<stdio.h>
int fileno(FILE *fp);
//返回与该流关联的文件描述符
```
#### 定位流

有三种方法定位标准IO流
- ftell和fseek函数
- ftello和fseeko函数
- fgetops和fsetops函数 ISOC标准，非unix需要用这两个函数

```
#inlcude<stdio.h>

int ftell(FILE *fp);
//成功返回当前文件指示，出错返回－1L
int fseek(FILE *fp, long offest, int whence);
//成功返回0，出错返回－1
void rewind(FILE *fp);
```

```
#include<stdio.h>
off_t ftello(FILE *fp);
//成功返回当前文件位置，出错返回(off_t)-1
int fseeko(FILE *fp, off_t offset, int whence);
//成功返回0，出错返回－1
```

```
#include<stdio.h>

int fgetpos(FILE *restrict fp, fpos_t *restrict pos);
int fsetops(FILE *fp, const fpos_t *pos);
//成功返回0，出错返回非0
```

#### 临时文件
有时候我们需要创建一些临时文件，ISO C 标准提供了下面一些函数：

```
#include<stdio.h>

char *tempnam(char *ptr);
//返回指向唯一路径名的指针

FILE *tmpfile(void);

//成功返回文件指针，出错返回NULL

char *mkdtemp(cahr *template);
//成功指向目录名的指针，出错返回NULL

char mkstemp(char *template);
//成功返回文件描述符，出错返回－1
```

#### 内存流
标准IO把数据缓存在内存中，因此每次一字符和每次一行更有效，我们也可以通过stebuf或setvbuf函数让IO库使用我们自己的缓冲区，

```
#include<stdio.h>

FILE *fmemopen(void *resirict buf, size_t size, const char *restrict type);
FILE *open_memstream(char **bufp, size_t *sizep);
//成功返回流指针，出错返回NULL

FILE* open_wmemstream(wchar_t **bufp, size_t *sizep);
```








