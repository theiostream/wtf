#!/usr/bin/env python

import os
import shutil
from subprocess import check_output

for e in check_output('echo $PATH', shell=True).rstrip('\n').split(':'):
	if os.path.exists(e+'/wtf'):
		shutil.move(e+'/wtf', e+'/wtf-old')

if not os.path.exists('/Library/wtf/'):
	shutil.copytree('./wtf', '/Library/wtf')

os.chmod('../wtf', 0755)	
shutil.copy('../wtf', '/usr/bin/')

print '[wtf installer] Done!'