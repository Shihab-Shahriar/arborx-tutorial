#!/bin/bash

rm -f CMakeCache.txt

export CUDA_LAUNCH_BLOCKING=1
export OMP_PROC_BIND=true

cmake \
 -D CMAKE_CXX_COMPILER=g++ \
 -D CMAKE_INSTALL_PREFIX="$SFTPATH" \
 -D Kokkos_ENABLE_OPENMP=ON \
 -D Kokkos_ARCH_KEPLER37=ON \
 -D Kokkos_ENABLE_TESTS=On \
 ../
