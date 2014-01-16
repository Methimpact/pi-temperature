#!/usr/bin/python
import os
import sys

ww = open("temp2.log", 'w')
ww.writelines(sys.argv)
ww.close()

readFile = open("/home/pi/temperature.dat")
readFilej = open("/home/pi/hours24.dat")


lines = readFile.readlines()
linesj = readFilej.readlines()


readFile.close()
readFilej.close()


w = open("/home/pi/temperature.dat",'w')
wj = open("/home/pi/hours24.dat",'w')
#wa = open("/home/pi/jennyall.dat",'a')

if(len(sys.argv)<6):
    w.writelines(sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+' '+sys.argv[4]+' 0 \n')
    wj.writelines(sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+' '+sys.argv[4]+' 0 \n')
 #   wa.writelines(sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+' '+sys.argv[4]+' 0 \n')
else:
    w.writelines(sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+' '+sys.argv[4]+' '+sys.argv[5]+'\n')
    wj.writelines(sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+' '+sys.argv[4]+' '+sys.argv[5]+'\n')
  #  wa.writelines(sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+' '+sys.argv[4]+' '+sys.argv[5]+'\n')

w.writelines([item for item in lines[:-1]])
wj.writelines([item for item in linesj[:-1]])
#wa.writelines([item for item in linesja[:-1]])
# should have 2160 lines... for i in `seq 1 2160`; do echo "0 0 0 0 0" >> temperature2.dat; done
#Should have 8640 lines:  for i in `seq 1 8640`; do echo "0 0 0 0 0" >> jenny2.dat; done

w.close()
wj.close()

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)
#f.write('Temperature: '+sys.argv[1]+' at time: '+sys.argv[2]+' '+sys.argv[3]+'\n')
