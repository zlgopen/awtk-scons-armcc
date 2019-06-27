# awtk-scons-armcc
build awtk with scons and armcc  on windows

* 将awtk 和 本项目取到同一级目录。

```
https://github.com/zlgopen/awtk.git
https://github.com/zlgopen/awtk-scons-armcc.git
```

* 安装scons和keil，并设置好Path环境变量。

* 进入目录awtk-scons-armcc，并根据需要修改awtk_config.py，然后编译。

```
scons
```

> 目前只在python3上测试过。

工作原理请参考：[集成 armcc 到 scons](docs/build_awtk_with_scons_and_armcc.md)
