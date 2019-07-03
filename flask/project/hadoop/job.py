#import os

#myCmd = os.popen('/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.1.2.jar wordcount input grep_example3').read()
#print(myCmd)

import subprocess

class HJob():

    cla='wordcount'
    arg=''
    input='input'
    output='out11'

    def __init__(self,cla='wordcount',input='/home/oussama3m/hadoop_0/data/input/',output='out2w2'):
        self.cla=cla
        self.input=input
        self.output=output

    def exec(self):
        
        MyOut = subprocess.Popen(['/usr/local/hadoop/bin/hadoop','jar','/usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.1.2.jar',self.cla,self.input,self.output],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        stdout,stderr = MyOut.communicate()
        print(stdout)
        print(stderr)
        coutput=''+self.output+'/part-r-00000'
        print("\n\n")
    
        My2Out = subprocess.Popen(['cat',coutput],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        stdout,stderr = My2Out.communicate()
        print(stderr)
        return stdout.decode("utf-8")

    def exec2(self):
        # execute
        
        exe="sudo su - vagrant -c 'hadoop jar processing2.jar Processing /user/vagrant/data/input/ /user/vagrant/"+self.output+"'"
        cat="sudo su - vagrant -c 'hadoop fs -cat /user/vagrant/"+self.output+"/*'"

        myOut = subprocess.Popen(['vagrant','ssh','gateway0','-c',exe],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        stdoutt,stderr = myOut.communicate()
        myOut = subprocess.Popen(['vagrant','ssh','gateway0','-c',cat],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        stdout,stderr = myOut.communicate()
        f=open('csvfile.csv','w')
        f.write(stdout.decode())
        f.close()
        return [stdoutt.decode(),stdout.decode()]

    def clean(self):
        c="sudo su - vagrant -c 'hadoop fs -ls /user/vagrant'"
        r="sudo su - vagrant -c 'hadoop fs -rm -r /user/vagrant/.staging /user/vagrant/cleanData /user/vagrant/prepData /user/vagrant/t*'"
        myOut = subprocess.Popen(['vagrant','ssh','gateway0','-c',r],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        stdoutt,stderr = myOut.communicate()
        myOut = subprocess.Popen(['vagrant','ssh','gateway0','-c',c],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        stdout,stderr = myOut.communicate()
        return [stdoutt.decode(),stdout.decode()]
