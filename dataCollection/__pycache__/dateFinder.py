import re
from datetime import datetime


def findDate(filename):


    match_str = re.search(r'\d{8}', filename)

    res = datetime.strptime(match_str.group(), '%Y%m%d').date()

    return(str(res))


def rgbtohex(rgb):
    return '%02x%02x%02x' % rgb