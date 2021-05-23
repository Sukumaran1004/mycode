
class student:
    def topten(self):
        n=1
        while n<=10:
            yield n*n
            n=n+1




s1=student()
values=s1.topten()

for i in values:
    print(i)
