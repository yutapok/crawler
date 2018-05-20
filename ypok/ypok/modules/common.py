import datetime
import time
import email.utils
from urllib.parse import urlparse


def rfc2822_to_unix(rfc2822_str):
    unix = None
    if isinstance(rfc2822_str, str):
        timetuple = email.utils.parsedate_tz(rfc2822_str)
        d = datetime.datetime(*timetuple[:7])
        unix = int(time.mktime(d.timetuple()))
    
    return unix       
    
def parse_domain(url_str):
    domain = None
    if isinstance(url_str, str):
        domain = urlparse(url_str).netloc 
    
    return domain
