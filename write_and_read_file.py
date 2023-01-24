with open("my_file.txt", "w") as file:
    file.write("Hallo")    # so ist es übersichtlicher und die warscheinlichkeit die datei versehentlich zu überschreiben ist geringer,
#                            da sie nicht nur in einer loop ist sondern auch weil sie automatisch geschlossen wird.

'''my_file = open("my_file.txt", "w")

my_file.write("Hallo")
my_file.close()'''

read_file = open("my_file.txt")
for line in read_file.readlines():
    print(line)
