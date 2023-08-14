import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import FormView from '../views/FormView.vue'
import RateView from '../views/RateView.vue'
import ConvertView from '../views/ConvertView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/form',
    name: 'Form',
    component: FormView
  },
  {
    path: '/rate',
    name: 'Rate',
    component: RateView
  },
  {
    path: '/convert',
    name: 'Convert',
    component: ConvertView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
