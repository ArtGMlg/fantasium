<template>
  <div class="chat">
    <Dialogue />
    <MessageInput />
  </div>
</template>

<script setup lang="ts">
import { uniqueId } from '@/reusable/functions'
import { useStore } from 'vuex'
import Dialogue from './Dialogue.vue'
import MessageInput from './MessageInput.vue'

const store = useStore()

if (localStorage.getItem('chatId')) {
  store.dispatch('setChatId', localStorage.getItem('chatId'))
} else {
  const id = uniqueId()
  localStorage.setItem('chatId', id)
  store.dispatch('setChatId', id)
}
</script>

<style scoped lang="scss">
.chat {
  margin: 0 32px 0 28px;
  height: calc(100% - 20px);
}
</style>
