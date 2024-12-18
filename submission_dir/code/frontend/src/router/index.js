import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import register from '../views/register.vue'
import Dashboard from '../views/dashboard.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/test',
    name: 'testRoute',
    component: () => import('@/views/test.vue')
  },
  {
    path: '/register',
    name: 'registerRoute',
    component: register
  },
  {
    path: '/login',
    name: 'loginRoute',
    component: () => import('@/views/login.vue')
  },
  {
    path: '/category/create',
    name: 'createCategoryRoute',
    component: () => import('@/views/categoryCreate.vue')
  },
  {
    path: '/product/create',
    name: 'createProductRoute',
    component: () => import('@/views/productCreate.vue')
  },
  {
    path: '/dashboard',
    name: 'dashRoute',
    component: Dashboard
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
