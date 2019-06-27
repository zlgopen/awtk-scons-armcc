import os
import platform
import SCons.Tool
import awtk_config as awtk

DefaultEnvironment(CCFLAGS = awtk.CCFLAGS, 
  CFLAGS = awtk.CFLAGS,
  LIBS = awtk.LIBS,
  LIBPATH = awtk.LIBPATH,
  CPPPATH = awtk.CPPPATH,
  LINKFLAGS = awtk.LINKFLAGS,
  OS_SUBSYSTEM_CONSOLE=awtk.OS_SUBSYSTEM_CONSOLE,
  OS_SUBSYSTEM_WINDOWS=awtk.OS_SUBSYSTEM_WINDOWS
)

env = DefaultEnvironment();
SCons.Tool.Tool('armcc')(env)
SCons.Tool.Tool('win4armcc')(env)

TK_ROOT_VAR = awtk.joinPath(awtk.VAR_DIR, 'awtk')
VariantDir(TK_ROOT_VAR, awtk.TK_ROOT)

SConscriptFiles=[
  awtk.joinPath(TK_ROOT_VAR, '3rd/nanovg/SConscript'),
  awtk.joinPath(TK_ROOT_VAR, '3rd/agge/SConscript'),
  awtk.joinPath(TK_ROOT_VAR, '3rd/gpinyin/SConscript'), 
  awtk.joinPath(TK_ROOT_VAR, '3rd/libunibreak/SConscript'),
  awtk.joinPath(TK_ROOT_VAR, 'src/SConscript'),
  'awtk-port/SConscript',
];

SConscript(SConscriptFiles)

