# 集成 armcc 到 scons

集成 armcc 到 scons 中并不是件容易的事情，如果只是修改 CC/CXX/AR/LINK 几个环境变量，scons 会用 Visual C++的参数调用方式，比如-c 成了/c，导致 armcc 无法识别。

花了半天时间去阅读 scons 的源码后，在 SCons/Tool 目录下发现，每种编译器都有一个类似插件的 tool，目测没有发现 armcc 的 tool，自己为 armcc 写一个 tool，应该可以解决这个问题。

在 [ToolsForFools](https://github.com/SCons/scons/wiki/ToolsForFools) 这篇文章中，了解到可以自己定义 tool，只要放到项目的 site\_scons/site\_tools 目录下即可。

为了支持 armcc，我们在 site\_scons/site\_tools/armcc 目录中创建一个 armcc 的 tool，从头编写一个 tool 还是比较麻烦的，考虑到 armcc 和 cc 类似，就直接把 SCons/Tool/cc.py 拷贝到 site_scons/site_tools/armcc/\_\_init\_\_.py，然后在此基础上进行修改。

在下面这行代码之后

```python
add_common_cc_variables(env)
```

增加下面的代码：

```python
    armcc = SCons.Tool.find_program_path(env, 'armcc.exe');
    armar = SCons.Tool.find_program_path(env, 'armar.exe');
    armlink = SCons.Tool.find_program_path(env, 'armlink.exe');

    env['CC']      = armcc
    env['CXX']     = armcc
    env['AR']      = armar
    env['LINK']      = armlink
    env['CXXCOM']    = '$CC -o $TARGET -c $CFLAGS $CCFLAGS $_CCCOMCOM $SOURCES'
    env['ARFLAGS']     = SCons.Util.CLVar('--create -r')
    env['ARCOM']       = '$AR $ARFLAGS $TARGET $SOURCES'
    env['OBJSUFFIX']      = '.o'
    env['LIBPREFIX']      = 'lib'
    env['LIBSUFFIX']      = '.a'
```

参考 scons 的 Tool 中的代码，在 SConstruct 文件中，加入下面的代码，来启用我们前面定义的 armcc：

```python
env = DefaultEnvironment();
SCons.Tool.Tool('armcc')(env)
```

使用 scons 编译，编译正常了，但是在 armar 生成。a 文件时，出现下面的错误：

```
The command line is too long.
```

这主要是.o 文件太多所致，armar 并不像 ar 那样可以通过@符合去文件读取参数，不过 armar 可以先创建一个.a 文件，然后一个一个的往里面追加.o 文件。

从 scons 的源码发现，命令最终是在 SCons/Platform/win32.py 里调用的。但这是系统文件，直接修改它并不明智，我们还是写一个 tool 来解决这个问题吧。

为了避免从头去实现，把 SCons/Platform/win32.py 拷贝到 site\_scons/site\_tools/win4armcc/\_\_init\_\_.py，然后再去修改。

* 先修改下面几个变量的值为：

```python
    env['OBJSUFFIX']      = '.o'
    env['LIBPREFIX']      = 'lib'
    env['LIBSUFFIX']      = '.a'
```

* 增加一个 exists 函数

```
def exists(env):
    return True
```

* 重新实现 spawn 函数。

```python
def exe_ar(sh, cmd, args, env):
    armar = args[0]
    #args[1] is --create
    #args[2] is -r
    target = args[3];
    objs = args[4:]
    for i in range(len(objs)):
        ARFLAGS='-r'
        if i == 0:
            ARFLAGS='--create -r'

        all_args= [armar, target,  ARFLAGS, objs[i] ]
        sargs = ' '.join(all_args).replace('\\', '/');
        print(str(i) + ': ' + sargs);
        exec_spawn([sh, '/C', sargs], env)

def spawn(sh, escape, cmd, args, env):
    if cmd.endswith('armar.exe'):
        exe_ar(sh, cmd, args, env);
    else:
        sargs = ' '.join(args).replace('\\', '/');
        return exec_spawn([sh, '/C', sargs], env)
```

同样，在 SConstruct 文件中启用 win4armcc。

```python
SCons.Tool.Tool('win4armcc')(env)
```

好了，现在可以用scons调用armcc了。
