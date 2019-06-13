# this file is only used for debugging
cmake_minimum_required(VERSION 3.12)
if(WIN32 AND DEFINED ENV{VCPKG_ROOT})
  set(CMAKE_TOOLCHAIN_FILE "$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake"
      CACHE STRING "")
endif()
project(ic LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

option(USE_CXX11_ABI "USE GLIB CXX11 ABI" ON)

if(NOT USE_CXX11_ABI)
    add_definitions("-D_GLIBCXX_USE_CXX11_ABI=0")
endif()

if(WIN32)
    set(DYNAMIC_LIB_SUFFIX pyd)
else()
    set(DYNAMIC_LIB_SUFFIX so)
endif()

include_directories(${PROJECT_SOURCE_DIR})

find_package(lemon REQUIRED)
include_directories(${LEMON_INCLUDE_DIR})

find_package(Python3 COMPONENTS Development)   

    
add_library(psp SHARED psp.cpp)
target_include_directories(psp PUBLIC ${Python3_INCLUDE_DIRS})
target_include_directories(psp PUBLIC ${Boost_INCLUDE_DIRS})
    

if(UNIX)
    set_target_properties(psp PROPERTIES LINK_FLAGS "-fPIC")
endif()

target_link_libraries(psp ${LEMON_LIBRARY})
target_link_libraries(psp ${Python3_LIBRARIES}) 

add_custom_command(TARGET psp POST_BUILD COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:psp> ${PROJECT_SOURCE_DIR}/info_cluster/psp.${DYNAMIC_LIB_SUFFIX})
    
include_directories(psp)
add_subdirectory(psp/core)
add_subdirectory(psp/set)
target_link_libraries(psp ic_static)
target_link_libraries(psp set_stl)