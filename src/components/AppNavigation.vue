<template>
  <nav class="navbar navbar-light">
    <div class="container">
      <AppLink class="navbar-brand" name="home">Panda</AppLink>
      <ul class="nav navbar-nav pull-xs-right">
        <li v-for="link in navLinks" :key="link.name" class="nav-item">
          <AppLink
            class="nav-link"
            active-class="active"
            :name="link.name"
            :params="link.params"
          >
            <i v-if="link.icon" :class="link.icon" /> {{ link.title }}
          </AppLink>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import { useStore } from "vuex";
import { computed } from "vue";

export default {
  name: "AppNavigation",
  setup() {
    const store = useStore();
    const username = computed(() => store.getters.user?.name);

    const displayStatus = computed(() =>
      username.value ? "authorized" : "anonym"
    );

    const allNavLinks = computed(() => [
      {
        name: "home",
        title: "Home",
        display: "all",
        icon: "el-icon-s-home",
      },
      {
        name: "login",
        title: "Sign in",
        display: "anonym",
      },
      {
        name: "register",
        title: "Sign up",
        display: "anonym",
      },
      {
        name: "dictionary",
        title: "Dictionary",
        display: "authorized",
        icon: "el-icon-notebook-1",
      },
      {
        name: "profile",
        params: { username: username.value },
        title: username.value || "User",
        display: "authorized",
      },
    ]);

    const navLinks = computed(() =>
      allNavLinks.value.filter(
        (l) => l.display === displayStatus.value || l.display === "all"
      )
    );

    return { navLinks };
  },
};
</script>
