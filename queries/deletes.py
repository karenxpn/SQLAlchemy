import asyncio

from sqlalchemy import select

from main import async_session
from models.user import User

async def delete_first_user():
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(User).order_by(User.id))
            first_user = result.scalars().first()

            if first_user:
                await session.delete(first_user)
            else:
                print('No user found')


asyncio.run(delete_first_user())