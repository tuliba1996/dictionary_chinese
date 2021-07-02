<template>
  <div>TO DO</div>
</template>

<script>
import { ref } from "vue";

export default {
  name: "Topic",
  set() {
    const dialogVisibleCreate = ref(false);

    const onToggleModal = () => {
      dialogVisibleCreate.value = !dialogVisibleCreate.value;
    };
    return {
      dialogVisibleCreate,
      onToggleModal,
    };
  },
};
</script>
