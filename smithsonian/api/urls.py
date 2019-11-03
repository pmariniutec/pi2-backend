from django.urls import path

from smithsonian.api.views import users, sightings

urlpatterns = [
    # NOTE: GET
    path('user/', users.UserDetail.as_view(), name='user'),

    # NOTE: POST
    # AUTHENTICATED VIEW (Send Header with token)
    # Expects: JSON
    # Example:
    #   {
    #       images: [url1, url2, ...], (max 5)
    #       cause_of_death: '',
    #       is_alive: '',
    #       latitude: 000.000,
    #       longitude: 000.000,
    #       comment: '',
    #       species: '',
    #   }
    path('sighting/', sightings.SightingView.as_view(), name='sighting')
]
