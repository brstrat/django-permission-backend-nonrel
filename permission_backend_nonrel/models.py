#from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db import models

from djangotoolbox.fields import ListField


class UserPermissionList(models.Model):
    user = models.ForeignKey('common.User')
    
    permission_list = ListField(models.CharField(max_length=64))
    permission_fk_list = ListField(models.CharField(max_length=32))

    group_fk_list = ListField(models.CharField(max_length=32))


class GroupPermissionList(models.Model):
    group = models.ForeignKey(Group)
    permission_list = ListField(models.CharField(max_length=64))
    permission_fk_list = ListField(models.CharField(max_length=32))
