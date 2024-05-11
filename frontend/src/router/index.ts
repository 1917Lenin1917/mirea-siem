import {createRouter, createWebHistory, RouteRecordRaw} from 'vue-router';

const routes: Array<RouteRecordRaw> = [
    {
        path: '/',
        name: 'index',
        redirect: '/connect',
    },
    {
        path: '/connect',
        name: 'connect',
        component: () => import('../views/ConnectPage/ConnectPage.vue')
    },
    {
        path: '/scripts',
        name: 'scripts',
        component: () => import('../views/ScriptsPage/ScriptsPage.vue')
    },
    {
        path: '/incidents',
        name: 'incidents',
        component: () => import('../views/IncidentsPage/IncidentsPage.vue')
    },
    {
        path: '/recommendations',
        name: 'recommendations',
        component: () => import('../views/RecommendationsPage/Recommendations.vue')
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router