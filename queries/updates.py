import asyncio

from sqlalchemy import select

from main import async_session
from models.user import Preference, User
#
# user_preference = (
#     Preference.query
#     .join(Preference.user)
#     .filter(User.email == 'johndoe@gmail.com')
#     .first()
# )
#
# user_preference.currency = 'GBP'
# session.commit()
#
# print(user_preference.currency)
#

async def update_user(first_name, last_name, email):
    async with async_session() as session:
            async with session.begin():
                    result = await session.execute(
                            select(User)
                            .where(User.first_name == first_name)
                            .where(User.last_name == last_name)
                    )

                    user = result.scalars().first()

                    if user:
                        user.email = email
                    else:
                        print('User not found')


asyncio.run(update_user('John', 'Doe', 'johndoe@hotmail.com'))


