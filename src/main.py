from time import gmtime, strftime

def main():
    with open("asd.txt","a") as pout:
        pout.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+"\n")

if __name__ == "__main__":
    main()
