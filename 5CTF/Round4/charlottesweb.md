charlottes web was a pcap to be looked at.

charlottes web 1
	What is the domain of the local network?  Followed the first TCP stream, found a kerberos ticket request, took the information after
	krbtgt
charlottes web 2
	What is the name of the Domain Controller? Looked through the list of packets, found a DRSUAPI, followed the TCP stream and found
	a name-pc.domain computer name
charlottes web 3
	What was the computer name of the client that got infected? The first TCP stream had a desktop name listed
charlottes web 4
	What is the sha1 hash of the downloaded executable? Used Export Objects-->HTTP, performed a Get-FileHash -Algorithm Sha1 on the file
charlottes web 5
	What IP was this downloaded from?  Looked at the hostname IP from the Export Objects
charlottes web 6
	what is the name of the malware given to it by AegisLab?  Looked up the SHA1 hash on VirusTotal, looked for AegisLab
charlottes web 7
	What is the Digicert Thumbprint of the Executable?  Under the details section in VirusTotal, X509 Signers-->DigiCert-->Thumbprint
charlottes web 8
	What is the Pastebin like domain that was contacted? Looked at one of the DNS query packets, the domain queried was the answer
charlottes web 9
	Data was being exfiltrated from the network. What Protocol was being used?  Looked at the protocol had that the largest packet
charlottes web 10
	What user account was compromised? Looked at the TCP stream for the exfiled data, and a user account is mentioned
charlottes web 11	
	what email was the exfiltrated data being sent to? Looked at the TCP stream for the exfiled data, the email to and from were the same
