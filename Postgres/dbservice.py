from dbpostgrey import createTable,insertplayer,fetchplayer


print("enter 1 to create table")
print("enter 2 to insert values")
print("enter 3 to display data")
print("enter 4 to remove data")


ch = int (input("enter choice"))

if ch==1:
    createTable()
elif ch==2:
    insertplayer()
elif ch==3:
    fetchplayer()
else:
    print("invalid choice")