from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import os, sys
extra_include_path = []
extra_include_path.append(os.path.join(os.getcwd(),'psp'))

extra_lib_dir = []
if sys.platform == 'win32':
    lemon_lib_name = 'lemon'
else:
    lemon_lib_name = 'lemon'
    
if(os.environ.get('VCPKG_ROOT') and os.environ.get('VCPKG_DEFAULT_TRIPLET')):
    root_dir = os.environ['VCPKG_ROOT']
    triplet = os.environ['VCPKG_DEFAULT_TRIPLET']
    include_dir = os.path.join(root_dir, 'installed', triplet, 'include')
    if(os.path.exists(include_dir)):
        extra_include_path.append(include_dir)
    lib_dir = os.path.join(root_dir, 'installed', triplet, 'lib')
    if(os.path.exists(lib_dir)):
        extra_lib_dir.append(lib_dir)
# collect library
sourcefiles = ['psp.pyx']
for i in os.listdir(os.path.join(os.getcwd(),'psp','core')):
    if(i.find('cpp')>0):
        sourcefiles.append(os.path.join(os.getcwd(),'psp','core',i))
set_file = os.path.join(os.getcwd(),'psp','set', 'set_stl.cpp')        
if(os.path.exists(set_file)):
    sourcefiles.append(set_file)
else:
    raise FileNotFoundError(set_file)
    
extensions = [
    Extension('psp', sourcefiles, 
        include_dirs=extra_include_path,
        library_dirs=extra_lib_dir,
        libraries = [lemon_lib_name]
    )
]        

setup(
    ext_modules = cythonize(extensions)
)