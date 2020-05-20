import Vue from 'vue'
import Router from "vue-router";
import mainPage from "@/views/mainPage";
import About from "@/views/About";
import Works from "@/views/Works";
import Movies from "@/views/Movies";
import Goods from "@/views/Goods";
import Contact from "@/views/Contact";

Vue.use(Router)

const routes = [
    {path: '/', name: 'mainPage', component: mainPage},
    {path: '/about', name: 'about', component: About},
    {path: '/works', name: 'works', component: Works},
    {path: '/movies', name: 'movies', component: Movies},
    {path: '/goods', name: 'goods', component: Goods},
    {path: '/contact', name: 'contact', component: Contact}
]

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: routes
})