from Model.request_sql import requestSQL

sql = requestSQL()

res = sql.execute('''select * from "user" where login_name = 'lj-biao-yin' ''')
print(res)
res = sql.execute('''select * from "user" where "id" in('232','210','139','351','133','315','20','198','274')''')
for re in  res:
    print(re[1])





