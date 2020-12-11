#Check if invalid data is discarded and value is retained

if "testfile.txt.a" in listfiles():
  removefile("testfile.txt.a")
if "testfile.txt.b" in listfiles():
  removefile("testfile.txt.b")

file=ABopenfile("testfile.txt",True)
file.writeat("Sabarni",0)
 file.close()

 #Read
file=ABopenfile("testfile.txt",True)
try:
    assert('SE'== myfile.readat(2,0))
    file.close()
except:
    file.close()
    log("Error Attack")
finally:
    exitall()
