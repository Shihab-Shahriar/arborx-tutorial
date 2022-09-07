
import os
import multiprocessing


"""
module load GCC/8.3.0  CUDA/10.1.243  OpenMPI/3.1.4
module load CMake/3.17.1
module load imkl/2019.5.281
"""
os.environ['export CUDA_LAUNCH_BLOCKING']='1'
os.environ['OMP_PROC_BIND']='true'
os.environ["SFTPATH"] = os.environ['HOME'] + \
    '/envs/stb_intel_13/'

make_jobs = multiprocessing.cpu_count()//2
if make_jobs <= 0:
    make_jobs = 4
print("make_jobs: ", make_jobs)


def run(cmd):
    print(cmd)
    os.system(cmd)
    return


depwd = os.getcwd()
log = depwd+'/compile.log'
err = depwd+'/compile.err'
os.system('date >'+log)
os.system('date >'+err)


# Trilinos
os.chdir(depwd)
folder = 'build_arborx_CPU'
run('rm -rf ./{} && mkdir ./{}'.format(folder, folder))
os.chdir(folder)
run('bash ../do-cmake-cpu.sh') 
run('date')
run(f"VERBOSE=1 make -j{make_jobs} install >> {log}  2>>{err}")
run('date')
run(f"ctest -j{make_jobs}")