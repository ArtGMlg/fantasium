import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import StartView from '../views/StartView.vue'
import UnderDevelopmentView from '../views/UnderDevelopmentView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: StartView,
  },
  {
    path: '/app',
    name: 'app',
    component: () => import('../views/HomeView.vue'),
  },
  {
    path: '/archive',
    name: 'archive',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: UnderDevelopmentView,
  },
  {
    path: '/settings',
    name: 'settings',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: UnderDevelopmentView,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
