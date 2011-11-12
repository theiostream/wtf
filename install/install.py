#!/usr/bin/env python

import os
import shutil
from subprocess import check_output

for e in check_output('echo $PATH', shell=True).rstrip('\n').split(':'):
	if os.path.exists(e+'/wtf'):
		shutil.move(e+'/wtf', e+'/wtf-old')

if not os.path.exists('/Library/wtf/'):
	os.makedirs('/Library/wtf')

# Update the adbs
if os.path.exists('/Library/wtf/lists'):
	shutil.rmtree('/Library/wtf/lists')

shutil.copytree('../adb', '/Library/wtf/lists')

os.chmod('../wtf', 0755)	
shutil.copy('../wtf', '/usr/bin/')

print '[wtf installer] Done!'