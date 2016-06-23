# Zsh 终端shell

Zsh是一款强大的shell工具，可以帮助你高效编写和执行命令，bash替代品。使用前需要配置，不然很难用。

#####运行环境
Mac OS X && Linux

#####安装
Linux  
```
sudo apt-get install zsh
```

Mac
```
brew install zsh
```

#####使用
切换到zsh  
```
chsh -s /bin/zsh
```

配置，安装oh-my-zsh  
```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
cp ~/.zshrc ~/.zshrc.orig
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```
autojump插件必须添加，zsh和autojump组合才是最强王者。先下载   

Linux
```
sudo apt-get install autojump
```

mac
```
brew install autojump
```

然后把以下代码添加到.zshrc   
```
[[ -s ~/.autojump/etc/profile.d/autojump.sh ]] && . ~/.autojump/etc/profile.d/autojump.sh
```

最后添加需要的插件 ，打开配置文件.zshrc，参考如下修改  
```
plugins=(git osx autojump)
```

修改完毕执行  
```
source ~/.zshrc
```


详细配置信息见[oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)