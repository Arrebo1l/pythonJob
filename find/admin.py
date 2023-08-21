from django.contrib import admin
from .models import JobPost
from .models import Management
from .models import Sales
from .models import Other

admin.site.register(JobPost)
admin.site.register(Management)
admin.site.register(Sales)
admin.site.register(Other)