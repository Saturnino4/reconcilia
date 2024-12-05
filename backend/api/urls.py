from django.urls import path
from api.Views import *
from api.views import outOfService


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

    # ********************** GET agendamento ************************
#     path('agendamento/',  AgendamentoViewsGet.as_view(), name='agendamento'),
#     path('agendamento/<int:id>/', AgendamentoViewsGet.as_view() , name='agendamento'),
#     path('agendamento/s/<str:campo>/<str:valor>/', getAgendamentoByAnyColumn , name='agendamento'),

#     # ********************** POST agendamento ************************
#     path('agendamento/registrar/', AgendamentoViewsPost.as_view() , name='agendamento'),

#     # ********************** PUT agendamento ************************
#     path('agendamento/<int:id>/atualizar/', AgendamentoViewsPut.as_view() , name='agendamento'),

#     # ********************** DELETE agendamento ************************
#     path('agendamento/<int:id>/deletar/',  AgendamentoViewsDelete.as_view() , name='agendamento'),

# # -------------------------------- /////////////////////// -------------------------------------------------

#     # ********************** GET agendamento_Cliente ************************
#     path('agendamento_servico/',  Agendamento_ServicoViewsGet.as_view(), name='agendamento_servico'),
#     path('agendamento_servico/<int:id>/', Agendamento_ServicoViewsGet.as_view() , name='agendamento_servico'),
#     path('agendamento_servico/s/<str:campo>/<str:valor>/', getAgendamentoByAnyColumn , name='agendamento_servico'),

#     # ********************** POST agendamento ************************
#     path('agendamento_servico/registrar/', Agendamento_ServicoViewsPost.as_view() , name='agendamento_servico'),

#     # ********************** PUT agendamento ************************
#     path('agendamento_servico/<int:id>/atualizar/', Agendamento_ServicoViewsPut.as_view() , name='agendamento_servico'),

#     # ********************** DELETE agendamento ************************
#     path('agendamento_servico/<int:id>/deletar/',  Agendamento_ServicoViewsDelete.as_view() , name='agendamento_servico'),

# # -------------------------------- /////////////////////// -------------------------------------------------

# # ********************** GET agendamento_funcionario ************************
#     path('agendamento_funcionario/',  Agendamento_FuncionarioViewsGet.as_view(), name='agendamento_funcionario'),
#     path('agendamento_funcionario/<int:id>/', Agendamento_FuncionarioViewsGet.as_view() , name='agendamento_funcionario'),
#     path('agendamento_funcionario/s/<str:campo>/<str:valor>/', getAgendamentoByAnyColumn , name='agendamento_funcionario'),

#     # ********************** POST agendamento ************************
#     path('agendamento_funcionario/registrar/', Agendamento_FuncionarioViewsPost.as_view() , name='agendamento_funcionario'),

#     # ********************** PUT agendamento ************************
#     path('agendamento_funcionario/<int:id>/atualizar/', Agendamento_FuncionarioViewsPut.as_view() , name='agendamento_funcionario'),

#     # ********************** DELETE agendamento ************************
#     path('agendamento_funcionario/<int:id>/deletar/',  Agendamento_FuncionarioViewsDelete.as_view() , name='agendamento_funcionario'),

# # -------------------------------- /////////////////////// -------------------------------------------------


#     # ********************** GET financa ************************
#     path('financa/', FinancaViewsGet.as_view() , name='financa'),
#     path('financa/<int:id>/', FinancaViewsGet.as_view() , name='financa'),

#     # ********************** POST financa ************************
#     path('financa/registrar/', FinancaViewsPost.as_view() , name='financa'),

#     # ********************** PUT financa ************************
#     path('financa/<int:id>/atualizar/', FinancaViewsPut.as_view() , name='financa'),

#     # ********************** DELETE financa ************************
#     path('financa/<int:id>/deletar/',  FinancaViewsDelete.as_view() , name='financa'),

# # -------------------------------- /////////////////////// -------------------------------------------------

#     # ********************** GET FUNCIONARIO ************************
#     path('funcionario/', FuncionarioViewsGet.as_view() , name='funcionario'),

#     # ********************** POST FUNCIONARIO ************************
#     path('funcionario/registrar/', FuncionarioViewsPost.as_view() , name='funcionario'),

#     # ********************** PUT FUNCIONARIO ************************
#     path('funcionario/<int:id>/atualizar/', FuncionarioViewsPut.as_view() , name='funcionario'),

#     # ********************** DELETE FUNCIONARIO ************************
#     path('funcionario/<int:id>/deletar/',  FuncionarioViewsDelete.as_view() , name='funcionario'),

# # -------------------------------- /////////////////////// -------------------------------------------------

#     # ********************** GET SERVICO ************************
#     path('servico/', ServicoViewsGet.as_view() , name='servico'),
#     path('servico/<int:id>/', ServicoViewsGet.as_view() , name='servico'),

#     # ********************** POST SERVICO ************************
#     path('servico/registrar/', ServicoViewsPost.as_view() , name='servico'),

#     # ********************** PUT SERVICO ************************
#     path('servico/<int:id>/atualizar/', ServicoViewsPut.as_view() , name='servico'),

#     # ********************** DELETE SERVICO ************************
#     path('servico/<int:id>/deletar/',  ServicoViewsDelete.as_view() , name='servico'),

# # -------------------------------- /////////////////////// -------------------------------------------------

#     # ********************** GET notificacao ************************
#     path('notificacao/', NotificacaoViewsGet.as_view() , name='notificacao'),
#     path('notificacao/<int:id>/', NotificacaoViewsGet.as_view() , name='notificacao'),

#     # ********************** POST notificacao ************************
#     path('notificacao/registrar/', NotificacaoViewsPost.as_view() , name='notificacao'),

#     # ********************** PUT notificacao ************************
#     path('notificacao/<int:id>/atualizar/', NotificacaoViewsPut.as_view() , name='notificacao'),

#     # ********************** DELETE notificacao ************************
#     path('notificacao/<int:id>/deletar/',  NotificacaoViewsDelete.as_view() , name='notificacao'),

# # -------------------------------- /////////////////////// -------------------------------------------------

 




]
