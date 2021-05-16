import os
import subprocess
import sys

larg = sys.argv[1]

# cur_dir=os.system("pwd")
# os.system("whoami;cd /")
# os.system("pwd")
# print("hello "+str(cur_dir))

list_files = subprocess.run(["ls"], stdout=subprocess.PIPE,text=True)
name=(list_files.stdout)
# print(type(name))
word=''
for x in name :
	if(x!='\n'):
		word+=x
	else:
		print(word)
		# num = ""
		# for c in inp_str:
  #   		if c.isdigit():
  #       		num = num + c
  #       final_name=str(larg[1])
  #       final_name+=num
  #       my_input=word+" "+final_name+".pdf"
  #       subprocess.run(["mv"],stdout=subprocess.PIPE,input=my_input)
		word=''	