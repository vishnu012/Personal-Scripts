#  root privileges needed                         #
#  for help sudo python3 -h                       #
#  sudo python3 scanner.py -i 127.0.0.1 -p 1-1024 #

import nmap
import argparse

def scan_host(ip_addr,port):
	scanr = nmap.PortScanner()
	scanr.scan(ip_addr,port,'-sV')
	print('---------'*4)
	print('nmap version : {}'.format(scanr.nmap_version()))
	print('---------'*4)
	print('host : {} , {}'.format(ip_addr,scanr[ip_addr].hostname()))
	print('state : {}'.format(scanr[ip_addr].state()))
	print('---------'*4)
	for proto in scanr[ip_addr].all_protocols():
		print('protocol : {}'.format(proto))
		print('---------------')
		ports = scanr[ip_addr][proto].keys()
		for port in ports:
			print('name : {} , port : {} , state : {} , version : {} , product : {} , cpe : {}'
				   .format(scanr[ip_addr][proto][port]['name'],port,scanr[ip_addr][proto][port]['state'],
				   scanr[ip_addr][proto][port]['version'],scanr[ip_addr][proto][port]['product'],
				   scanr[ip_addr][proto][port]['cpe']))
	print('--------'*12)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description ="nmap automation script")
	parser.add_argument("-i","--ip_address",required=True,help="ip address of the host ( eg - 127.0.0.1 )")
	parser.add_argument("-p","--port",required=True,help="port range ( eg - 1-1024 )")
	args = parser.parse_args()

	if args.ip_address and args.port:
		scan_host(args.ip_address,args.port)
	else:
		exit()