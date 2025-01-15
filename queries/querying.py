from sqlalchemy import desc

from models.user import User, Role

all_users = User.query.all()
first_user = User.query.first()

print(all_users)
print(first_user)

johns = User.query.filter_by(first_name='John').all()
print(johns)

johns = User.query.filter(User.first_name == 'John').all()
print(johns)


gmail_users = User.query.filter(User.email.like('%@gmail.com')).all()
print(gmail_users)

super_admins = (User.query
                .join(User.roles)
                .filter(Role.slug == 'super-admin').all())
print(super_admins)


users_by_name = User.query.order_by(User.first_name).all()
print(users_by_name)

users_by_name_desc = User.query.order_by(desc(User.first_name)).all()
print(users_by_name_desc)


first_three_users = User.query.limit(3).all()
print(first_three_users)

skip_three_users = User.query.offset(3).all()
print(skip_three_users)


num_of_users = User.query.count()
print(num_of_users)
