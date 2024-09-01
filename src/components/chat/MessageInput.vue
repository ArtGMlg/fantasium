<template>
  <div class="flex items-center">
    <a-input :style="inputStyle" v-model:value="msg"></a-input>
    <send-btn @get-voice="sendMessage" @send="sendMessage" :msg-empty="!msg"></send-btn>
  </div>
</template>

<script setup lang="ts">
import { ref, type CSSProperties } from 'vue'
import SendBtn from './SendBtn.vue'

const inputStyle: CSSProperties = {
  height: '77px',
  borderRadius: '35px',
  marginRight: '28px',
  fontSize: '16px',
}

// eslint-disable-next-line no-spaced-func, func-call-spacing
const emit = defineEmits<{
  (event: 'input', value: string): void
}>()

const msg = ref<string>('')

const sendMessage = (text: string | null) => {
  emit('input', text || msg.value)
  msg.value = ''
}
</script>

<style scoped>

</style>
