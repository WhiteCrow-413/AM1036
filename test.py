import subprocess
command = 'powershell MpPreference > D:\ho\temp.ini'

#subprocess.call('powershell MpPreference', shell=True)

f=open('output.txt', 'w')
out=subprocess.check_output('powershell MpPreference', shell=True, encoding='utf-8')
f.write(out)
f.close()

file = open('output.txt','rt', encoding = 'utf-8')
line = file.readline()
for line in file:
	if (line.find("ExclusionProcess") >= 0):
		print(line[49:-2])