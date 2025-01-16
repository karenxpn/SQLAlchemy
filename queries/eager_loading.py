import asyncio

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from main import async_session
from models.user import User

async def get_users():
    async with async_session() as session:
        result = await session.execute(
            select(User)
            .options(joinedload(User.addresses))
        )
        return result.scalars().unique().all()

users = asyncio.run(get_users())
for user in users:
    print(user.addresses)

