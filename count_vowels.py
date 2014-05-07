#resume = open('webdeveloper.txt')
#print resume.read()


vowels = 'aeiouAEIOU'
count = 0
string = open('webdeveloper.txt')
resume = string.read()
for i in resume:
   if i in vowels:
       count += 1
   print count

#print string

#def find_vowels(resume):

#    count = 0
 #vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
   # vowels = "aeiouAEIOU"
   # for letter in resume:
       # if letter in vowels:
           # count + 1
       # print count

