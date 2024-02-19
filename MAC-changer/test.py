# #!/usr/bin/env python3
import subprocess

dir_path = f'dir C:\\Users\\IGS\\Desktop'
do_dir_path = subprocess.Popen(dir_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
do_dir_path_out, do_dir_path_err = do_dir_path.communicate()
if do_dir_path.returncode == 0:
    print(f'\n')
    print(f'{do_dir_path_out}')
    print(f'\n')
else:
    print(f'\n')
    print(f'{do_dir_path_err}')
    print(f'\n')
