def main():
    philosophers_file = open('philosophers.txt', 'w')
    philosophers_file.write("John Locke" + '\n')
    philosophers_file.write("David Hume" + '\n')
    philosophers_file.write("Edmund Burke" + '\n')

    philosophers_file.close()
main()
