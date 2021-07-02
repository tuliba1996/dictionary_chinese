<template>
  <div class="page-container profile">
    <div class="title">
      <span>PROFILE</span>
    </div>
    <div class="info-container">
      <el-avatar :size="130">
        <img
          src="https://cube.elemecdn.com/e/fd/0fc7d20532fdaf769a25683617711png.png"
        />
      </el-avatar>
      <div class="info">
        <p>{{ user_info.name }}</p>
        <p>{{ user_info.email }}</p>
      </div>
    </div>
    <div class="btn-logout">
      <el-button @click="onLogout" type="danger">Log Out</el-button>
    </div>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { routerPush } from "../router";

export default {
  name: "Profile",
  setup() {
    const store = useStore();
    const user_info = store.getters.user;

    const onLogout = async () => {
      await store.dispatch("onUpdateUser", null);
      await routerPush("home");
    };
    return {
      onLogout,
      user_info,
    };
  },
};
</script>
