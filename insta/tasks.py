from insta.celery import app_insta
from celery import shared_task
from app.models import UserID, InstagramUser, SystemSetting
from app.insta_script.login import login_user
from app.insta_script.tegs import get_user_pk_by_tag
from app.insta_script.user import follow
from instagrapi import Client
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


@app_insta.task(bind=True)
def get_all_teg():
    users = UserID.objects.all()
    for user in users:
        get_user_id_by_teg_.delay(user, user.id)


@app_insta.task(bind=True)
def get_user_id_by_teg_(teg_name, teg_id):
    try:
        user = InstagramUser.objects.get(system=True)
    except ObjectDoesNotExist:
        return

    cl = login_user(user.pk, user.login, user.password)
    users_pk = get_user_pk_by_tag(cl, teg_name, SystemSetting.get_value('AMOUNT_FOLLOWERS'))
    if users_pk:
        user_objects = [UserID(user_id=user, teg_id=teg_id) for user in users_pk]
        UserID.objects.bulk_create(user_objects)


@app_insta.task(bind=True)
def get_all_active_user():
    active_users = InstagramUser.objects.filter(
        Q(active=True) & Q(system=False) & Q(main=False)
    )

    if active_users is None:
        return
    for user in active_users:
        user_tags_pk = list(user.teg.values_list('pk', flat=True))
        if user_tags_pk:
            follow_to_user.delay(user.pk, user.login, user.password, user_tags_pk)


@app_insta.task(bind=True)
def follow_to_user(user_pk, login, password, user_tags_names):
    cl = login_user(str(user_pk), login, password)
    for pk in user_tags_names:
        user_ids = UserID.objects.filter(teg=pk).values_list('user_id', flat=True)
        for user_id in user_ids:
            follow(cl, str(user_id))



