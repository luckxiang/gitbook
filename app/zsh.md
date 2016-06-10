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

添加插件 ，打开配置文件.zshrc，参考如下修改  
```
plugins=(git osx)
```

修改完毕执行  
```
source ~/.zshrc
```

详细配置信息见[oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)