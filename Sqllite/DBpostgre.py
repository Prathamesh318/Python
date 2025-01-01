import psycopg2 as ps

db="Testing2"
dbuser="postgres"
dbhost="localhost"
dbpassword="3108"
portno=5432

conn=ps.connect(
    database=db,
    user=dbuser,
    host=dbhost,
    password=dbpassword,
    port=portno
)

cur=conn.cursor()