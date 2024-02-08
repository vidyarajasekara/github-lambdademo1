import pandas as pd
# # import re
# data = """1001###101010vidya5@gmail.com
#         2002###202020dharshee01@gmail.com
#         3003###303030joshna6@gmail.com"""
# rows = data.split('\n')
# print(rows)
# employee_id = []
# emails = []
# mod_emails=[]
# phonenum = []
# ph_num = ""
# em_id = ""
# for row in rows:
#     if not row:
#         continue
#     columns = row.split("###")
#     emp_id = columns[0]
#     emp_email = columns[1]
#     employee_id.append(emp_id)
#     emails.append(emp_email)
# print(employee_id)
# print(emails)
#
# # mod_emails,ph_num
# for char in emails:
#     if char.isdigit():
#         ph_num += char
#
#     else:
#
#         rem_char = emails[len(ph_num):]
#         mod_emails.append(rem_char)
#         break
#     phonenum.append(ph_num)
# print(phonenum)
# print(mod_emails)



data = """1001###101010vidya5@gmail.com
        2002###202020dharshee01@gmail.com
        3003###303030joshna6@gmail.com"""

rows = data.split('\n')
print(rows)

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

print(employee_id)
print(phonenum)
print(mod_emails)






























# ph_num

# for char in emails:
#     if char.isdigit():
#         ph_num += char
# # for char in emails:
# #     if char.isalpha():
# #         em_id += char
# #     else:
# #         continue
# # if flag == 0:
# #     emails.append(em_id)
# # print(emails)




# df is data frame object
# df=pd.DataFrame([row.split("###") for row in rows],columns=['employee_id','email'])