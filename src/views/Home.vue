<template>
  <div class="home">
    <div class="banner">
      <div class="container">
        <el-avatar shape="square" :size="100">
          <img src="../assets/images/panda.png" />
        </el-avatar>
        <h1 class="logo">PANDA CHINESE</h1>
      </div>
    </div>
  </div>
  <div class="page-container">
    <search-text v-if="!isAuth" />
    <topic-list v-if="isAuth" />
  </div>
</template>

<script>
import SearchText from "../components/SearchText";
import TopicList from "../components/TopicList";
import { useStore } from "vuex";
import { computed } from "vue";
import { getItems } from "../services/fireStore";
export default {
  name: "Home",
  components: {
    SearchText,
    TopicList,
  },
  setup() {
    const store = useStore();
    const isAuth = computed(() => store.getters.isAuthorized);

    const getData = async () => {
      const items = await getItems("topic");
      console.log("items", items);
    }
    getData();
    return {
      isAuth,
    };
  },
};
</script>
