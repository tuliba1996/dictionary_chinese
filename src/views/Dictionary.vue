<template>
  <div class="container">
    <div class="dictionary">
      <search-text/>
    </div>
  </div>

</template>

<script>
import SearchText from "../components/SearchText";
export default {
  name: "Dictionary",
  components: {
    SearchText
  }
};
</script>

