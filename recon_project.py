import argparse
import sys
import whois
from datetime import datetime
import dns.resolver

parser=argparse.ArgumentParser(
description="This is python recon tool",
epilog="Use this tool for basic recon for offensive Recon and SOC",
usage='%(prog)s -d domain_name [-s IP_ADDR]'
  )
parser.suggest_on_error = True

parser.add_argument("-d","--domain",
help="Enter the domain name",
metavar="Domain",
dest="domain"
)
parser.add_argument("-s","--shodan",
help="Enter the IP address for the shodan search",
metavar="Shodan",
dest="shodan"
)
parser.add_argument("-v","-verison",
help="print version of the project",
action="version",
version='%(prog)s 1.0')

#parser.print_help()
args=parser.parse_args()
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

shodan=args.shodan
domain=args.domain
#print(f"The domain you entered is {d} and shodan IP is {s}")

try:
  w = whois.whois(domain)
  def format_date(value):
    if not value:
        return "Not Available"
    if isinstance(value, list):
        value = value[0]
    if isinstance(value, datetime):
        return value.strftime("%d %b %Y")
    return str(value)

  print("[+] Printing the WHOIS information...")
 
  print("Domain:", w.domain_name)
  print("Registrar:", w.registrar)
  print("Created:", format_date(w.creation_date))
  print("Expires:", format_date(w.expiration_date))
  print("Name Servers:", w.name_servers)
  print("Registrant Country:", w.country) 
except:
  pass

#Working for dnsresolver from dnspython tool(pip install dnspython)
print("DNS RECORD INFORMATION:")
try:
  for a in dns.resolver.resolve(domain, 'A'):
    print(f"A record:{a.to_text()}")
  for ns in dns.resolver.resolve(domain, 'NS'):
    print(f"A record:{ns.to_text()}")
  for mx in dns.resolver.resolve(domain, 'MX'):
    print(f"A record:{mx.to_text()}")
  for txt in dns.resolver.resolve(domain, 'TXT'):
    print(f"TXT record:{txt.to_text()}")
  
  
except:
  pass