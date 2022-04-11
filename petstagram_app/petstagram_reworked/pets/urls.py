# from django.urls import path
#
# from petstagram_reworked.pets.views import list_pets, details_or_comment_pet, like_pet, create_pet, edit_pet, \
#     delete_pet, comment_pet
#
# urlpatterns = [
#     path('', list_pets, name='list pets'),
#     path('details/<int:pk>', details_or_comment_pet, name='pet details'),
#     path('like/<int:pk>', like_pet, name='like pet'),
#     path('create/', create_pet, name='create pet'),
#     path('edit/<int:pk>', edit_pet, name='edit pet'),
#     path('delete/<int:pk>', delete_pet, name='delete pet'),
#     path('comment/<int:pk>', comment_pet, name='comment pet'),
# ]

from django.urls import path

from petstagram_reworked.pets.views import PetDetailsView, CommentPetView, ListPetsView, \
    CreatePetView, EditPetView, DeletePetView, LikePetView

urlpatterns = [
    path('', ListPetsView.as_view(), name='list pets'),
    path('details/<int:pk>', PetDetailsView.as_view(), name='pet details'),
    path('like/<int:pk>', LikePetView.as_view(), name='like pet'),
    path('create/', CreatePetView.as_view(), name='create pet'),
    path('edit/<int:pk>', EditPetView.as_view(), name='edit pet'),
    path('delete/<int:pk>', DeletePetView.as_view(), name='delete pet'),
    path('comment/<int:pk>', CommentPetView.as_view(), name='comment pet'),
]