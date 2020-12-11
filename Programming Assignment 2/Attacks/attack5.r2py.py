def close(time):
    def sleep():
        sleep(time)
        log("Invalid Operation")
        exitall()
    return sleep
    terminate = close(10)
    createthread(terminate)



if "testfile.txt.a" in listfiles():
  removefile("testfile.txt.a")
if "testfile.txt.b" in listfiles():
  removefile("testfile.txt.b")

file=ABopenfile("testfile.txt",True)

try:
    file.writeat("abc"* 1000)

file.close()

file = ABopenfile("testfile.txt",True)

try:
    file.readat(None,0)
except:
    log("Error Attack")
finally:
    exitall()

    