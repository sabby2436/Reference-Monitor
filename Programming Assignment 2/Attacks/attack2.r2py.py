## Check if New File is created by setting ABopen file


if "testfile.txt.a" in listfile():
    removefile("testfile.txt.a")
if "testfile.txt.b" in listfile():
    removefile("testfile.txt.b")


try:
    file = ABopenfile("textfile.txt",False)
except FileNotFoundError:
    pss
else:
    log("ERROR Attack-7")
finally:
    exitall()

file.close()


