import psycopg2
import csv
Jk = psycopg2.connect(host="localhost",user="postgres",password="123123123",port=5432,database="Phonepe-Pulse")
x = Jk.cursor()


#Inserting the Aggregated transaction details to SQL table
csv_file_path_AT = "E:\GUVI\Capstone Projects\Phonepe-Pulse\Agg_trans_dataframe.csv"
f = open(csv_file_path_AT, "r")
reader = csv.reader(f)
for row in reader:
    x.execute("INSERT INTO Aggregated_transaction(state,year,quarter,transaction_type,transaction_count,transaction_amount) VALUES (%s, %s, %s, %s, %s, %s)",row)
Jk.commit()



#Inserting the Aggregated user details to SQL table
csv_file_path_AU = "E:\GUVI\Capstone Projects\Phonepe-Pulse\Agg_user_dataframe.csv"
f = open(csv_file_path_AU, "r")
reader = csv.reader(f)
for row in reader:
    x.execute("INSERT INTO Aggregated_user(state,year,quarter,device_brands,counts,percentage) VALUES (%s, %s, %s, %s, %s, %s)",row)
Jk.commit()



#Inserting the map transaction details to SQL table
csv_file_path_MT = "E:\GUVI\Capstone Projects\Phonepe-Pulse\Map_trans_dataframe.csv"
f = open(csv_file_path_MT, "r")
reader = csv.reader(f)
for row in reader:
    x.execute("INSERT INTO Map_transactions(state,year,quarter,district,counts,amount) VALUES (%s, %s, %s, %s, %s, %s)",row)
Jk.commit()



#Inserting the map user details to SQL table
csv_file_path_MU = "E:\GUVI\Capstone Projects\Phonepe-Pulse\Map_user_dataframe.csv"
f = open(csv_file_path_MU, "r")
reader = csv.reader(f)
for row in reader:
    x.execute("INSERT INTO Map_users(state,year,quarter,district,registeredusers) VALUES (%s, %s, %s, %s, %s)",row)
Jk.commit()



#Inserting the top transaction details to SQL table
csv_file_path_TT = "E:\GUVI\Capstone Projects\Phonepe-Pulse\Top_trans_dataframe.csv"
f = open(csv_file_path_TT, "r")
reader = csv.reader(f)
for row in reader:
    x.execute("INSERT INTO Top_transactions(state,year,quarter,pincode,count,amount) VALUES (%s, %s, %s, %s, %s, %s)",row)
Jk.commit()


#Inserting the top user details to SQL table
csv_file_path_TU = "E:\GUVI\Capstone Projects\Phonepe-Pulse\Top_user_dataframe.csv"
f = open(csv_file_path_TU, "r")
reader = csv.reader(f)
for row in reader:
    x.execute("INSERT INTO Top_users(state,year,quarter,pincode,registered_user) VALUES (%s, %s, %s, %s, %s)",row)
Jk.commit()