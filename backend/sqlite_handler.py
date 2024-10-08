from sqlite3 import connect, Row

from config import config


DB_PATH = config["database_path"]


class SQLiteHandler:
    """
    how to connect to sqlite database:

    # # #
    with SQLiteHandler(path) as cur:
        # cur.execute(command)
        ...
    # # #

    will commit and close the connection automatically
    """
    def __init__(self, file=DB_PATH):
        self.file = file

    def __enter__(self):
        self.conn = connect(self.file)
        self.conn.row_factory = Row
        return self.conn.cursor()

    def __exit__(self, err_type, value, traceback):
        self.conn.commit()
        self.conn.close()
