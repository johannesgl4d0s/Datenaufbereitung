# Keep this file separate

def secrets():
    return {"host": "fhwn-db.postgres.database.azure.com",
            "port": 5432,
            "database": "music-store",
            "user": "student",
            "pass": "dqda-22"}


# Return a psycopg2 connection string
def psycopg2(secrets_dic):
    return ('dbname=' + secrets_dic['database'] + ' user=' + secrets_dic['user'] +
            ' password=' + secrets_dic['pass'] + ' host=' + secrets_dic['host'] +
            ' port=' + str(secrets_dic['port']))


# Return an SQLAlchemy string
def alchemy(secrets_dic):
    return ('postgresql://' + secrets_dic['user'] + ':' + secrets_dic['pass'] + '@' + secrets_dic['host'] +
            ':' + str(secrets_dic['port']) + '/' + secrets_dic['database'])
