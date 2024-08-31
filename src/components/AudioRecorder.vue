<template>
  <div>
    <button v-if="state === 'standby'" class="send-btn" @click="onStartRecord">
      <img :src="micSrc" alt="mic">
    </button>
    <button
      v-else-if="state === 'record'"
      class="send-btn"
      @click="onStopRecord"
    >
      <img :src="stopSrc" style="width: 35px;" alt="stop">
    </button>
    <div v-else-if="state === 'processing'" class="send-btn">
      <LoadingOutlined style="font-size: 35px;" />
    </div>
    <div v-else-if="state === 'error'" class="send-btn">
      <WarningOutlined style="font-size: 35px;"/>
    </div>
  </div>
</template>

<script setup lang="ts">
import { startRecording, stopRecording } from '@/features/domain/audioService'
import { ref, watch, computed } from 'vue'
import { useStore } from 'vuex'
import { LoadingOutlined, WarningOutlined } from '@ant-design/icons-vue'
import micSrc from '@/assets/icons/mic.svg'
import stopSrc from '@/assets/icons/stop-solid.svg'

// eslint-disable-next-line func-call-spacing, no-spaced-func
const emit = defineEmits<
  (event: 'input', value: string) => void
>()

const store = useStore()

const state = ref<'record'|'standby'|'processing'|'error'>('standby')

watch(computed(() => store.getters.transcription), () => {
  state.value = 'standby'
  emit('input', store.getters.transcription)
})

const stopWatch = ref<boolean>(false)

watch(computed(() => store.getters.transcriptionError), () => {
  if (stopWatch.value) return

  state.value = 'error'
  stopWatch.value = true
  setTimeout(() => {
    state.value = 'standby'
    store.dispatch('transcriptionError', '')
    stopWatch.value = true
  }, 1500)
  // emit('input', store.getters.transcription)
})

const onStartRecord = () => {
  startRecording().then(() => {
    state.value = 'record'
  })
}

const onStopRecord = () => {
  state.value = 'processing'
  stopRecording()
}

</script>

<style lang="scss" scoped>
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
