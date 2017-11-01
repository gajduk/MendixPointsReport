from time import strftime,gmtime

def log(msg,error=False):
    separator = "!!ERROR!! : "
    if not error:
        separator = ":"
    print strftime("%Y-%m-%d %H:%M:%S", gmtime()),separator,msg
