import sqlite3
import os

class DB:

    def __init__(self) -> None:
        self.connection = None
        self.create_connection()
    def create_connection(self):
        self.connection = sqlite3.connect(self.set_full_path('./posts.db'))

    def set_full_path(self, filename):
        script_dir = os.path.dirname(__file__)
        return os.path.join(script_dir, "../db/"+filename)

    def sample_data(self):
        cur = self.connection.cursor()
        # Create table
        # cur.execute('''CREATE TABLE posts
        #             (id INTEGER PRIMARY KEY AUTOINCREMENT,
        #             posted BOOLEAN, 
        #             image_path VARCHAR,
        #             caption VARCHAR,
        #             ig_users VARCHAR)''')
        cur.execute("INSERT INTO posts VALUES(null,false, '/home/odin/Pictures/Email.png', 'Example Caption', 'rosalia,some,two,three')")
        self.connection.commit()

    def get_posts_all_posts(self):
        cur = self.connection.cursor()
        result = cur.execute("SELECT rowid, posted, image_path, caption, ig_users FROM posts")
        posts = []
        for row in result:
            post = {'path' : row[1], 'caption': row[2], 'users' : row[3]}
            posts.append(post)
        self.connection.commit()
        return posts

    def get_unpublished_posts(self):
        cur = self.connection.cursor()
        result = cur.execute("SELECT id,image_path,caption,ig_users FROM posts where posted=false")
        posts = []
        for row in result:
            post = {'id' : row[0], 'path' : row[1], 'caption': row[2], 'users' : (row[3].split(','))}
            posts.append(post)
        self.connection.commit()
        return posts

    def update_post_as_published(self, id):
        cur = self.connection.cursor()
        cur.execute("UPDATE posts SET posted=1 where id="+str(id))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()