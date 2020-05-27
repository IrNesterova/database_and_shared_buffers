import os
import sys

service_directory = os.path.dirname(__file__)
source_directory = os.path.abspath(service_directory)
os.chdir(source_directory)
venv_base = os.path.abspath(os.path.join(source_directory, "..", "..", "venv"))
sys.path.append(".")
old_os_path = os.environ['PATH']
os.environ['PATH'] = os.path.join(venv_base, "Scripts")+ os.pathsep + old_os_path
site_packages = os.path.join(venv_base, "Lib", "site-packages")
prev_sys_path = list(sys.path)
import site
site.addsitedir(site_packages)
sys.real_prefix = sys.prefix
sys.prefix = venv_base
new_sys_path = list()
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path