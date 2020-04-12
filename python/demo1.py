from io import StringIO
import pdfminer
import hashlib
from pdfminer import high_level
import sys, os

os.chdir("uploads/")
cwd = os.getcwd()
# print("current directory - "+cwd)
filepath=sys.argv[1]
# print("filepath="+filepath)
# print(sys.argv[1])
# print("in pdftohash")
writefile='out.txt'
readObj=open(filepath,'rb')
writeObj=open(writefile,'w',encoding='utf-8')
high_level.extract_text_to_fp(readObj,writeObj)
readObj.close()
writeObj.close()
fi=open("out.txt",'r', encoding="utf-8")
text=fi.read()
# print("in pdftohash")
# print(text)
fi.close()
h = hashlib.sha256(text.encode('utf-8'))
print(h.hexdigest())

# def pdfToHash(filepath):
#     print("in pdftohash")
#     writefile='uploads/out.txt'
#     readObj=open(filepath,'rb')
#     writeObj=open(writefile,'w',encoding='utf-8')
#     high_level.extract_text_to_fp(readObj,writeObj)
#     readObj.close()
#     writeObj.close()
#     fi=open("out.txt",'r', encoding="utf-8")
#     text=fi.read()
#     print(text)
#     fi.close()
#     h = hashlib.sha256(text.encode('utf-8'))
#     print("hash",h.hexdigest())
#     return h

# filepath=None
# pdfToHash(filepath)


# filename='D:\\project\\574_TDC\\blockchain\\cert\\schedule.pdf'
# file2='uploads/out.txt'
# readobj=open(filename,'rb')
# writeobj=open(file2, 'w',encoding='utf-8')
# high_level.extract_text_to_fp(readobj,writeobj)
# readobj.close()
# writeobj.close()
# fi=open("out.txt",'r', encoding="utf-8")
# text=fi.read()
# print(text)
# fi.close()

# h = hashlib.sha256(text.encode('utf-8'))
# print("hash",h.hexdigest())

# fi2=open("out.txt",'r', encoding="utf-8")
# text2=fi2.read()
# # print(text)
# fi2.close()

# h2 = hashlib.sha256(text2.encode('utf-8'))
# print("hash2",h2.hexdigest())
# print("Matches") if text==text2 else print("BUSTED")

# pdfObj=open(filename,'rb')

# pdfReader=PyPDF2.PdfFileReader(pdfObj)
# if pdfReader.isEncrypted:
#     pdfReader.decrypt("")
# pageObj=pdfReader.getPage(0)
# text=pageObj.extractText()
# pages=pdfReader.numPages
# count=0
# text=""

# while count<pages:
#     pageObj=pdfReader.getPage(count)
#     count+=1
#     text+=pageObj.extractText()
