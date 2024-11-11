import mysql.connector


def mysqlConnection():
    ## create connection
    cnn = mysql.connector.connect(user = 'root' , host = 'localhost' , database = 'proj_grocery_store')

    try :
        if cnn :
            return cnn
    except Exception as e:
        print(e)


