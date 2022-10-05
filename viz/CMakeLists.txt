cmake_minimum_required(VERSION 3.17)
project(ArborXExamples CXX)

list(APPEND CMAKE_PREFIX_PATH "$ENV{HOME}/envs/stb_intel_13")

find_package(ArborX REQUIRED)
find_package(Boost COMPONENTS program_options)

add_executable(ArborX_TreeViz.exe tree_visualization.cpp)
target_link_libraries(ArborX_TreeViz.exe ArborX::ArborX Boost::program_options)

