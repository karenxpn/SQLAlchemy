import asyncio

from sqlalchemy import select

from main import async_session
from models.user import User, Role, Address, Preference

async def get_admin():
    async with async_session() as session:
        result =  await session.execute(
            select(Role).where(Role.slug == "admin")
        )
        return result.scalars().first()



admin_role = asyncio.run(get_admin())
print(admin_role)


async def create_users():
    async with async_session() as session:
        user = User(
            first_name="John",
            last_name="Smith",
            email='johnsmith@gmail.com'
        )
        session.add(user)

        user2 = User()
        user2.first_name = "Jane"
        user2.last_name = "Doe"
        user2.email = 'janedoe@gmail.com'

        session.add(user2)

        user3 = User(
            first_name="Jay",
            last_name="Jones",
            email='jayJones@gmail.com'
        )

        user3.roles.append(admin_role)
        user3.addresses.append(
            Address(
                road_name='34 main road',
                postcode='IG114XE',
                city='London'
            )
        )

        user3.preference = Preference(
            language='English',
            currency='GBP',
        )

        session.add(user3)
        await session.commit()

asyncio.run(create_users())