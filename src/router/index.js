import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

export const AppRouteNames =
  "home" | "login" | "dictionary" | "topic" | "register"; //|  | "profile" | "profile-favorites" | ;

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/Login.vue"),
  },
  {
    path: "/dictionary",
    name: "dictionary",
    component: () => import("../views/Dictionary.vue"),
  },
  {
    path: "/topic",
    name: "topic",
    component: () => import("../views/Topic.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () => import("../views/Register.vue"),
  },
  {
    path: "/profile/",
    name: "profile",
    component: () => import("../views/Profile.vue"),
  },
  // {
  //   name: "settings",
  //   path: "/settings",
  //   component: () => import("../views/Settings.vue"),
  // },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export const routerPush = (name, params) => {
  if (params !== undefined) {
    return router.push({
      name,
      params,
    });
  } else {
    return router.push({ name });
  }
};

export default router;
