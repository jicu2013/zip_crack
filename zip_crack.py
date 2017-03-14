import zipfile
import sys
def main():
    zipfilename=sys.argv[1]
    distfilename=sys.argv[2]
    zFile = zipfile.ZipFile(zipfilename)
    print "ziped file list:"
    print " "+str(zFile.namelist())
    fp_dist=open(distfilename,'rb')

    for line in fp_dist.readlines():
        password = line.strip('\n')
        #print password
        try:
            zFile.extractall(pwd=password)
        except Exception, e:
            #print e
            print ""
        else:
            print "[!]crack and zip file with PASSWD \"%s\""%(password)
if __name__ == "__main__":
    main()