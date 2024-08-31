<template>
  <div class="flex items-center">
    <a-input :style="inputStyle" v-model="msg"></a-input>
    <send-btn @get-voice="sendMessage" @send="sendMessage"></send-btn>
  </div>
</template>

<script setup lang="ts">
import { ref, type CSSProperties } from 'vue'
import SendBtn from './SendBtn.vue'

const inputStyle: CSSProperties = {
  height: '77px',
  borderRadius: '35px',
  marginRight: '28px',
}

const msg = ref<string>('')

const sendMessage = (text: string | null) => {
  if (!text) {
    // TODO отправка msg на эндпоинт генерации
  } else {
    // TODo отправка text на эндпоинт генерации
  }
}
</script>

<style scoped>

</style>
