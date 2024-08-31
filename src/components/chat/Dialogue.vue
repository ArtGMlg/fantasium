<template>
  <div class="dialogue">
    <Outcoming msg-text="Lorem ipsum?" />
    <Incoming msg-audio="" msg-pic="" msg-text="Lorem ipsum..."/>
  </div>
</template>

<script setup lang="ts">
import Incoming from './Incoming.vue'
import Outcoming from './Outcoming.vue'

</script>

<style scoped lang="scss">
.dialogue {
  min-height: calc(100% - 64px - 44px - 40px);
  max-height: calc(100% - 64px - 44px - 40px);
  height: calc(100% - 64px - 44px - 40px);
  align-content: end;
  margin: 20px 0;
}
</style>
