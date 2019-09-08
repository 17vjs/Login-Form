import csv
filename = "./data/user_master.csv"
fields = []
rows = []


def read_csv(username, password):
    with open(filename, 'r') as csvfile:
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
