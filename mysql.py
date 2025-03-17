import mysql.connector as  m
mydb = m.connect(
    host="hostname",
    user="user_name",
    password="password",
    database="database_name"
)
mycursor = mydb.cursor()
mycursor.execute("select adhar_NO,vid,has_voted FROM voter")
list1=[]
list2=[]
for i in mycursor:
    list1.append(i)
for j in list1:
    for k in j:
        list2.append(k)

if '1234567890' in list2:
     ind=list2.index('1234567890')
     print(ind)
