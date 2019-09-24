from django.urls import path,include
from app_version_1 import views

urlpatterns = [
    path('',views.home),
    path('login/',views.login),
    path('form-register/',views.registerForm),
    path('register/', views.register),
    path('form-bus/', views.busForm),
    path('form-add-bus/', views.addBusForm),
    path('add-bus/', views.addBus),
    path('delete-bus/<int:b_id>', views.deleteBus),
    path('form-update-bus/<int:b_id>', views.formUpdateBus),
    path('update-bus/', views.updateBus),
    path('form-forgot-password/', views.formForgotPassword),
    path('forgot-password/',views.forgotPassword),

    path('form-search-bus/',views.formSearchBus),
    path('search-bus/',views.searchBus),

    path('seat/<int:b_id>', views.seat),
    path('transaction/<int:b_id>', views.transaction),

    path('logout/',views.logout),
    path('form-change-password/',views.formChangePassword),
    path('change-password/',views.changePassword)

]