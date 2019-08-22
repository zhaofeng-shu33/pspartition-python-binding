# we use this setup.py to build wheels of info-clustering package
# this kind of installation is more flexible and maintainable than `cmake install`
# you can only choose one of the two installation methods.
# before running this file, make sure psp dynamic lib exists in build directory
import os,sys,platform
if(sys.platform == 'linux' and platform.linux_distribution()[0].find('CentOS') >= 0):
    IS_CENTOS = True
else:
    IS_CENTOS = False    
from setuptools import setup, Extension
from Cython.Build import cythonize

with open('README.md') as fh:
    long_description = fh.read()
    
def find_all_cpp(dir):
    cpp_list = []
    for dp, dn, fn in os.walk(dir):
        for i in fn:
            if(i.find('cpp')>0):
                cpp_list.append(os.path.join(dp, i))
    return cpp_list   
def add_source_file(sourcefiles, cpp_file):   
    if(os.path.exists(cpp_file)):
        sourcefiles.append(cpp_file)
    else:
        raise FileNotFoundError(cpp_file)
        
def set_up_cython_extension():
    extra_include_path = []
    extra_include_path.append(os.path.join(os.getcwd(),'psp'))

    extra_lib_dir = []
    if sys.platform == 'win32':
        lemon_lib_name = 'lemon'
    else:
        lemon_lib_name = 'emon'
        
    if(os.environ.get('VCPKG_ROOT')):
        root_dir = os.environ['VCPKG_ROOT']
        triplet = os.environ.get('VCPKG_DEFAULT_TRIPLET', 'x64-windows')
        include_dir = os.path.join(root_dir, 'installed', triplet, 'include')
        if(os.path.exists(include_dir)):
            extra_include_path.append(include_dir)
        lib_dir = os.path.join(root_dir, 'installed', triplet, 'lib')
        if(os.path.exists(lib_dir)):
            extra_lib_dir.append(lib_dir)
    # collect library
    sourcefiles = ['psp.pyx']
    sourcefiles.extend(find_all_cpp(os.path.join(os.getcwd(), 'psp', 'core')))
    set_file = os.path.join(os.getcwd(), 'psp', 'set', 'set_stl.cpp')    
    add_source_file(sourcefiles, set_file)
    thread_file = os.path.join(os.getcwd(), 'psp', 'preflow', 'InterruptibleThread', 'InterruptibleThread.cpp')
    add_source_file(sourcefiles, thread_file)
    extra_compile_flags_list = []
    if(sys.platform == 'darwin'):
        extra_compile_flags_list.append('-std=c++11')
    extensions = [
        Extension('info_cluster.psp', sourcefiles, 
            include_dirs=extra_include_path,
            library_dirs=extra_lib_dir,
            extra_compile_args=extra_compile_flags_list,
            libraries = [lemon_lib_name]
        )
    ]
    return cythonize(extensions)

ext_module_class = set_up_cython_extension()

setup(
    name='info_cluster',
    version='0.6', # python binding version, not the C++ lib version
    packages=['info_cluster'],
    ext_modules=ext_module_class,
    author="zhaofeng-shu33",
    author_email="616545598@qq.com",
    description="a hierachical clustering algorithm based on information theory",
    url="https://github.com/zhaofeng-shu33/principal_sequence_of_partition",
    long_description = long_description,
    long_description_content_type="text/markdown",        
    classifiers=[
        "Programming Language :: Python :: 3",
    ], 
    license="Apache License Version 2.0",
)
