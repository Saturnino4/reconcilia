import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '@/views/dashboardViews.vue'
   
const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: Dashboard
  },
 
  {
    name: 'login',
    path: '/login',
    component : () =>  import('@/views/loginViews.vue'),
  },
  {
    name: 'registro_externo',
    path: '/registro_externo',
    component : () =>  import('@/views/registro_externo.vue'),
  },
  
  {
    name: 'extrato',
    path: '/extrato',
    component : () =>  import('@/views/extratoViews.vue'),
  },

  {
    name: 'analise',
    path: '/analise',
    component : () =>  import('@/views/analiseViews.vue'),
  },
  {
    name: 'simulacao',
    path: '/simulacao',
    component : () =>  import('@/views/simulacaoViews.vue'),
  },

  {
    name: 'pendencia',
    path: '/pendencia',
    component : () =>  import('@/views/pendenciaViews.vue'),
  },

  {
    name: 'tarefa',
    path: '/tarefa',
    component : () =>  import('@/views/tarefaViews.vue'),
  },
  
  {
    name: 'cliente',
    path: '/cliente',
    component : () =>  import('@/views/clienteViews.vue'),
  },
  
  {
    name: 'configuracao',
    path: '/configuracao',
    component : () =>  import('@/views/configuracaoViews.vue'),
  },
  

  // {
  //   name: 'funcionario',
  //   path: '/funcionario',
  //   component : () =>  import('@/views/Funcionario.vue'),
  // },
 

  // {
  //   path: '/financa',
  //   name: 'financa',
  //   component: () => import('@/views/Financa.vue')
  // },  

  // {
  //   name: 'galeria',
  //   path: '/galeria',
  //   component : () =>  import('@/views/Galeria.vue'),
  // },  
  // {
  //   path: '/agendamento',
  //   name: 'agendamento',
    
  //   component:  () => import('@/views/Agendamento.vue')
  // },

  {
    path: '/:catchAll(.*)',
    name: 'not-found',
    component: () => import('@/views/NotFound.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach((to, from, next) => {
  // Verifique se há dados do usuário no localStorage
  const user = JSON.parse(localStorage.getItem('userData'));

  if (!user && to.path !== '/login') {
    // Se não houver usuário e a rota não for '/login', redirecione para '/login'
    next('/login');
  } else {
    // Caso contrário, continue para a rota solicitada
    next();
  }
});


export default router
