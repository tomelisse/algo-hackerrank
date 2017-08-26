import datetime as dt

def timeConversion(s):
    return dt.datetime.strptime(s, '%I:%M:%S%p').strftime('%H:%M:%S')
        
if __name__ == '__main__':
    s = input().strip()
    result = timeConversion(s)
    print(result)
