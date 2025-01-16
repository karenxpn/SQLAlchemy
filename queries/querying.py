import asyncio
from sqlalchemy import select, func
from main import async_session
from models.user import User, Role

async def get_all_users():
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        return users

users = asyncio.run(get_all_users())
print(users)

async def get_first_user():
    async with async_session() as session:
        result = await session.execute(select(User))
        user = result.scalars().first()
        return user

first_user = asyncio.run(get_first_user())
print(first_user)

async def get_john_users():
    async with async_session() as session:
        result = await session.execute(
            select(User)
            .where(User.first_name == "John")
        )
        users = result.scalars().all()
        return users

john_users = asyncio.run(get_john_users())
print(john_users)

async def get_gmail_users():
    async with async_session() as session:
        result = await session.execute(
            select(User)
            .where(User.email.like('%gmail.com'))
        )
        users = result.scalars().all()
        return users

gmail_users = asyncio.run(get_gmail_users())
print(gmail_users)

async def get_super_admin_users():
    async with async_session() as session:
        result = await session.execute(
            select(User)
            .join(User.roles)
            .where(Role.slug == 'super-admin')
        )
        users = result.scalars().all()
        return users

super_admin_users = asyncio.run(get_super_admin_users())
print(super_admin_users)

async def get_users_ordered_by_name():
    async with async_session() as session:
        result = await session.execute(
            select(User)
            .order_by(User.first_name)
            # .order_by(desc(User.first_name))
        )
        users = result.scalars().all()
        return users

users_by_name = asyncio.run(get_users_ordered_by_name())
print(users_by_name)

async def get_first_three_users():
    async with async_session() as session:
        result = await session.execute(
            select(User)
            .limit(3)
        )
        users = result.scalars().all()
        return users

first_three_users = asyncio.run(get_first_three_users())
print(first_three_users)


async def skip_three_users():
    async with async_session() as session:
        result = await session.execute(
            select(User)
            .offset(3)
        )
        users = result.scalars().all()
        return users

skip_three_users = asyncio.run(skip_three_users())
print(skip_three_users)


async def get_users_count():
    async with async_session() as session:
        result = await session.execute(
            select(func.count(User.id))
        )
        return result.scalar()

num_users = asyncio.run(get_users_count())
print(num_users)