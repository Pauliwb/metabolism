# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from my_app.models import Product, AppUser, UserInformation

admin.site.register(Product)
admin.site.register(AppUser)
admin.site.register(UserInformation)
