# vim

一个文本编辑器，日常开发主要的代码编辑工具。

--- 

#####运行环境
Mac OS X && Linux

#####安装
Linux
```
sudo apt-get vim //这个版本自带lua和python3，免去自己编译的麻烦
```

Mac
```
brew info vim //先看一下安装选项
brew install vim --with-lua --with-override-system-vi  
//我的系统安装的时候报错：ld: library not found for -lruby.2.5.1,由于我已经用brew安装了ruby，所以我做了一个软连接重新安装即可
ln -s /usr/local/opt/ruby/lib/libruby.2.5.1.dylib /usr/local/lib/libruby.2.5.1.dylib
```

#####使用
1. 配置环境   
见我的github vim项目，最开始fork别人的配置再按自己需求修改的，用了一段时间之后切到了spf13-vim，很好很强大。


