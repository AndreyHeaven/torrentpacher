from time import sleep
import urllib
import subprocess
import sys
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="araygorodskiy"
__date__ ="$04.02.2009 17:56:17$"
def download_tracker_ini():
    file = urllib.urlopen("http://re-tracker.ru/trackerssimple.ini",proxies=None);
    file2 = open("trackerssimple.ini","w")
    file2.write(file.read());
    try:
        retcode = subprocess.call("iconv"+" -f UTF16LE -t UTF8 trackerssimple.ini -o trackerssimple-utf8.ini",shell=True);
        if retcode < 0:
            print >>sys.stderr, "Child was terminated by signal", -retcode
        else:
            print >>sys.stderr, "Child returned", retcode
    except OSError, e:
        print >>sys.stderr, "Execution failed:", e
#    p = subprocess.Popen("iconv -f UTF16LE -t UTF8 trackerssimple.ini", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=True)
#    (child_stdin, child_stdout) = (p.stdin, p.stdout)
#    i = os.system("iconv -f UTF16LE -t UTF8 trackerssimple.ini -o trackerssimple-utf8.ini");
#    print i
    sleep(10)
    file3 = open("trackerssimple-utf8.ini","r");
    print file3.read();
#    print(child_stdout.read())
    pass;
if __name__ == "__main__":
#    print sys.byteorder
    download_tracker_ini();
