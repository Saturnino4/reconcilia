from django.urls import path
from api.Views import *
from api.views import outOfService
from api.views import ourData


urlpatterns = [
    # ********************** GET UTILIZADOR ************************
    path('utilizador/', UtilizadorViewsGet.as_view(), name='utilizador'),
    path('utilizador/<int:id>/', UtilizadorViewsGet.as_view(), name='utilizador'),

    # ********************** POST UTILIZADOR ************************
    path('utilizador/registrar/', UtilizadorViewsPost.as_view(), name='utilizador'),
    path('login/', LoginViews.as_view(), name='login'),

    # ********************** PUT UTILIZADOR ************************
    path('utilizador/<int:id>/atualizar/', UtilizadorViewsPut.as_view(), name='utilizador'),

    # ********************** DELETE UTILIZADOR ************************
    path('utilizador/<int:id>/deletar/', UtilizadorViewsDelete.as_view(), name='utilizador'),

# -------------------------------- /////////////////////// -------------------------------------------------

    # ********************** GET ROLE ************************
    path('role/', RoleViewsGet.as_view(), name='role'),
    path('role/<int:id>/', RoleViewsGet.as_view(), name='role'),

    # ********************** POST ROLE ************************
    path('role/registrar/', RoleViewsPost.as_view(), name='role'),

    # ********************** PUT ROLE ************************
    path('role/<int:id>/atualizar/', RoleViewsPut.as_view(), name='role'),

    # ********************** DELETE ROLE ************************
    path('role/<int:id>/deletar/', RoleViewsDelete.as_view(), name='role'),
# -------------------------------- /////////////////////// -------------------------------------------------

    # ********************** GET MOEDA ************************
    path('moeda/', MoedaViewsGet.as_view(), name='moeda'),
    path('moeda/<int:id>/', MoedaViewsGet.as_view(), name='moeda'),

    # ********************** POST MOEDA ************************
    path('moeda/registrar/', MoedaViewsPost.as_view(), name='moeda'),

    # ********************** PUT MOEDA ************************
    path('moeda/<int:id>/atualizar/', MoedaViewsPut.as_view(), name='moeda'),

    # ********************** DELETE MOEDA ************************
    path('moeda/<int:id>/deletar/', MoedaViewsDelete.as_view(), name='moeda'),
# -------------------------------- /////////////////////// -------------------------------------------------

    # ********************** GET LOCALIZACAO ************************
    path('local/', LocalViewsGet.as_view(), name='local'),
    path('local/<int:id>/', LocalViewsGet.as_view(), name='local'),

    # ********************** POST LOCALIZACAO ************************
    path('local/registrar/', LocalViewsPost.as_view(), name='local'),

    # ********************** PUT LOCALIZACAO ************************
    path('local/<int:id>/atualizar/', LocalViewsPut.as_view(), name='local'),

    # ********************** DELETE LOCALIZACAO ************************
    path('local/<int:id>/deletar/', LocalViewsDelete.as_view(), name='local'),

# -------------------------------- /////////////////////// -------------------------------------------------

    # ********************** GET BANCO ************************
    path('banco/', BancoViewsGet.as_view(), name='banco'),
    path('banco/<int:id>/', BancoViewsGet.as_view(), name='banco'),

    # ********************** POST BANCO ************************
    path('banco/registrar/', BancoViewsPost.as_view(), name='banco'),

    # ********************** PUT BANCO ************************
    path('banco/<int:id>/atualizar/', BancoViewsPut.as_view(), name='banco'),

    # ********************** DELETE BANCO ************************
    path('banco/<int:id>/deletar/', BancoViewsDelete.as_view(), name='banco'),

# -------------------------------- /////////////////////// -------------------------------------------------

    # ********************** GET CONTA ************************
    path('conta/', ContaViewsGet.as_view(), name='conta'),
    path('conta/<int:id>/', ContaViewsGet.as_view(), name='conta'),

    # ********************** POST CONTA ************************
    path('conta/registrar/', ContaViewsPost.as_view(), name='conta'),

    # ********************** PUT CONTA ************************
    path('conta/<int:id>/atualizar/', ContaViewsPut.as_view(), name='conta'),

    # ********************** DELETE CONTA ************************
    path('conta/<int:id>/deletar/', ContaViewsDelete.as_view(), name='conta'),

# -------------------------------- /////////////////////// -------------------------------------------------

    # ********************** GET CONTA ************************
    path('swift/', SwiftView.as_view(), name='swift'),

    path('nostro/', ourData, name='nostro'),



# -------------------------------- /////////////////////// -------------------------------------------------

   


    # ********************** GET PERMISSAO ************************
    path('permissao/', PermissaoViewsGet.as_view(), name='permissao'),
    path('permissao/<int:id>/', PermissaoViewsGet.as_view(), name='permissao'),

    path('permissao/u/<int:id>/', Permissao_Utilizador.as_view(), name='permissao'),

    # ********************** POST PERMISSAO ************************
    path('permissao/registrar/', PermissaoViewsPost.as_view(), name='permissao'),

    # ********************** PUT PERMISSAO ************************
    path('permissao/<int:id>/atualizar/', PermissaoViewsPut.as_view(), name='permissao'),

    # ********************** DELETE PERMISSAO ************************
    path('permissao/<int:id>/deletar/', PermissaoViewsDelete.as_view(), name='permissao'),

# -------------------------------- /////////////////////// -------------------------------------------------

    # ********************** GET CLIENTE ************************
    path('cliente/', ClienteViewsGet.as_view(), name='cliente'),
    path('cliente/<int:id>/', ClienteViewsGet.as_view(), name='cliente'),
    # path('cliente/s/<str:campo>/<str:valor>/', getClienteByAnyColumn, name='cliente'),

    # ********************** POST CLIENTE ************************
    path('cliente/registrar/', ClienteViewsPost.as_view(), name='cliente'),

    # ********************** PUT CLIENTE ************************
    path('cliente/<int:id>/atualizar/', ClienteViewsPut.as_view(), name='cliente'),

    # ********************** DELETE CLIENTE ************************
    path('cliente/<int:id>/deletar/', ClienteViewsDelete.as_view(), name='cliente'),

# -------------------------------- /////////////////////// -------------------------------------------------

    # ********************** GET HISTORICO ************************
    path('historico/', outOfService , name='historico'),
    path('historico/<int:id>/',outOfService , name='historico'),

    # ********************** POST HISTORICO ************************
    path('historico/registrar/', outOfService , name='historico'),

    # ********************** PUT HISTORICO ************************
    path('historico/<int:id>/atualizar/', outOfService , name='historico'),

    # ********************** DELETE HISTORICO ************************
    path('historico/<int:id>/deletar/',  outOfService , name='historico'),

# -------------------------------- /////////////////////// -------------------------------------------------

]