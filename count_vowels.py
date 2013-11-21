vowels = 'aeiouAEIOU'
count = 0
string = open('openfile.txt')
resume = string.read()
for i in resume:
   if i in vowels:
       count += 1
   print count
