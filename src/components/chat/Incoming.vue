<template>
  <div class="in-message">
    <div class="in-message__pic">
      <img :src="msgPic" alt="illustration">
    </div>
    <div class="in-message__text">{{ msgText }}</div>
    <div class="in-message__audio"></div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  msgPic: string
  msgText: string
  msgAudio: string
}>()
</script>

<style scoped lang="scss">
.in-message {
  width: fit-content;
  padding: 24px;
  max-width: 50%;
  background-color: #e5e5e5;
  margin-right: auto;
  border-radius: 32px;

  &__text {
    line-height: normal;
  }
}
</style>
