from array import array
from netaddr import *

def subnet_calculator():
    class_A = ('10.0.0.1')
    class_B = ('172.16.0.1')
    class_C = ('192.168.0.1')


    print ("CLASS A = 10.0.0.1")
    print ("CLASS B = 172.16.0.1")
    print ("CLASS C = 192.168.0.1")
    print ("---------------------")
    user_input_1 = raw_input("Select a Class: ")
    hostsPerSubnet = int(raw_input("How many Hosts per subnet: "))
    user_input_2 = raw_input(("Enter starting IP address: "))
    Intarr=array('f',[])


