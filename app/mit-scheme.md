# mit-scheme


《计算机程序的构造与解释》一书中使用的scheme解释器，练习lisp的必备工具。

---

#####运行环境
Mac OS X

#####安装
```
brew install Caskroom/cask/xquartz
brew install homebrew/x11/mit-scheme
```
#####使用

1. 编辑test.scm文件并保存。
2. 终端运行mit－scheme解释器。
3. 编译源代码，在解释器输入命令：
```
(cf "test")
```

4. 加载，在解释器输入命令：
```
(load "test.scm")
```