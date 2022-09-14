Files mentioned below are available in https://github.com/Shihab-Shahriar/arborx-tutorial repository.
## Installing Arborx

+ Official Doc for installation can be found [here](https://github.com/arborx/ArborX/wiki/Build).

### Installing Kokkos
+ First we will have to install Kokkos. Here we'll go with a simple Kokkos installation without GPU support for now. To do this, clone the kokkos [source](https://github.com/kokkos/kokkos) in your HPCC machine. 
	+ Copy `do-cmake-cpu-kokkos.sh`in the source directory. This will be used to configure the CMake settings for Kokkos. 
	+ Also copy `compile-kokkos.py`. 
+ Load necessary modules:
```			
    module load GCC/8.3.0 CUDA/10.1.243 OpenMPI/3.1.4
    module load CMake/3.17.1
    module load imkl/2019.5.281
 ```

+ From the Kokkos source root, run `python3 ./compile-kokkos.py`. This will use `do-cmake-cpu-kokkos.sh`to configure and build Kokkos, among other things.

If it goes well, kokkos will be installed in `$HOME/envs/stb_intel_13/` directory.

### Installing ArborX
+ Copy the [source](https://github.com/arborx/ArborX) in HPCC.
+ Copy both `do-cmake-cpu-arborx.sh` and `compile-arborx.py`files to the source directory.
+ Run `python3 ./compile-arborx.py`. 

There should be a `build_Arborx-CPU` folder inside source directory if all goes well. It'll contain several built examples too that you can play with.

## Compiling Against ArborX
 We'll now build a simple example that uses ArborX, and verify that it works by comparing with Python's scipy module, which also provides nearest neighbor search functionalities. The example will be borrowed from [SimToolBox repo](https://github.com/wenyan4work/SimToolbox/tree/dev)'s `dev`branch.
+ Copy all the contents inside `MPI/TEST2_POINTCLOUD`into a local directory.
+ Replace texts inside CMakeLists.txt with the text in CMakeLists-Pointcloud.txt. Notice we've removed our dependency on MPI since this example doesn't use it. And C++ 14 is being used now, which removes a bug. 
+ Let's store location of our libraries in $PROOT variable with: `export $PROOT=$HOME/envs/stb_intel_13`
+ Inside the directory, configure the project with `cmake -D CMAKE_PREFIX_PATH=$PROOT .` (Notice the `.`
in the end). `CMAKE_PREFIX_PATH`is used to tell CMake where to find ArborX.
+ Build the project with `make -j8`.

  An executable called `verify`will be created.

  To test it:
  + First generate test data and store results returned by scipy. Both can be done with: `python3 GenTestDataset.py`
  + Run the CPP executable: `./verify > verify.log`
  + Make sure the results match: `python3 Verify.py`.


### Comments
+ If you ever have to leave your terminal during the process, make sure to load the modules first. 
