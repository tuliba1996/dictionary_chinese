<template>
  <el-dialog :title="props.title" v-model="props.dialogVisible" center>
    <slot />
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="props.onToggle">Cancel</el-button>
        <el-button type="primary" @click="props.onSubmitForm"
          >Confirm</el-button
        >
      </span>
    </template>
  </el-dialog>
</template>

<script>
export default {
  name: "Modal",
  props: {
    title: { type: String },
    dialogVisible: { type: Boolean },
    onToggle: { type: Function, required: true },
    onSubmitForm: { type: Function, required: true },
  },
  setup(props, { attrs }) {
    return {
      props,
      attrs,
    };
  },
};
</script>
