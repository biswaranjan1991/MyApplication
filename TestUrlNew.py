import requests
import time
from beautifultable import BeautifulTable
#count = raw_input('Enter number of URLs to test:')
#print count
#timeO = raw_input('Enter threashold time in seconds:')
#print timeO
urls = ["www.google.com"]
for i in range(int(2)):
#{
        #temp = raw_input('Enter URL:')
        #print temp
        urls.append("www.google.com")
#}
j = 0
k = 0
table = BeautifulTable()
table.column_headers = ["Current Time Stamp", "Status", "URL","Response Time","Reason For Failure"]
while j < len(urls):
#{
        ts = time.time()
        try:
                response = requests.get(urls[j], timeout=float(timeO))
                response.raise_for_status()
                table.append_row([ts,response.status_code, urls[j], response.elapsed.total_seconds(), "NA"])
                j += 1
        except requests.exceptions.ConnectionError as e:
                k += 1
                print(k)
                if (k>=3):
                #{
                        #table.append_row([ts,"Connection Exception", urls[j], "0", e])
                        table.append_row([ts,"Connection Exception", urls[j], time.time() - ts, e])
                        k = 0
                        j += 1
                #}
                continue
        except requests.exceptions.Timeout as e:
                table.append_row([ts,"Timeout Exception", urls[j], "0", e])
                j += 1
                continue
        except requests.exceptions.HTTPError as e:
                table.append_row([ts,"HTTP Exception", urls[j], "0", e])
                j += 1
                continue
        except requests.exceptions.RequestException as e:
                table.append_row([ts,"Default Exception Block", urls[j], "0", e])
                j += 1
                continue
#}
print(table)

