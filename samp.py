

a=10
b=input("Enter a number")

try:
    print(a/b)

except Exception as e:
    try:
        print(b/a)
    except Exception as f:
        print("ERRor",e,f)
finally:
    print("Close")
