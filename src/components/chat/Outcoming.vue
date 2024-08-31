<template>
  <div class="out-message">
    <div class="out-message__text">{{ msgText }}</div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  msgText: string
}>()
</script>

<style scoped lang="scss">
.out-message {
  width: fit-content;
  padding: 24px;
  max-width: 50%;
  background-color: #e5e5e5;
  margin-left: auto;
  border-radius: 32px;

  &__text {
    line-height: normal;
  }
}
</style>
