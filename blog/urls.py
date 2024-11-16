from django.urls import path

from blog.views import index, computers, contact, means_clothes, womans_clothes, category, detail

urlpatterns = [
    # 👉-------------------------Pages----------------------------👈

    path('', index, name='index'),
    path('computers/', computers, name='computers'),
    path('contact/', contact, name='contact'),
    path('means_clothes/', means_clothes, name='mansclothes'),
    path('womans_clothes/', womans_clothes, name='womansclothes'),

    # 👉-------------------------Pages end----------------------------👈

    # ��-------------------------category----------------------------��

    path('category/<slug:slug>', category, name='category'),

    # ��-------------------------category end----------------------------��

    # ��-------------------------detail----------------------------��

    path('detail/<int:id>', detail, name='detail')

    # ��-------------------------detail end----------------------------��

]