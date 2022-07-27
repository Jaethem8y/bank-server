import aiomysql

async def custom_query(pool,query:str):
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(query)
            return await cur.fetchall()

async def custom_query_single(pool,query:str):
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(query)
            return await cur.fetchone()
            

async def get_one_row(pool,table_name:str):
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute("SELECT * FROM " + table_name + ";")
            return await cur.fetchone()

async def get_all_rows(pool,table_name:str):
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute("SELECT * FROM " + table_name + ";")
            return await cur.fetchall()