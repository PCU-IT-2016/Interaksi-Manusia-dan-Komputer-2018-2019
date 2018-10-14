from django.contrib import admin

from MainApp.models import Account, City, Infrastructure, Place, Category, Transportation, Schedule, Transaction, Transactions_Detail

admin.site.register(Account)
admin.site.register(City)
admin.site.register(Infrastructure)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(Transportation)
admin.site.register(Schedule)
admin.site.register(Transaction)
admin.site.register(Transactions_Detail)