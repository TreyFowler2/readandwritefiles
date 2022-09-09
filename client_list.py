def main():
    infile = open('clients.txt', 'r')

    number = 1
    for line in infile:
        text = line.rstrip("\n")
        print(number, '. ', text, sep="")
        #turn number into a string inside the parenthesis. print(str(number) + '.', text) 
        number += 1

    
main()