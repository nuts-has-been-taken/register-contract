import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DAppHomeView from '../views/DAppHomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/',
      name: 'dapp',
      component: DAppHomeView
    },
    {
      path: '/electionlist',
      name: 'electionlist',
      component: () => import('../views/ElectionListView.vue')
    },
    {
      path: '/vote/:id',
      name: 'vote',
      component: () => import('../views/VoteById.vue')
    }, {
      path: '/admin',
      name: 'admin',
      component: () => import('../views/AdminView.vue')
    }, {
      path: '/voter',
      name: 'voter',
      component: () => import('../views/VoterView.vue')
    },{
      path:'/register',
      name:'register',
      component:()=>import('../views/RegisterView.vue')
    },{
      path:'/createelection',
      name:'createelection',
      component:()=>import('../views/CreateElectionView.vue')
    },{
      path:'/deleteelection',
      name:'deleteelection',
      component:()=>import('../views/DeleteElectionView.vue')
    }
  ]
})

export default router
