import csv
user_master_csv = "./data/user_master.csv"
stores_csv = "./data/stores.csv"


def read_stores_csv():
    rows = []
    with open(stores_csv, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
    stores = []
    for i in range(1, len(rows)):
        stores.append({
            rows[0][0]: rows[i][0],
            rows[0][1]: rows[i][1],
            rows[0][2]: rows[i][2],
            rows[0][3]: rows[i][3],

        })
    return {"stores": stores}


def read_user_master_csv(username, password):
    rows = []
    with open(user_master_csv, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
    u = rows[0].index('username')
    p = rows[0].index('password')
    r = rows[0].index('role')
    for row in rows:
        if row[u] == username and row[p] == password:
            return [True, {"role": row[r]}]
    else:
        return [False, {"role": "unknown"}]
