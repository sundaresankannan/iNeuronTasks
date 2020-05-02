""" Task 1, program 2"""
final=""
for i in range(2000,3201):
    if (i%7==0 and i%5!=0):
        final=final+str(i)+","
print(final[0:len(final)-1])
