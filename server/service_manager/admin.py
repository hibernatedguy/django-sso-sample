from django.contrib import admin

from simple_sso.sso_server.models import Token, Consumer

admin.site.register(Token)
admin.site.register(Consumer)
