#! /usr/bin/python3

import os
import subprocess
import sys

list_args = sys.argv[1]

if(list_args=='help' or list_args=='-help'or list_args=='-h'or list_args=='--help'):
	print("\nThis script will extract the number from each file name in the directory\nand then name it with the common name you gave in the arguements !")
	print("\nSo basically if you have randomly named files you wanna work with ,\nbut they have weird names ,BUT correct numbers associated , then this is the tool !")
	print("\nusage : $rPrem.py <common_name_you_wanna_use>\n")
	print("WORKS WITH PDF FILES RIGHT NOW ! CAN EASILY MODIFY FUNCTIONALITY IF NEEDED")
	sys.exit()

# print(list_args)
# cur_dir=os.system("pwd")
# os.system("whoami;cd /")
# os.system("pwd")
# print("hello "+str(cur_dir))

list_files = subprocess.run(["ls"], stdout=subprocess.PIPE,text=True)
name=(list_files.stdout)


# print("test")
# cname='234'
# for x in cname:
# 	if x.isdigit():
# 		print(x+"is a digit")

# print(type(name))

word=''
for x in name :
	if(x!='\n'):
		word+=x
	else:
		# print(word)
		digits=''
		for x in word:
			if x.isdigit():
				digits+=x

		final_name=word+' '+list_args+digits+'.pdf'
		# print(final_name)
		command="mv "+final_name
		os.system(command)
		# subprocess.run(["mv"],stdout=subprocess.PIPE,input=final_name,encoding='ascii')
		word=''