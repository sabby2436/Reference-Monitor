# Check if valid data is appended

if "testfile.txt.a" in listfiles():
  removefile("testfile.txt.a")
if "testfile.txt.b" in listfiles():
  removefile("testfile.txt.b")

file=ABopenfile("testfile.txt",True)

file.writeat("Sabarni",0)
file.close()

file = ABopenfile("testfile.txt",True)
file.writeat("KunduE",0)
file.close()

file = ABopenfile("testfile.txt",True)

try:
    assert('SabarniKunduE'== file.readat(None,0))
    file.close()
except:
    file.close()
    log("Error Attack")
finally:
    exitall()
    
