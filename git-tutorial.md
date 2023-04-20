# git tutorials

## git configuration

```git
git config --global  user.name  "xxx"
git config --global user.email  "706990@gmail.com"
git config --list # 列出所有配置信息
```

## git与github连接

```git
git remote add origin <https://github.com/snowGlint/easybio.git>
git push -u origin main
```

```git
git branch -m master main #修改分支名master为main
```

## workflow

```git
git clone # git clone 到本地
git checkout -b xxx # 切换至新分支xxx（相当于复制了remote的仓库到本地的xxx分支上
修改或者添加本地代码（部署在硬盘的源文件上）
git diff # 查看自己对代码做出的改变
git add # 上传更新后的代码至暂存区
git commit # 可以将暂存区里更新后的代码更新到本地git
git push origin xxx # 将本地的xxxgit分支上传至github上的git
```

如果在写自己的代码过程中发现远端GitHub上代码出现改变

```git
git checkout main # 切换回main分支
git pull origin master(main) # 将远端修改过的代码再更新到本地
git checkout xxx # 回到xxx分支
git rebase main # 我在xxx分支上，先把main移过来，然后根据我的commit来修改成新的内容（中途可能会出现，rebase conflict -----》手动选择保留哪段代码）
g​it push -​f origin xxx # 把rebase后并且更新过的代码再push到远端github上;（-f ---》强行）
```

原项目主人采用pull request中的 squash and merge合并所有不同的commit。

远端完成更新后：

```git
git branch -d xxx # 删除本地的git分支
git pull origin main  
```
