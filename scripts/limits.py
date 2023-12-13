from app.models import Limit, InstagramUser

# Normal limits for one account
limits = {'LIMIT_IP': (10, 'Кількість сторінок на 1 IP'),                     # use of 10 accounts per IP address (count)
          'MIN_PUBLIC_POST': (4, 'Мінімальна кількість постів'),              # min number publishing of post for account (count)
          'MAX_PUBLIC_POST': (16, 'Максимальна кількість постів'),            # max number publishing of post for account (count)
          'MIN_PUBLIC_HISTORY': (24, 'Мінімальна кількість історій'),         # min number publishing of history for account (count)
          'MAX_PUBLIC_HISTORY': (48, 'Максимальна кількість історій'),        # max number publishing of history for account (count)
          'MIN_DELAY': (1, 'Мінімальна затримка дій'),                        # min delay after each request (sec)
          'MAX_DELAY': (4, 'Максимальна затримка дій'),                       # max delay after each request (sec)
          'MIN_DIRECT': (7, 'Мінімальна кількість повідомлень (за мин)'),     # min delay after send message (minutes)
          'MAX_DIRECT': (10, 'Максимальна кількість повідомлень (за мин)'),   # max delay after send message (minutes)
}


def run():
    # for key, (value, description) in limits.items():
    #     Limit.objects.create(name=key, limit=value, description=description)
    print(1)
    d = InstagramUser.get_password(3)
    print(2)
    print(d)








