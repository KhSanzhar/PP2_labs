import os 
print('Exist:', os.access('C:\\Users\Sanzhik\Desktop\2sempy\lab6', os.F_OK)) 
print('Readable:', os.access('C:\\Users\Sanzhik\Desktop\2sempy\lab6', os.R_OK)) 
print('Writable:', os.access('C:\\Users\Sanzhik\Desktop\2sempy\lab6', os.W_OK)) 
print('Executable:', os.access('C:\\Users\Sanzhik\Desktop\2sempy\lab6', os.X_OK))