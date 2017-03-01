#!/usr/bin/env python
# -*- coding: utf-8 -*-

device_name="28-05167057deff"


def main():
	#while True:
	node = open("/sys/bus/w5/devices/"+device_name+"/w2_slave")
	text = node.read();
	print text.split("\n")[1]

def parse_info(info):
	line = info.split("\n")[1]
	temp = line.split(" ")[-1]
	return float(temp.split("=")[1])/1000.0
		

if __name__ == "__main__":
	node = open("/sys/bus/w1/devices/"+device_name+"/w1_slave")
	text = node.read();
	print parse_info(text)
	
		


