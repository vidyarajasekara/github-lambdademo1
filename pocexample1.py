import pandas as pd
from sqlalchemy import create_engine
import pymysql
data = """1001###101010vidya5@gmail.com
        2002###202020dharshee01@gmail.com
        3003###303030joshna6@gmail.com"""

rows = data.split('\n')
print("Given Employee Data as a list :",rows)

employee_id = []
mod_emails = []
phonenum = []

for row in rows:
    if not row.strip():  # Use strip to remove leading/trailing whitespaces
        continue
    columns = row.split("###")
    emp_id = columns[0].strip()
    emp_email = columns[1].strip()
    employee_id.append(emp_id)

    # Extract phone number
    ph_num = ''.join(filter(str.isdigit, emp_email))[:6]
    phonenum.append(ph_num)

    # Extract modified email
    mod_email = emp_email[len(ph_num):]
    mod_emails.append(mod_email)

print("Employee id list:",employee_id)
print("PhoneNo list :",phonenum)
print("Email list is:",mod_emails)

# Create a DataFrame
df = pd.DataFrame({'Employee_ID': employee_id, 'Phone_Number': phonenum, 'Email': mod_emails})

# Display the DataFrame
print(df)
#
# # MySQL database connection parameters
# db_user = 'root'
# db_password = 'root'
# db_host = 'localhost'
# db_port = '3306'
# db_name = 'vidya_1'
#
# # Create a SQLAlchemy engine
# engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
#
# # Insert the DataFrame into a MySQL table called 'your_table_name'
# table_name = 'employeetable'
# df.to_sql(table_name, con=engine, if_exists='replace', index=False)
#
# # read the data from the db
# query = f'select * from {table_name}'
# df_from_db=pd.read_sql(query,con=engine)
#
# print("dataframe from mysql")
# print(df_from_db)
#
#
# # Close the database connection
# engine.dispose()




























