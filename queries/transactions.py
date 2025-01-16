import asyncio

from main import async_session
from models.user import User, Preference

async def transaction_example():
    async with async_session() as session:
        user = User(
            first_name='John',
            last_name='Smith',
            email='jsmith@gmail.com'
        )
        session.add(user)

        raise Exception("Something went wrong")

        preference = Preference(
            language="English",
            currency="GBP",
        )

        preference.user = user
        await session.commit()


asyncio.run(transaction_example())