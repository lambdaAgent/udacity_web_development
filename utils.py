def escape_html(s):
    s = re.sub(r'(&)',"&amp;" ,s)
    s = re.sub(r'(<)',"&lt;" ,s)
    s = re.sub(r'(>)',"&gt;" ,s)
    s = re.sub(r'(")',"&quot;" ,s)
    return s

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
    try:
        months.index(month.title())
        return  month.title()
    except:
        return None

def valid_day(day):
    try:
        if day.isdigit():
            if int(day) > 0 and int(day) <= 31:
                return int(day)
            else:
                raise Exception("out of range")
        else:
            raise Exception("Not a digit")
    except:
        return None

def valid_year(year):
    try:
        if int(year) >= 1920 and int(year) <= 2020:
            return int(year)
    except:
        return None