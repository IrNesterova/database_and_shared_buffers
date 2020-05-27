# coding=utf-8
import psycopg2
from psycopg2.extras import DictCursor


class Worker():
    def __init__(self, database="postgres", user="postgres", password="qwerty007", host="localhost", port="5432"):
        self.conn = psycopg2.connect(database=database, user=user,
                                     password=password, host=host, port=port)
        self.conn.autocommit = True
        with self.conn:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("create extension if not exists pg_buffercache;")

    def execCurrentBuffer(self):
        val = ""
        with self.conn:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("begin;")
                cur.execute("SELECT pg_size_pretty(current_setting('block_size')::int * count(*) FILTER (WHERE usagecount > 4)) \"usagecount > 4\" FROM pg_buffercache;")
                val = cur.fetchall()
                cur.execute("end;")
        
        return val
    def execLowBuffer(self):
        val = ""
        with self.conn:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT pg_size_pretty(current_setting('block_size')::int * count(*) FILTER (WHERE usagecount = 1)) \"usagecount = 1\" FROM pg_buffercache;")
                val = cur.fetchall()
        
        return val
    def execBuffer(self):
        val = ""
        with self.conn:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("show shared_buffers;")
                val = cur.fetchall()

        
        return val

    def execAlterSystem(self):
        with self.conn:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("ALTER SYSTEM set shared_buffers TO '2048MB';")

    def end(self):
        self.conn.close()
# Шумные запросы мешают других, перетягивают внимание на себя, мешают серверу