import psycopg2 as ps
db="Testing2"
dbuser = "postgres"
dbhost ="localhost"
dbpassword="3108"
portno=5432


conn = ps.connect(
    database=db,
    user=dbuser,
    host=dbhost,
    password=dbpassword,
    port=portno
)

cur=conn.cursor()


def createTable():
    query="create table player(pid int,pname varchar)"
    cur.execute(query)
    conn.commit()

def insertplayer():
    pid=int(input("enter player id"))
    pname=input("enter the player name")
    query=f"insert into player values({pid},'{pname})"
    cur.execute(query)
    conn.commit()
    conn.close()

def fetchplayer():
    query="select * from player"
    cur.execute(query)
    rows=cur.fetchall()
    print(rows)


if(conn!=None):
    print ("connection done")
else:
    print("connection failed")