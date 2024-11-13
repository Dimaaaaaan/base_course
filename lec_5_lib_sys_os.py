import sys, os

print(os.getcwd())

os.system('echo саша')
#os.system("python3 /workspaces/base_course/lec_5_lib_sys_os.py")

	
print("Python version is:", sys.version)
print(sys.path)
print(sys.platform)

print(dir(sys))

print(dir(print))