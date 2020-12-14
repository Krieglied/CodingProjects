Pursuit was a pcap to be looked at

Pursuit 1
	What is the source IP address?  Literally the source IP of the first packet
Pursuit 2
	What is the destination IP address?  Literally the destination IP of the first packet
Pursuit 3
	How many hops does it take to get a reply from the destination IP? Looking at the ttl of the packet that doesn't get a 
	time-to-live exceeded error returned
Pursuit 4
	What is the MAC address of the source? Literally the source MAC of the first packet
Pursuit 5
	Where is the company that made the the source headquartered? (country)  First a lookup on a OUI table, and then a google 
	search on the company
Pursuit 6
	In which packet number do we get the first reply from the destination IP?  The first Echo ping reply packet
Pursuit 7
	What was the response time?  Looked at the Response time section of ICMP for the packet
Pursuit 8
	What is the IP address of the 5th router in the path? Looked at the router after the packet with ttl=5 was sent
