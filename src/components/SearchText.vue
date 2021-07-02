<template>
  <div class="search-word">
    <div class="input-search">
      <el-autocomplete
        class="inline-input"
        v-model="searchText"
        :fetch-suggestions="querySearch"
        placeholder="Please Input"
        :trigger-on-focus="false"
        @select="handleSelectSearch"
        clearable
      >
      </el-autocomplete>
    </div>
    <div class="tran-container" v-if="show_tran">
      <div class="character-chinese">
        <span>{{ character.chinese }}</span>
        <div>
          <span>Pinyin: </span>
          <span>{{ character.pinyin }}</span>
        </div>
      </div>

      <div class="trans-vn">
        <span>Translate</span>
        <p>{{ character.vietnamese }}</p>
      </div>
    </div>
    <div class="hanzi-container">
      <div ref="char" id="character-target"></div>
      <el-button v-if="show_tran" @click="animateWord" type="primary"
        >Animate</el-button
      >
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { queryCharacter } from "../services/queryCharacter";
import HanziWriter from "hanzi-writer";
export default {
  name: "SearchText",

  setup() {
    const searchText = ref("");
    let writer = null;
    const char = ref(null);
    const show_tran = ref(false);
    const character = ref({});
    const querySearch = async (queryString, cb) => {
      if (queryString) {
        const results = await queryCharacter(queryString);
        const formatResults = results.data.map((c) => {
          return {
            ...c,
            value: `${c.chinese} - ${c.pinyin} - ${c.vietnamese}`,
          };
        });
        cb(formatResults);
      }
    };
    const handleSelectSearch = async (item) => {
      character.value = item;
      if (char.value.innerHTML) char.value.innerHTML = "";
      writer = await HanziWriter.create("character-target", item.chinese, {
        width: 350,
        height: 350,
        padding: 25,
        showOutline: true,
      });
      show_tran.value = true;
    };
    const animateWord = () => writer.animateCharacter();

    return {
      searchText,
      char,
      character,
      querySearch,
      show_tran,
      handleSelectSearch,
      animateWord,
    };
  },
};
</script>
