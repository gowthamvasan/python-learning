import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    commands = (
        """
        INSERT INTO commit_information (commit_id, username, author_name, email, created_on)
        VALUES('30e2c363d974c7e0d994aee3b4addd0329738uytr','gowthamvasan', 'Giri', 'gowtham@gmail.com','2018-03-30 07:34:27');
        """,
    )
    try:
        # read connection parameters
        params = config()
        # print(params)

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        for command in commands:
            print(command)
            cur.execute(command)

        # display the PostgreSQL database server version
        # output = cur.fetchone()
        # print(output)
       
	# close the communication with the PostgreSQL
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
