import requests

url = "https://www.zillow.com/homes/for_rent/18025_rid/2-_beds/1200-1700_mp/X1-SSo3jl0uztxfae1000000000_a3t9l_sse/"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
r = requests.get(url, headers=header)

print(r)
