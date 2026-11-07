
def decdnded(mylist):
    print(sorted(mylist))


def acdnded(mylist):
    print(sorted(mylist, reverse=True))

def mysort(f,mylist):
    f(mylist)

mylist = input("لیست اعداد رو وارد کنید. \n")
mylist_1 = mylist.split(",")
print(mylist_1)

choice = input("چگونه مرتبسازی شود ؟ صعودی '1' یا نزولی '2'\t")

if choice == "1":
    mysort(decdnded, mylist_1)

elif choice == "2":
    mysort(acdnded, mylist_1)

else:
    print("لطفا تنها از گزینه های موجود انتخاب کنید .")