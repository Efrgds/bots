import sqlite3 as sq


class Database:
    def __init__(self):
        self.connection = None
        self.create_users()
        self.create_connection()

    async def create_connection(self):
        self.connection = await sq.connect('../../data.db')


async def create_users(self, user_id: int):
    if self.connection is None:
        await self.create_connection()
    async with self.connection.execute("INSERT INTO users VALUES (?, ?, ?)", (user_id, 'user_name', 'user_ticket')):
        await self.connection.commit


async def add_question(self, user_id: int, question: str):
    # question = cur.execute("SELECT 1 FROM questions WHERE user_id = '{key}'".format(key=user_id)).fetchone()
    if self.connection is None:
        await self.create_connection()
    async with self.connection.execute("INSERT INTO questions VALUES (user_id, question)", (user_id, question)):
        await self.connection.commit()


async def get_unanswered_questions(self):
    if self.connection is None:
        await self.create_connection()
    async with self.connection.execute("SELECT * FROM questions WHERE answer IS NULL") as cur:
        rows = await cur.fetchall()
        return rows


async def update_questions_id(self, question_id: int, answer: str):
    async with self.connection.execute('UPDATE questions SET answer = ? WHERE id = ?', (answer, question_id)):
        await self.connection.commit


async def get_question(self, question_id: int):
    async with self.connection.execute('SELECT user_id, question, answer FROM questions WHERE id = ?',
                                       (question_id,)) as cur:
        row = await cur.fetchone()
        if row is not None:
            user_id, question, answer = row
            return {'user_id': user_id, 'question': question, 'answer': answer}
        else:
            return None


async def delete_question(self, question_id: int):
    async with self.connection.execute('DELETE FROM questions WHERE id = ?', (question_id,)):
        await self.connection.execute("DELETE FROM sqlite_sequens WHERE name='questions'")
        await self.connection.commit()


async def edit_questions(state, user_id):
    pass

# async with state.proxy() as data:
#     cur.execute("UPDATE users SET user_name = '{}', user_ticket = '{}' WHERE user_id == '{}'".format(data['user_name'],
#                                                                                              data[
#                                                                                                  'user_ticket', user_id]))
#     db.commit()
