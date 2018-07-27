# centos7安装pyton3.7
    1. 安装相关的软件
        yum -y groupinstall "Development tools"
        yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make expat-devel gdbm-devel cmake

    3.7版本需要一个新的包libffi-devel，安装此包之后再次进行编译安装即可。

    #yum install libffi-devel -y
    #make install
    若在安装前移除了/usr/bin下python的文件链接依赖，此时yum无法正常使用，需要自己下载相关软件包安装，为节省读者时间，放上链接

    #wget http://mirror.centos.org/centos/7/os/x86_64/Packages/libffi-devel-3.0.13-18.el7.x86_64.rpm
    #rpm -ivh libffi-devel-3.0.13-18.el7.x86_64.rpm
    安装完成后重新进行make install，结束后再次配置相关文件的软连接即可。

    2. 下载python3.7 tar.gz
        下载地址: https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz
        cd /usr/local
        wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz
        tar zxvf Python-3.5.0.tgz
        cd Python-3.5.0

        编译
        ./configure --prefix=/usr/local/python3.5

        安装
        make && make install

        建立软连接
        cd /usr/local/
        # ln -s python3.5 python
        mv /usr/bin/python /usr/bin/python.bak
        # ln -s /usr/local/python/bin/python3 /usr/bin/python3
        # ln -s /usr/local/python/bin/python3 /usr/bin/python
        # ln -s /usr/local/python/bin/python3.5 /usr/bin/python3.5
        # ln -s pip3 /usr/bin/pip3
        # ln -s pydoc3 /usr/bin/pydoc3
        # ln -s pyvenv /usr/bin/pyvenv
        # ln -s pip3 /usr/bin/pip

        查看版本
        [root@daheige local]# python -V
        Python 3.5.0

        因为执行yum需要python2版本，所以我们还要修改yum的配置，执行：

        vi /usr/bin/yum

        把#! /usr/bin/python修改为#! /usr/bin/python2.6

        将/usr/bin/python2先删除,然后建立软连接到python2.6

        同理 vi /usr/libexec/urlgrabber 文件里面的#! /usr/bin/python 也要修改为#! /usr/bin/python2.6
        这样python3版本就安装完成；同时python2也存在
        查看
         ll python*
        lrwxrwxrwx  1 root root   29 7月  28 01:12 python -> /usr/local/python/bin/python3
        lrwxrwxrwx  1 root root    9 7月  28 01:27 python2 -> python2.6
        -rwxr-xr-x. 2 root root 4864 8月  18 2016 python2.6
        -rwxr-xr-x  1 root root 1418 8月  18 2016 python2.6-config
        lrwxrwxrwx  1 root root   29 7月  28 01:12 python3 -> /usr/local/python/bin/python3
        lrwxrwxrwx  1 root root   31 7月  28 01:13 python3.5 -> /usr/local/python/bin/python3.5
        -rwxr-xr-x. 2 root root 4864 8月  18 2016 python.bak
        lrwxrwxrwx  1 root root   16 4月  21 18:49 python-config -> python2.6-config

        查看版本
        [root@daheige ~]# python
        Python 3.5.0 (default, Jul 28 2018, 01:08:49) 
        [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)] on linux
        Type "help", "copyright", "credits" or "license" for more information.

        [root@daheige ~]# python2.6
        Python 2.6.6 (r266:84292, Aug 18 2016, 15:13:37) 
        [GCC 4.4.7 20120313 (Red Hat 4.4.7-17)] on linux2
        Type "help", "copyright", "credits" or "license" for more information.
        




