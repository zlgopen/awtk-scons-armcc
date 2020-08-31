import os
import platform

def joinPath(root, subdir):
  return os.path.normpath(os.path.join(root, subdir))

CWD=os.path.normpath(os.path.abspath(os.path.dirname(__file__)));

TK_ROOT          = joinPath(CWD, '../awtk')
TK_SRC           = joinPath(TK_ROOT, 'src')
TK_3RD_ROOT      = joinPath(TK_ROOT, '3rd')
TK_PLATROM_ROOT  = joinPath(CWD, '../awtk-aworks-rt1052')
GTEST_ROOT       = joinPath(TK_ROOT, '3rd/gtest/googletest')

BUILD_DIR        = joinPath(CWD, 'build')
BIN_DIR          = joinPath(BUILD_DIR, 'bin')
LIB_DIR          = joinPath(BUILD_DIR, 'lib')
VAR_DIR          = joinPath(BUILD_DIR, 'var')
TK_DEMO_ROOT     = joinPath(TK_ROOT, 'demos')

LCD='CUSTOM'
INPUT_ENGINE='pinyin'
NANOVG_BACKEND='AGGE'

COMMON_FLAGS=' -DHAS_AWTK_CONFIG --cpu=Cortex-M7 --apcs=interwork --gnu'

COMMON_CFLAGS  = COMMON_FLAGS
COMMON_CCFLAGS = COMMON_FLAGS

OS_FLAGS=''
OS_LIBS=[]
OS_LIBPATH=[]
OS_CPPPATH=[]
OS_LINKFLAGS=''
OS_SUBSYSTEM_CONSOLE=''
OS_SUBSYSTEM_WINDOWS=''

OS_LIBS = OS_LIBS

LINKFLAGS=OS_LINKFLAGS;
LIBPATH=[LIB_DIR] + OS_LIBPATH
CFLAGS=OS_FLAGS + COMMON_CFLAGS 
CCFLAGS=OS_FLAGS + COMMON_CCFLAGS 

LIBS=['awtk', 'gpinyin', 'nanovg-agge', 'agge', 'nanovg', 'linebreak']

CPPPATH=[TK_ROOT, 
  TK_SRC, 
  TK_3RD_ROOT, 
  joinPath(TK_SRC, 'ext_widgets'), 
  joinPath(TK_3RD_ROOT, 'agge'), 
  joinPath(TK_PLATROM_ROOT, 'awtk-port'), 
  joinPath(TK_3RD_ROOT, 'agg/include'), 
  joinPath(TK_3RD_ROOT, 'nanovg'), 
  joinPath(TK_3RD_ROOT, 'nanovg/base'), 
  joinPath(TK_3RD_ROOT, 'libunibreak'), 
  joinPath(TK_3RD_ROOT, 'gpinyin/include'), 
  ] + OS_CPPPATH

os.environ['LCD'] = LCD
os.environ['TARGET_ARCH'] = 'arm'
os.environ['BIN_DIR'] = BIN_DIR;
os.environ['LIB_DIR'] = LIB_DIR;
os.environ['TK_ROOT'] = TK_ROOT;
os.environ['CCFLAGS'] = CCFLAGS;
os.environ['VGCANVAS'] = 'NANOVG'
os.environ['INPUT_ENGINE'] = INPUT_ENGINE;
os.environ['NANOVG_BACKEND'] = NANOVG_BACKEND;
os.environ['TK_3RD_ROOT'] = TK_3RD_ROOT;
os.environ['GTEST_ROOT'] = GTEST_ROOT;
os.environ['TOOLS_NAME'] = '';
os.environ['NATIVE_WINDOW'] = 'raw';
os.environ['GRAPHIC_BUFFER'] = 'default';
