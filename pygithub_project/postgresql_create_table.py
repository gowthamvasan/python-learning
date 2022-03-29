import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    commands = (
        """
        CREATE TABLE commit_information (
            commit_id TEXT PRIMARY KEY,
            username VARCHAR ( 50 ) NOT NULL,
            author_name VARCHAR ( 50 ) NOT NULL,
            email VARCHAR ( 255 ) NOT NULL,
            commitMsg VARCHAR ( 255 ) NOT NULL,
            created_on TIMESTAMP NOT NULL
        );
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
