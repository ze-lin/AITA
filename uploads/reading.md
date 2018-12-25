+++
title = "自动删除Mac版迅雷无用组件"
date = 2018-10-15T16:23:24+08:00
tags = ["Shell",  "Mac"]
draft = false
weight = 0

+++

最近发现Github上这个项目陆陆续续收获了三个Star（没错，就这么土鳖，三个就很开心了）。感觉大家对这段脚本还是有一点点需求的，写一篇文章，希望能帮助到有需要的人吧。

<!--more-->

懒得往下看的朋友可以直接戳下方链接去项目地址了，README有使用方法和**注意事项（请务必阅读）**。

项目地址：[ThunderPlugInsDeleter-macOS](https://link.zhihu.com/?target=https%3A//github.com/ludanxer/ThunderPlugInsDeleter-macOS)

如果你在用Mac版迅雷的话，刚下载下来是这个样子的：

![thunder-before](/images/thunder-before.png)

天啊！我只想要个下载工具，我下了个什么？？？这还不算完，等你打开某些视频的时候，发现你莫名其妙的开始使用了XLPlayer播放工具，XL（迅雷）Player又是什么鬼？？？

你在网上搜索，可以得到相应的解决方法。删除路径

```text
/Applications/Thunder.app/Contents/PlugIns/
```

下的一系列的稀奇古怪的组件（容我吐槽一下那些组件的命名方式），即可还你一个清爽的迅雷界面，我曾经也是手动一个个删除的。但是作为一个有更新强迫症的人，每次发现存在更新后都会升级，而每次升级后都需要手动删除，这也实在是太麻烦了！

懒惰是第一生产力，这个项目就应运了。用简单的shell脚本代替手动删除，当然原理还是删除那些没用组件们了。效果图如下：

![thunder-after](/images/thunder-after.png)

是不是感觉整个世界清爽了许多？每次更新完毕之后，只需要再次执行脚本即可，不再需要进入目录下一个个删除了！

需要使用的话，点击下方的链接进入项目主页，README里面有**注意事项（请务必阅读）**和简单的使用说明哦。

项目地址：[ThunderPlugInsDeleter-macOS](https://link.zhihu.com/?target=https%3A//github.com/ludanxer/ThunderPlugInsDeleter-macOS)