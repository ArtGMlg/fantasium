<template>
  <div class="chat">
    <Dialogue :dialogue="history" />
    <MessageInput @input="onInput" />
  </div>
</template>

<script setup lang="ts">
import { uniqueId } from '@/reusable/functions'
import { useStore } from 'vuex'
import { ref } from 'vue'
import { generateService } from '@/init/services'
import { ChatMessage } from '@/store'
import Dialogue from './Dialogue.vue'
import MessageInput from './MessageInput.vue'

const store = useStore()

const history = ref<Record<string, ChatMessage>>({})

const chatId: string = localStorage.getItem('chatId') ?? uniqueId()
if (!localStorage.getItem('chatId')) {
  localStorage.setItem('chatId', chatId)
}
store.dispatch('setChatId', chatId)

const onInput = (value: string) => {
  const outMsgId = uniqueId()
  const inMsgId = uniqueId()

  history.value[outMsgId] = {
    type: 'outcoming',
    content: value,
  }

  history.value[inMsgId] = {
    type: 'incoming',
    content: '',
    voiceover: '',
    illustration: '',
  }

  generateService.generate({
    chatId,
    message: value,
  })
    .then((response) => {
      history.value[inMsgId].content = response.content
      history.value[inMsgId].voiceover = response.voiceover
    })

  generateService.getIllustration({
    chatId,
    message: value,
  })
    .then((response) => {
      history.value[inMsgId].illustration = response.image
    })
}
</script>

<style scoped lang="scss">
.chat {
  margin: 0 32px 0 28px;
  height: calc(100% - 20px);
}
</style>
