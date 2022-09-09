def main():
    philosophers_file = open('philosophers.txt','r')
    line1 = philosophers_file.readline().rstrip("\n")
    line2 = philosophers_file.readline().rstrip("\n")
    line3 = philosophers_file.readline().rstrip("\n")

    #can also use .read command instead of separate lines

    print(line1)
    print(line2)
    print(line3)

main()