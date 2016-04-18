from subprocess import call
from subprocess import Popen
import os

editors = ["FrameEditorEllipse"]

bat_file = 'test.bat'
with open(bat_file, 'w') as file:
    port = 5005
    file.write("start python ts_server.py -to %d" % port)
    file.write("\n")
    file.write("timeout /t 1")
    file.write("\n")
    for e in editors:
        file.write("start python block.py -from %d -to %d -editor %s" %  (port, port+1, e))
        file.write("\n")
        file.write("timeout /t 1")
        file.write("\n")
        port += 1
    file.write("start python ts_shower.py -from %d" % port)
    file.write("\n")
    #file.write("PAUSE")
    file.write("exit")
    file.write("\n")
#call(["cmd", bat_file])
os.system("start " + bat_file)
