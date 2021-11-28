import os.path
import sqlite3 as sql


class Database:

    def DBopen(self):
        self.connection = sql.connect('numbs.sqlite3')
        self.q = self.connection.cursor()

    def DBclose(self):
        self.q.close()
        self.connection.close()

    def DBplus(self, input, output):
        self.DBopen()
        self.q.execute('''INSERT INTO `first` (`input`, `output`) VALUES (?, ?)''', (str(input), str(output)))
        self.connection.commit()
        self.DBclose()

    def __init__(self):
        if os.path.exists('numbs.sqlite3') == False:
            self.DBopen()
            self.q.execute('''CREATE TABLE `first` (`id` INT AUTO_INCREMENT, `input` INT(2), `output` INT(2), PRIMARY KEY(`id`))''')
            self.connection.commit()
            self.DBclose()
