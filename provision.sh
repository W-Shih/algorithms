# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       provision.sh to set up virtual machine env
#
# =================================================================================================
#    Date      Name                    Description of Change
# 14-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================

#!/usr/bin/env bash

echo 'Start!'

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2

cd /vagrant

sudo apt-get update
sudo apt-get install tree

if [ ! -f "/usr/bin/pip" ]; then
  sudo apt-get install -y python3-pip
  sudo apt-get install -y python-setuptools
  sudo ln -s /usr/bin/pip3 /usr/bin/pip
else
  echo "pip3 已安装"
fi

# 升级 pip，目前存在问题，read timed out，看脸，有时候可以，但大多时候不行
# python -m pip install --upgrade pip
# 换源完美解决
# 安装pip所需依赖
pip install --upgrade setuptools      # -i https://pypi.tuna.tsinghua.edu.cn/simple # 清華鏡像
pip install --ignore-installed wrapt  # -i https://pypi.tuna.tsinghua.edu.cn/simple
# 安装 pip 最新版
pip install -U pip                    # -i https://pypi.tuna.tsinghua.edu.cn/simple
# 根据 requirements.txt 里的记录安装 pip package，确保所有版本之间的兼容性
pip install -r requirements.txt       # -i https://pypi.tuna.tsinghua.edu.cn/simple

# 如果想直接进入 /vagrant 路径下
# 请输入 vagrant ssh 命令进入
# 手动输入
# 输入 ls -a
# 输入 vi .bashrc
# 在最下面，添加cd /vagrant

echo 'All Done!'
