#!/usr/bin/python

#from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import * 
from time import gmtime, sleep, strftime
from datetime import datetime
import os
import glob
import time


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'

device_folder = glob.glob(base_dir + '28*')[0]
device_folder2 = glob.glob(base_dir + '28*')[1]
device_file = device_folder + '/w1_slave'
device_file2 = device_folder2 + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r') 
    lines = f.readlines()
    f.close()
    return lines

def read_temp_raw2():
    f2 = open(device_file2, 'r')
    lines2 = f2.readlines()
    f2.close()
    return lines2


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f

def read_temp2():
    lines2 = read_temp_raw2() 
    while lines2[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines2 = read_temp_raw2()
    equals_pos2 = lines2[1].find('t=')
    if equals_pos2 != -1:
        temp_string2 = lines2[1][equals_pos2+2:]
        temp_c2 = float(temp_string2) / 1000.0
        temp_f2 = temp_c2 * 9.0 / 5.0 + 32.0
        return temp_f2


cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
cmd2 = "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1"

def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

flag = 0
while 1:
	ipaddr = run_cmd(cmd)
        if(ipaddr == ''):
		ipaddr = run_cmd(cmd2)

        rcmd = "ssh pi@wigner.physics.drexel.edu \'/home/pi/protemp.py "+str(read_temp())+" "+datetime.now().strftime("%Y-%m-%d")+" "+datetime.now().strftime("%H:%M")+" " +ipaddr+" "+str(read_temp2())+"\'"

       

        os.system(rcmd)
	sleep(10)
      
