import psycopg2,csv
from config import config

csv_file='/Users/user/Documents/Git_repos/Personal/python-learning/pygithub_project/project_dataset.csv'

def insert_commit_status(dataset):
    """ Connect to the PostgreSQL database server """
    conn = None
    command = """ INSERT INTO commit_information VALUES(%s,%s,%s,%s,%s); """
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
        print('Inserting data into the table:', dataset)
        cur.execute(command,dataset)
       
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
    with open(csv_file, 'r') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        for row in csvreader:
            insert_commit_status(row)
