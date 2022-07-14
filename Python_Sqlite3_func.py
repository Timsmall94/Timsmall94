import sqlite3
conn=sqlite3.connect("testing.db")
c = conn.cursor()

#how to check table column
#c.execute("select * from pragma_table_info('info') as tblInfo")
#fetch=c.fetchall()
#for fit in fetch:
#	print(fit)
#conn.commit
#conn.close

#c.execute ("""CREATE TABLE info(
#first_name text, 
# last_ name text,	
# age integer,	
#phoneNumber text CHECK(phoneNumber GLOB '06[1-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),	
# email text UNIQUE)""")
#	
#conn.commit()
#conn.close()
#print("table successfly created")


#item =c.fetchall()
#for items in item:
#	print(items)

#conn.commit()
#conn.close
#my_info=[
#('seun', 'ayobami', 23, '0620987654','seun@ayobami.com'),
#('adeeko', 'oluwatobi', 25, '0634567890', 'adeeko@oluwatobi.com'),
#('adura', 'gbemi', 27, '0632124567','adura@gbemi.com'),
#('fimi', 'sile', 27, '0649871234', 'fimi@sile.com'),
#('tami', 'joor',28, '0659871234','tami@joor.com'),
#('epo', 'ora', 20, '0661244567','epo@ora.com'),
#('oniyi','nuru', 24,'0678902324','niy8i@nuru.com')
#]
#

#selecting all item from db quering
def select_all():
	c.execute("select rowid, * from info")
	items =c.fetchall()
	for item in items:
		print(item)
	conn.commit()
	conn.close()

#function to select many
def select_many(id):
	c.execute("select rowid, * from info",)
	one=c.fetchmany(id)
	print (one)
	conn.commit()
	conn.close()


#function to add one
def add_one(firstname, lastname, age, phoneNumber, email ):
	c.execute("insert into info values(?,?,?,?,?)",(firstname, lastname, age, phoneNumber,email))
	print("data Added successfully")
	conn.commit()
	conn.close()

#function to add many	
def add_many(many):
	c.executemany("insert into info values (?,?,?,?,?)", many)
	conn.commit()
	conn.close()

#function to select by rowid
def select_id(id):
	c.execute("select rowid,* from info WHERE rowid=(?)", (id,))
	items =c.fetchall()
	if items:
		print(items)
	else:
		print(f"user with id {id} does not exist ")
	conn.commit()
	conn.close()

#function to select firstname
def select_firstname(name):
#name=input("type the name you want to search")
	c.execute("select rowid,* from info WHERE first_name=?", (name,))
	items =c.fetchall()
	for item in items:
		print(item)
	conn.commit()
	conn.close()
	
#function to select lastname
def select_lastname(name):
	#name=input("type the name you want to search")
	c.execute("select rowid,* from info WHERE last_=?", (name,))
	items =c.fetchall()
	for item in items:
		print(item)
	conn.commit()
	conn.close()

#function to select by age
def select_age(age):
	c.execute("select rowid,* from info WHERE age=(?)", (age,))
	items =c.fetchall()
	if items:
		for item in items:
			print(item)
	else:
		print(f"user with age {age} doesn't Exist")
	
	conn.commit()
	conn.close()

#selecting a phone	
def select_phoneNumber(num):
	c.execute("select rowid, * from info Where phoneNumber=? ",(num,))
	items =c.fetchall()
	for item in items:
			print(item)
	conn.commit()
	conn.close()	

#selecting all the phone number
def select_all_number( ):
	c.execute("select rowid, phoneNumber  from info")
	exist=c.fetchall()
	print("PhoneNumbers")
	for item in exist:
		print (item)
	conn.commit()
	conn.close()

#searching for a single  email
def select_email(mail):
	c.execute("select rowid, * from info where email=?",(mail,))
	conn.commit()
	exist= c.fetchall()
	if exist:
		print(exist)
	else:
		print("user don't exist")

#query to update info in the DB
def update_age(age, id):
	c.execute("update info SET age=? WHERE rowid = ?", (age, id,))
	conn.commit()
	new_id = c.fetchall()
	if new_id:
		print(new_id)
	else:
		print(f"The user with id{id} not Found!!")

#updating many info the DB infomation 
def update_age_many(many):
	c.executemany("update info SET age=? WHERE rowid = ?", many)
	conn.commit()
	new_id = c.fetchall()
	if new_id:
		print("data updated succefully")
	else:
		print(f"The user with id{id} not Found!!")

#updating names in the db
def update_name(fname, lname, id):
	c.execute("update info SET first_name=?, last_=? WHERE rowid = ?", (fname, lname, id,))
	new = c.fetchone()
	conn.commit()
	if new:
		print(new)
	else:
		print(f"The user with id {id} not Found!!!")
		conn.close()
	
#deleting a record
def  delete_record(id):
	c.execute("Delete from info where id =?",id)
	print (f"The details with id {id} is succefully Deleted")
	conn.commit
	conn.close