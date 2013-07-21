import zipfile
import os 
class ZipCSV :
    def process_csv (self,filename):
        zfile = zipfile.ZipFile(filename)
        for name in zfile.namelist():
            (dirname, filename) = os.path.split(name)
            print "reading " + filename + " on " + dirname
            d=zfile.read(name)
            for l in d.split("\n"):
                self.process(l)
    def process_generate (self,filename,classname):
        zfile = zipfile.ZipFile(filename)
        for name in zfile.namelist():
            (dirname, filename) = os.path.split(name)
            print "reading " + filename + " on " + dirname
            d=zfile.read(name)
            for l in d.split("\n"):
                v=l.split(",")
                self.generate(v,classname)
                return
    def generate(self,v,name):
        c=0
        print "class %s:"  % name
        v2=[]
        for f in v :
            f=f.strip("\"").rstrip("\"")
            #self.fields_dict[f]=c
            print "    %s=%d" % (f,c)
            print "    def get%s(self):\n        return self.v[%s.%s]" % (f,name,f)
            c=c+1
            v2.append(f)       
        print "    fields=%s" % (v2)
