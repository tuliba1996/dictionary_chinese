<template>
  <div id="login">
    <el-card class="form-container">
      <template #header>
        <div class="card-header">
          <h2>Sign in to Account</h2>
        </div>
      </template>
      <div>
        <el-form
          ref="formRef"
          :model="form"
          :rules="rules"
          @submit.prevent="login"
          class="form-inner"
        >
          <el-form-item prop="email">
            <el-input
              placeholder="Please input your Email"
              v-model="form.email"
            ></el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input
              placeholder="Password"
              type="password"
              v-model="form.password"
            ></el-input>
          </el-form-item>
        </el-form>
        <el-button
          type="success"
          :disabled="!form.email || !form.password"
          @click="login"
          >SIGN IN
        </el-button>
        <div class="login-footer">
          <div>
            <span>Don’t have an account? </span>
            <AppLink name="register">Sign Up</AppLink>
          </div>
          <p><i>Forgot Password?</i></p>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
import { ref, reactive } from "vue";
import { routerPush } from "../router";
import { postLogin } from "../services/postLogin";
import { useStore } from "vuex";
import { ElMessage } from "element-plus";

export default {
  name: "Login",
  setup() {
    const formRef = ref(null);
    const isDisable = ref(true);

    const store = useStore();

    const form = reactive({
      email: "",
      password: "",
    });
    const rules = reactive({
      email: [
        { required: true, message: "Please input Email", trigger: "blur" },
        {
          type: "email",
          message: "Please input correct email address",
          trigger: ["blur"],
        },
      ],
      password: [
        { required: true, message: "Please input Password", trigger: "blur" },
      ],
    });

    const login = async () => {
      formRef.value?.validate(async (valid) => {
        if (!valid) {
          return;
        }
        const result = await postLogin(form);
        if (result.status === "ok") {
          await store.dispatch("onUpdateUser", result.data);
          await routerPush("home");
        } else {
          ElMessage.error("Error, please try again!");
        }
      });
    };

    return { formRef, rules, form, login, isDisable };
  },
};
</script>
