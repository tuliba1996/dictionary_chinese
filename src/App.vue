<template>
  <app-navigation />
  <router-view />
</template>

<script>
import AppNavigation from "./components/AppNavigation";


  export default {
    name: "App",
    components: {
      AppNavigation
    }
  }

</script>
