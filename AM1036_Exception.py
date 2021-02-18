import os
import time

# Python -> cmd -> Powershell
#log = input("input data : ")

"""
Add-MpPreference : 추가
Remove-MpPreference : 삭제

-ExclusionExtension : 지정된 확장명을 가진 모든 파일
-ExclusionPath : 폴더 내 모든 파일 또는 지정된 파일
-ExclusionProcess : 프로세스
"""

def AddExtension(log):
	tmp = 'powershell Add-MpPreference -ExclusionExtension "'+ log +'"'
	os.system(tmp)


def AddProcess(log):
	tmp = 'powershell Add-MpPreference -ExclusionProcess "'+ log +'"'
	os.system(tmp)

def AddPath(log):
	tmp = 'powershell Add-MpPreference -ExclusionPath "'+ log +'"'
	os.system(tmp)



def SubExtension(log):
	tmp = 'powershell Remove-MpPreference -ExclusionExtension "'+ log +'"'
	os.system(tmp)


def SubProcess(log):
	tmp = 'powershell Remove-MpPreference -ExclusionProcess "'+ log +'"'
	os.system(tmp)

def SubPath(log):
	tmp = 'powershell Remove-MpPreference -ExclusionPath "'+ log +'"'
	os.system(tmp)



def list_extension():
	command = 'powershell Get-MpPreference > /temp.ini'

	os.system(command)

	file = open('/temp.ini','rt', encoding = 'utf-8')
	line = file.readline()
	for line in file:
		if (line.find("ExclusionExtension") >= 0):
			extension = line[49:-2]


	return extension

def list_process():
	command = 'powershell Get-MpPreference > /temp.ini'

	os.system(command)

	file = open('/temp.ini','rt', encoding = 'utf-8')
	line = file.readline()
	for line in file:
		if (line.find("ExclusionProcess") >= 0):
			process = line[49:-2]

	return process


def list_path():
	command = 'powershell Get-MpPreference > /temp.ini'

	os.system(command)

	file = open('/temp.ini','rt', encoding = 'utf-8')
	line = file.readline()
	for line in file:
		if (line.find("ExclusionPath") >= 0):
			path = line[49:-2]

	return path