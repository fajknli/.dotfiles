PC Overview
###############

恭喜你查看此文档，说明你开始遗忘过去的事情了，但你可以通过此文档重新开始。

1. VPS 外网连接
=================

这里使用的是dae作为代理软件，我做的有vA,和novA,一个进行连接，一个解除连接

vA 首先是查看dae.service服务有没有开启,然后再把dae需要的配置文件(自己放在.local/share/proxy-files-dae 里)复制到dae需要的地方，当作dae代理的配置，这样就可以直接修改这个目录里的文件就可以影响到dae的配置了

注意，这里有几个相关的目录:

.local/share/proxy-files-dae 是dae的配置文件(有专门的仓库)
.local/lib/shell/proxy 里面是shell脚本,是负责复制更新上面proxy-files-dae里的配置的

然后vA和novA的作用就是执行.local/lib/shell/proxy里的一些脚本，和启动/关闭dae服务的

主要用法就是:

直接克隆整个个人配置仓库，然后直接用就好了，如果要修改或者更新的话，直接去.local/share/proxy-files-dae里修改配置，比如节点地址

如果是更新geoip.dat和geosite.dat(负责过滤判断网站是否需要通过代理的文件),就执行.local/lib/shell/proxy里的download-geoip_geosite.sh这会去github里下载最新的geoip.dat和deosite.dat到.local/share/proxy-files-dae(应该会覆盖原文件吧，毕竟是更新),这里要注意得先要进外网，因为github下东西，你知道的。可以使用network-check.sh进行查看

还有个pull_dae_config_gitee.sh是负责把已经推送到仓库的proxy-files-dae拉取下来，替换掉旧的

2. dotfiles 的配置
=====================

dotfiles 是将系统所有常用配置都集合的东西，有了它，重新安装系统的话就可以根据它将系统配置恢复到和之前一样，每个人的dotfiles都不一样，所以这个东西很重要。

如果你是重新安装一个系统的话，要想恢复配置，首先得有vps,因为仓库在github需要外网，然后再使用裸仓库模式克隆仓库 `git clone --bare https://github.com/fajknli/.dotfiles.git $HOME/.dotfiles` 然后再到.bashrc里添加一个别名(alias) `alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'` 再刷新 `source ~/.bashrc` 
再把裸仓库的内容检出(恢复配置文件) `dotfiles checkout 2>&1 | grep -E "\s+\." | awk {'print $1'} | xargs -I{} mv {} {}.bak` (这个命令可以将已经有的文件进行备份，而不是直接覆盖),再 `dotfiles checkout`

如果有冲突报错就 `dotfiles checkout -f` 强制检出覆盖

再 `dotfiles config --local status.showUntrackedFiles no` 关闭未追踪文件显示，因为这个裸仓库在家目录，所以家目录所有的文件都会被显示为被追踪，很烦，就只关注已追踪的。

那如果已经恢复了，并且修改了配置或者添加了配置，怎么修改? 修改.local/bin/dots文件，如果要添加追踪文件的话，就在这个dots脚本里添加，删除也是。然后要更新什么的也直接运行这个dots脚本
