<template>
  <router-link
    :aria-label="props.name"
    :to="props"
    v-bind="attrs"
  >
    <slot />
  </router-link>
</template>

<script>
import { RouterLink } from "vue-router";


export default {
  name: "AppLink",
  components: {
    RouterLink,
  },
  props: {
    name: { type: String, required: true },
    params: { type: Object, default: () => ({}) },
  },
  setup(props, { attrs }) {
    return {
      props,
      attrs,
    }
  },
};
</script>

<style scoped>

</style>
