<!-- eslint-disable vuejs-accessibility/click-events-have-key-events -->
<!-- eslint-disable vuejs-accessibility/media-has-caption -->
<template>
  <div class="in-message">
    <div v-if="msgText">
      <div class="in-message__pic">
        <img v-if="msgPic" :src="'data: image/png;base64,' + msgPic" alt="illustration">
      </div>
      <div class="in-message__text">{{ msgText }}</div>
      <div class="in-message__audio hover:cursor-pointer" @click="play">
        <i class="pi pi-volume-up"></i>
      </div>
      <audio ref="audio" :src="'data:audio/wav;base64,' + msgAudio"></audio>
    </div>
    <template v-else>
      <LoadingAnimation />
      <div class="in-message__text">Создаем историю...</div>
    </template>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import LoadingAnimation from './loadingAnimation/LoadingAnimation.vue'

defineProps<{
  msgPic: string
  msgText: string
  msgAudio: string
}>()

const audio = ref<HTMLAudioElement | null>(null)
const playing = ref<boolean>(false)

const play = () => {
  if (!playing.value) {
    playing.value = true
    audio.value?.play().then(() => {
      playing.value = false
    })
  } else {
    audio.value?.pause()
  }
}
</script>

<style scoped lang="scss">
.in-message {
  width: fit-content;
  padding: 24px;
  max-width: 50%;
  background-color: #e5e5e5;
  margin-right: auto;
  border-radius: 32px;
  position: relative;

  &__text {
    line-height: normal;
    margin-top: 20px;
    text-align: start;
  }

  &__audio {
    width: 66px;
    height: 66px;
    border-radius: 33px;
    background-color: #FFDD2D;
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    right: -20px;
    bottom: -20px;

    .pi {
      font-size: 28px;
    }
  }
}
</style>
