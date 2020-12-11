## Attack Scenario- Creation of New File with default Backup stored as SE

if "testfile.txt.a" in listfile():
    removefile("testfile.txt.a")
if "testfile.txt.b" in listfile():
    removefile("testfile.txt.b")


file = ABopenfile("textfile.txt",True)

try:
    assert('SE'==file.readat(2,0))
    file.close()
except:
    file.close()
    