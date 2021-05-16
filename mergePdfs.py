#! /usr/bin/python3

# import sys
# from PyPDF2 import PdfFileMerger , PdfFileReader

# if(sys.argv[1]=='-h' or sys.argv[1]=='-help' or sys.argv[1]=='help' ) :
# 	print("To merge pdf's you should supply the common-name of the pdf files and the number of pdf files you wanna combine\n and then you'll get the output there !\nExample : suppose you want to combine a1.pdf a2.pdf a3.pdf ; Use the following command : \n python3 mergePdfs a 3")
# else:
# 	name=sys.argv[1]
# 	number=sys.argv[2]
# 	print("Mergin pdfs . . .")
# 	mergedObject = PdfFileMerger()
# 	for fileN in range (1,number+1):
# 		n=str(fileN)
# 		mergedObject.append(PdfFileReader('prem'+n+'.pdf','rb'))

# 	mergedObject.write('premcombined.pdf')

import sys
from PyPDF2 import PdfFileMerger, PdfFileReader
 
if(sys.argv[1]=='-h' or sys.argv[1]=='-help' or sys.argv[1]=='help' ) :
	print("To merge pdf's you should supply the common-name of the pdf files and the number of pdf files you wanna combine\n and then you'll get the output there !\nExample : suppose you want to combine a1.pdf a2.pdf a3.pdf ; Use the following command : \n python3 mergePdfs a 3")
else: 
	name=str(sys.argv[1])
	num=int(sys.argv[2])
	# Call the PdfFileMerger
	mergedObject = PdfFileMerger()
	 
	# I had 116 files in the folder that had to be merged into a single document
	# Loop through all of them and append their pages
	for fileNumber in range(1, num+1):
	    mergedObject.append(PdfFileReader(name + str(fileNumber)+ '.pdf', 'rb'))
	 
	# Write all the files into a file which is named as shown below
	mergedObject.write(name+"_combined.pdf")