# dnsproject
Project to parse DNS logs and creating a profile for a DNS intrusion detection system

A query log file is gererated whenever there is a DNS request from the browser. The log file is genrated using the bind9 server.
The log file generated shows that every website visited makes a number of DNS requests which is huge and these requests are 
continuously generated as long as the webpage stays. So, the python code written detects DNS requests made and branch them under 
the parent DNS request made. Using this a human readable format of DNS requests was made.
The human readable format is generated in a separate report.txt file.
The query.log file should be present in the same directory as of the python code.
