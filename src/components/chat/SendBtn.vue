<template>
  <div>
    <AudioRecorder v-if="msgEmpty" @input="onInput" />
    <button v-else class="send-btn" @click="onSend">
      <img :src="sendSrc" alt="send">
    </button>
  </div>
</template>

<script setup lang="ts">
import sendSrc from '@/assets/icons/send.svg'
import AudioRecorder from '../AudioRecorder.vue'

// eslint-disable-next-line func-call-spacing, no-spaced-func
const emit = defineEmits<{
  (e: 'send', value: null): void
  (e: 'getVoice', value: string): void
}>()

const onInput = (value: string) => {
  emit('getVoice', value)
}

const onSend = () => {
  emit('send', null)
}

withDefaults(
  defineProps<{
    msgEmpty: boolean
  }>(),
  {
    msgEmpty: true,
  },
)
</script>

<style scoped lang="scss">
.send-btn {
  width: 88px;
  height: 88px;
  border-radius: 44px;
  background-color: #FFDD2D;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
