# Using only one website for demo
# Uncomment below 'urls' to fetch more IP proxies

urls = ["https://free-proxy-list.net"]


"""
urls = ["https://free-proxy-list.net","https://free-proxy-list.net/uk-proxy.html",
    "https://www.us-proxy.org","https://www.sslproxies.org","https://premproxy.com/list",
    "http://nntime.com/","https://hidemy.name/en/proxy-list/","http://free-proxy.cz",
    "https://hidester.com/proxylist/","https://nordvpn.com/free-proxy-list/",
    "https://www.hide-my-ip.com/proxylist.shtml","http://www.httptunnel.ge/ProxyListForFree.aspx"]
"""


"""
Data configurations below - to have ease while scraping
Can easily modify here, if the configuration for a website changes
"""

# ID used for proxy table
id_tags_name = ["proxylisttable", "proxylisttable", "proxylisttable", "proxylisttable", "proxylist", "proxylist",
                "", "proxy_list", "", "", "sort-list", "ctl00_ContentPlaceHolder1_GridViewNEW"]

# Class name used for proxy table
class_name = ["", "", "", "", "", "", "proxy__t", "", "table table-hover",
                "table table-bordered table-hover table-hover proxy-list-table", "", ""]


""" 
Given below is the sequence for above websites, in which following columns will be displayed.
Note: 20 is an exception
        It's used to differentiate data written in different format on the website. 
        Hence, it'll be handled differently by scraper.py
"""

ip_seq = [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1] # IP Address
port_seq = [1, 1, 1, 1, 20, 20, 1, 1, 2, 2, 1, 20, 2, 2, 2] # Port number
country_seq = [3, 3, 3, 3, 3, 4, 2, 3, 3, 0, 2, 20, 4, 4, 4] # Country name
anon_seq = [4, 4, 4, 4, 1, 2, 5, 6, 7, 20, 5, 20, 3, 3, 5] # anonymity level
https_seq = [6, 6, 6, 6, 20, 20, 4, 2, 4, 3, 4, 20, 6, 6, 6] # HTTP or HTTPS
pages = [15, 5, 10, 5, 20, 18, 36, 9, 5, 15, 18, 1, 2, 6, 2] # number of pages
