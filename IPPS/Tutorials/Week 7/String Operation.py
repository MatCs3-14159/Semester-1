#STRING OPERATIONS
char = chr(65)
print (char)
ascii_value = ord ('A')
print (ascii_value)

my_str = " Hello world "
upper_str =  my_str.upper()
lower_str = my_str.lower()
print (upper_str)
print (lower_str)
print(len(my_str))

str1 = "Hello"
str2 = "World"
new_word = str1 + " " + str2
print(new_word)

text = "The,quick,brown,fox,jumps,over,the,lazy,dog"
words = text.split(",")     #jaba "argument" pass gareko aauxa string bhitra ani split garne 
print (words)
print (type(words))
x = ", ".join(words)         # k bata join garne euta data structure lai
print (x)

sliced = my_str[1:11:2]
print (sliced)
reversed_my_str  = my_str[::-1]
print (reversed_my_str)

print (my_str.capitalize())
print (my_str.title())
print (my_str.strip())
print (my_str.replace("Hello", "My"))
print (my_str.find("Hello"))
print (my_str.startswith(" Hello"))
print (my_str.startswith("World "))
print (my_str.endswith(" Hello"))
print (my_str.endswith("World "))




