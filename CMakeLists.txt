cmake_minimum_required(VERSION 3.12)

project(ic LANGUAGES CXX)

option(USE_CXX11_ABI "USE GLIB CXX11 ABI" ON)

if(NOT USE_CXX11_ABI)
    add_definitions("-D_GLIBCXX_USE_CXX11_ABI=0")
endif()

if(WIN32)
    set(DYNAMIC_LIB_SUFFIX dll)
elseif(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")    
    set(DYNAMIC_LIB_SUFFIX dylib)
else()
    set(DYNAMIC_LIB_SUFFIX so)
endif()

include_directories(${PROJECT_SOURCE_DIR})

find_package(lemon REQUIRED)
include_directories(${LEMON_INCLUDE_DIR})

if("$ENV{APPVEYOR}" AND WIN32) # appveyor tries to find py37, in which vcpkg(2018.11) does not support
    set(Python3_ROOT_DIR C:/Python36-x64)
endif()

find_package(Python3 COMPONENTS Interpreter Development)
    
    
if(WIN32)
    find_package(Boost REQUIRED python${Python3_VERSION_MAJOR}${Python3_VERSION_MINOR})
elseif(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    find_package(Boost REQUIRED python${Python3_VERSION_MAJOR}${Python3_VERSION_MINOR})    
else()
    string(FIND ${CMAKE_SYSTEM} "el" IS_ENTERPRISE_LINUX)
    if(${IS_ENTERPRISE_LINUX} STREQUAL -1) # not enterprise linux
        find_package(Boost REQUIRED python-py${Python3_VERSION_MAJOR}${Python3_VERSION_MINOR})    
    else()
        set(BP Boost_PYTHON-PY${Python3_VERSION_MAJOR}${Python3_VERSION_MINOR}_LIBRARY_RELEASE)
        set(${BP} ${Boost_LIBRARY_DIR_RELEASE}/libboost_python3-mt.so.${Boost_MAJOR_VERSION}.${Boost_MINOR_VERSION}.${Boost_SUBMINOR_VERSION} CACHE type FILEPATH)
    endif()
endif()
    
add_library(psp SHARED psp.cpp)
target_include_directories(psp PUBLIC ${Python3_INCLUDE_DIRS})
target_include_directories(psp PUBLIC ${Boost_INCLUDE_DIRS})
    
if(WIN32)
    target_link_libraries(psp debug ${Boost_PYTHON${Python3_VERSION_MAJOR}${Python3_VERSION_MINOR}_LIBRARY_DEBUG})    
    target_link_libraries(psp optimized ${Boost_PYTHON${Python3_VERSION_MAJOR}${Python3_VERSION_MINOR}_LIBRARY_RELEASE})
elseif(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    target_link_libraries(psp ${Boost_PYTHON${Python3_VERSION_MAJOR}${Python3_VERSION_MINOR}_LIBRARY_RELEASE})
else()
    target_link_libraries(psp ${Boost_PYTHON-PY${Python3_VERSION_MAJOR}${Python3_VERSION_MINOR}_LIBRARY_RELEASE})
endif()

if(USE_LEMON)
    if(UNIX)
        set_target_properties(psp PROPERTIES LINK_FLAGS "-fPIC")
    endif()
    target_link_libraries(psp ${LEMON_LIBRARY})
endif()    

# magic files to extract the release library

target_link_libraries(psp ${Python3_LIBRARIES}) 

if(WIN32)
  # install debug type dll
  set(DYNAMIC_LIB_SUFFIX pyd)
  add_custom_command(TARGET psp POST_BUILD COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:psp> ${PROJECT_SOURCE_DIR}/info_cluster/psp.${DYNAMIC_LIB_SUFFIX})
endif()
    

include_directories(psp)
include_directories(${PROJECT_BINARY_DIR}/psp)
add_subdirectory(psp)
target_link_libraries(psp ic_static)
target_link_libraries(psp set_stl)
