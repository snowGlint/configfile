# Mamba tutuorial

下载

```bash
curl 
-L https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh 
-o Mambaforge-Linux-x86_64.sh
```

启动  
`bash Mambaforge-Linux-x86_64.sh`  yes, init(yes)  然后重启终端：

```bash
(base) mamba deactivate # 退出base
mamba create -p /home/codespace/conda_software # 创建一个环境保存conda 软件
```

.bashrc添加 `PATH=$PATH:/workspaces/Drawplot/conda_software/bin` 然后重启终端。

```bash
mamba deactivate # 退出base
mamba activate /workspaces/Drawplot/conda_software # 进入该环境
```

https://anaconda.org/ 查软件下载命令

```bash
mamba install r-base=4.2  
mamba install python=3.10  
mamba install radian #在.bashrc 中设置radian 别名r: alias r='radian'
```

取消自动启动conda

```bash
conda config --set auto_activate_base false
```
