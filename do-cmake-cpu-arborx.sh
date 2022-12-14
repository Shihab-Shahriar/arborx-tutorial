#!/bin/bash

rm -f CMakeCache.txt

export CUDA_LAUNCH_BLOCKING=1
export OMP_PROC_BIND=true

cmake \
-D CMAKE_INSTALL_PREFIX="${SFTPATH}" \
-D Kokkos_ROOT="${SFTPATH}" \
-D ARBORX_ENABLE_EXAMPLES=ON \
-D ARBORX_ENABLE_MPI=OFF \
-D CMAKE_CXX_EXTENSIONS=OFF \
 ../