#读文件
"""
inputfilename=input("")
inputfile=open(inputfilename,"r")
print("opening file",inputfilename,"for reading.")
for line in inputfile:
    print(line)
inputfile.close()
print("completed",inputfilename)
"""
#常用算法
"""
伪代码
read a line from a file as a string
while(string is not empty)
process the line
read another line from the file
实现1
while True:
text=file.readline()
if not text:
break
print(text,end="")
实现2
inputfilename=input("")
inputfile=open(inputfilename,"r")
print("opening file",inputfilename,"for reading.")

line=inputfile.readline()

while(line!=""):
#readline returns""当达到最后一行
print(line)
line=inputFile.readline()
inputfile.close()
print("completed)
"""