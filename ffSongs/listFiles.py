import os
dir = '.'
ext = '.mid'
txt_files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir,f)) and f.endswith(ext)]
print(txt_files)