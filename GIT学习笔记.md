# Git 学习笔记

## 1. 什么是 Git
Git 是一个开源的分布式版本控制系统，能够高效地处理各种大小的项目。
现在我用我的大白话来记录一下我对于git的理解。首先我们为什么会需要使用git？比如现在我们这个组10个人在开发一个软件，那么很显然我们10个人肯定每个人有每个人的分工，
比如我负责开发自动驾驶，A负责开发外观，B负责开发电门不啦不啦，那么我们每个人对应的在文件里工作的区域也就不一样，那么我们每个人在修改完一个部分后都会上传自己修改过后的版本。
那么现在问题来了，我们怎么知道这个版本你修改到了最新，另外9个人呢？我们应该怎么检查呢？所以，这就需要GIT来帮助我们，它可以完整记录我们的每一个副本到资源库里来帮助我们实现版本控制！

## 2. Git 基本命令

| 作用 | 命令 | 备注 |
| ---- | ---- | ---- |
| 设置用户名 | `git config --global user.name "whu-ljy"` | 配置用户名 |
| 设置邮箱 | `git config --global user.email "1321792054@qq.com"` | 配置邮箱 |
| 初始化一个新的 Git 仓库 | `git init` | 创建仓库 |
| 克隆一个远程仓库 | `git clone https://github.com/user/repository.git` | 克隆仓库 |
| 查看文件状态 | `git status` | 查看仓库当前状态 |
| 添加文件到暂存区 | `git add filename` | 添加文件 |
| 提交文件 | `git commit -m "提交信息"` | 提交更改 |
| 查看提交历史 | `git log` | 查看历史 |
| 查看所有分支 | `git branch` | 查看分支 |
| 创建新分支 | `git branch new-branch` | 创建分支 |
| 切换到新分支 | `git checkout new-branch` | 切换分支 |
| 创建并切换到新分支 | `git checkout -b new-branch` | 创建并切换分支 |
| 切换到主分支 | `git checkout main` | 切换到主分支 |
| 合并分支 | `git merge new-branch` | 合并分支 |
| 查看远程仓库 | `git remote -v` | 查看远程 |
| 添加远程仓库 | `git remote add origin https://github.com/user/repository.git` | 添加远程 |
| 推送到远程仓库 | `git push origin main` | 推送远程 |
| 拉取远程仓库的更新 | `git pull` | 拉取远程 |
| 撤销工作区的更改 | `git checkout -- filename` | 撤销更改 |
| 重置暂存区的文件 | `git reset HEAD filename` | 重置暂存区 |
| 重置到上一个提交 | `git reset --hard HEAD^` | 回退版本 |
