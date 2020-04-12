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


