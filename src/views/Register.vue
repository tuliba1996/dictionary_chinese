<template>
  <div id="login">
    <el-card class="form-container" v-if="!registerSuccess">
      <template #header>
        <div class="card-header">
          <h2>Sign up</h2>
        </div>
      </template>
      <div>
        <el-form
          ref="formRef"
          :model="form"
          :rules="rules"
          @submit.prevent="register"
          class="form-inner"
        >
          <el-form-item prop="first_name">
            <el-input
              placeholder="Please input your Name"
              v-model="form.first_name"
            ></el-input>
          </el-form-item>
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
          :disabled="!(form.first_name && form.email && form.password)"
          @click="register"
          >SIGN UP
        </el-button>
      </div>
    </el-card>
    <el-card v-if="registerSuccess">
      <div>
        <p>Register is success!</p>
        <el-button @click="gotoPageLogin" type="success">LOGIN</el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
import { ref, reactive } from "vue";
import { postRegister } from "../services/postRegister";
import { routerPush } from "../router";
import { ElMessage } from "element-plus";

export default {
  name: "Register",
  setup() {
    const formRef = ref(null);
    const registerSuccess = ref(false);

    const form = reactive({
      first_name: "",
      email: "",
      password: "",
    });
    const rules = reactive({
      first_name: [
        { required: true, message: "Please input your name", trigger: "blur" },
      ],
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
        {
          min: 6,
          message: "Please lengthen this text to 6 characters or more",
        },
      ],
    });

    const register = async () => {
      formRef.value?.validate(async (valid) => {
        if (!valid) {
          ElMessage.error("Please check your information.");
        }
        const result = await postRegister(form);
        if (result.status === "ok") {
          registerSuccess.value = true;
        } else {
          ElMessage.error("Error, please try again!");
        }
      });
    };

    const gotoPageLogin = async () => await routerPush("login");

    return { formRef, rules, form, register, registerSuccess, gotoPageLogin };
  },
};
</script>
