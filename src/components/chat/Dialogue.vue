<template>
  <div class="dialogue" id="diaBounder" ref="dia">
    <template v-for="(msg, i) in dialogue">
      <Outcoming
        v-if="msg.type === 'outcoming'"
        :key="'in' + i"
        :msg-text="msg.content" />
      <Incoming
        v-else-if="msg.type === 'incoming'"
        :key="'out' + i"
        :msg-pic="msg.illustration || ''"
        :msg-audio="msg.voiceover || ''"
        :msg-text="msg.content" />
    </template>

  </div>
</template>

<script setup lang="ts">
import { ChatMessage } from '@/store'
import { ref, watch, nextTick } from 'vue'
import Incoming from './Incoming.vue'
import Outcoming from './Outcoming.vue'

const dia = ref<HTMLElement>()

const props = defineProps<{
  dialogue: Record<string, ChatMessage>
}>()

watch(() => props.dialogue, () => {
  const el = document.getElementById('diaBounder')
  if (el) {
    nextTick(() => {
      el.scrollTop = el.scrollHeight
    })
  }
}, {
  deep: true,
})
</script>

<style scoped lang="scss">
.dialogue {
  min-height: calc(100% - 64px - 44px - 40px);
  max-height: calc(100% - 64px - 44px - 40px);
  height: calc(100% - 64px - 44px - 40px);
  align-content: end;
  margin: 20px 0;
  overflow: auto;
}
</style>
