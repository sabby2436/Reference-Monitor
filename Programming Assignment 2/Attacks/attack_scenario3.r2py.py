# Read directly into Negative Offset Value

if "testfile.txt.a" in listfiles():
  removefile("testfile.txt.a")
if "testfile.txt.b" in listfiles():
  removefile("testfile.txt.b")

file=ABopenfile("testfile.txt",True)

try:
    file.readat(2,-2)
except RepyArgumentError:
    pass
else:
    log("Error Attack")
finally:
    exitall()

myfile.close()


