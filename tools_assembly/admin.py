from django.contrib import admin
from .models import ToolAssembly, Holder, Tool, UserComment

admin.site.register(ToolAssembly)
admin.site.register(Holder)
admin.site.register(Tool)
admin.site.register(UserComment)
