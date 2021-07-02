<template>
  <div class="topic-title">
    <span>Topics</span>
    <div>
      <el-button @click="onToggleModal" type="success"
        >Create <i class="el-icon-circle-plus el-icon-left"></i>
      </el-button>
    </div>
  </div>
  <div>
    <div v-for="topic in listTopic" :key="topic.id" class="topic-item">
      <div style="width: 50%">
        <a>{{ topic.name }}</a>
      </div>
      <div style="width: 30%">
        <span class="description">{{ topic.description }}</span>
      </div>
      <div style="width: 20%">
        <el-button
          @click="onDeleteTopic(topic)"
          type="danger"
          icon="el-icon-delete"
        ></el-button>
      </div>
    </div>
  </div>

  <!--  Create Topic-->
  <modal
    title="Create Topic"
    :dialog-visible="dialogVisibleCreate"
    :on-toggle="onToggleModal"
    :on-submit-form="onsubmitForm"
  >
    <el-form class="create-topic" :model="form">
      <el-form-item label="Topic name" :label-width="formLabelWidth">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="Description" :label-width="formLabelWidth">
        <el-input v-model="form.description"></el-input>
      </el-form-item>
    </el-form>
  </modal>
</template>

<script>
import { reactive, ref } from "vue";
import { getTopic, postTopic, deleteTopic } from "../services/topic";
import { ElMessage, ElMessageBox } from "element-plus";
import Modal from "../components/Modal";
import { useStore } from "vuex";
import { routerPush } from "../router";

export default {
  name: "TopicList",
  components: {
    Modal,
  },
  setup() {
    const store = useStore();

    const user_id = store.getters.user_id;
    const listTopic = ref([]);
    const dialogVisibleCreate = ref(false);
    const form = reactive({
      user: user_id,
      name: "",
      description: "",
    });

    const gotoPageWord = async () => {
      await routerPush("topic");
    };

    const onToggleModal = () => {
      form.name = "";
      form.description = "";
      dialogVisibleCreate.value = !dialogVisibleCreate.value;
    };

    const onsubmitForm = async () => {
      const result = await postTopic(form);

      if (result.status === "ok") {
        dialogVisibleCreate.value = !dialogVisibleCreate.value;
        await fetchTopic();
      } else {
        ElMessage.error("Can't not create topic");
      }
    };

    const fetchTopic = async () => {
      const result = await getTopic({ user: user_id });
      if (result.status === "ok") {
        listTopic.value = result.data;
      } else {
        ElMessage.error("Can't not get topic");
      }
    };

    const onDeleteTopic = async (topic) => {
      ElMessageBox.confirm("Are you sure delete topic?", "Warning", {
        confirmButtonText: "OK",
        cancelButtonText: "Cancel",
        type: "warning",
      })
        .then(async () => {
          const result = await deleteTopic(topic.id);
          if (result.status === "ok") {
            await fetchTopic();
            ElMessage({
              type: "success",
              message: "Delete completed",
            });
          } else {
            ElMessage({
              type: "error",
              message: "delete topic error",
            });
          }
        })
        .catch(() => {
          ElMessage({
            type: "info",
            message: "Delete canceled",
          });
        });
    };

    fetchTopic();

    return {
      listTopic,
      formLabelWidth: "120px",
      form,
      dialogVisibleCreate,
      onToggleModal,
      onsubmitForm,
      gotoPageWord,
      onDeleteTopic,
    };
  },
};
</script>
