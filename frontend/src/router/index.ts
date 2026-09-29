import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Substation = () => import('@/views/substation/index.vue')
const Line = () => import('@/views/line/index.vue')
const Inspection = () => import('@/views/inspection/index.vue')
const Outage = () => import('@/views/outage/index.vue')
const Load = () => import('@/views/load/index.vue')
const Switchop = () => import('@/views/switchop/index.vue')
const Emergency = () => import('@/views/emergency/index.vue')
const Repair = () => import('@/views/repair/index.vue')
const Workpermit = () => import('@/views/workpermit/index.vue')
const Protect = () => import('@/views/protect/index.vue')
const Battery = () => import('@/views/battery/index.vue')
const Meter = () => import('@/views/meter/index.vue')
const Dispatchlog = () => import('@/views/dispatchlog/index.vue')
const Grounding = () => import('@/views/grounding/index.vue')
const Capacity = () => import('@/views/capacity/index.vue')
const Tool = () => import('@/views/tool/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/substation', name: 'substation', component: Substation },
    { path: '/line', name: 'line', component: Line },
    { path: '/inspection', name: 'inspection', component: Inspection },
    { path: '/outage', name: 'outage', component: Outage },
    { path: '/load', name: 'load', component: Load },
    { path: '/switchop', name: 'switchop', component: Switchop },
    { path: '/emergency', name: 'emergency', component: Emergency },
    { path: '/repair', name: 'repair', component: Repair },
    { path: '/workpermit', name: 'workpermit', component: Workpermit },
    { path: '/protect', name: 'protect', component: Protect },
    { path: '/battery', name: 'battery', component: Battery },
    { path: '/meter', name: 'meter', component: Meter },
    { path: '/dispatchlog', name: 'dispatchlog', component: Dispatchlog },
    { path: '/grounding', name: 'grounding', component: Grounding },
    { path: '/capacity', name: 'capacity', component: Capacity },
    { path: '/tool', name: 'tool', component: Tool },
  ],
})

export default router
