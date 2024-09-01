<!-- eslint-disable max-len -->
<!-- eslint-disable vuejs-accessibility/click-events-have-key-events -->
<template>
  <div @click="redirect" class="sider-btn" :class="{'unfocused': router.currentRoute.value.path !== to}">
    <div class="sider-btn__icon">
      <img :src="iconPath" alt="si">
    </div>
    <span :class="[
      'additional-text',
    ]"
    >
      {{ text }}
    </span>
    <div class="layer"></div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const props = defineProps<{
  iconPath: string,
  text?: string,
  to: string
}>()

const router = useRouter()

const redirect = () => {
  router.push(props.to)
}
</script>

<style scoped lang="scss">
.unfocused {
  opacity: .4;
}

.sider-btn {
  width: 100%;
  height: 68px;
  display: flex;
  align-items: center;
  margin-bottom: 24px;

  :not(.layer) {
    z-index: 1;
  }

  &__icon {
    margin-left: 14px;
    min-width: 36px;
    max-width: 36px;
  }

  &:hover {
    cursor: pointer;
    opacity: 1;

    .layer {
      width: 336px;
    }
  }
}

.additional-text {
  color: black;
  font-size: 24px;
  margin-left: 38px;
  white-space: nowrap;
}

.layer {
  position: absolute;
  width: 68px;
  height: 68px;
  border-radius: 34px;
  background-color: rgba($color: #fff, $alpha: .3);
  transition: width linear .2s;
  box-shadow: 0px 0px 15px 0px rgba(34, 60, 80, 0.2);
}
</style>
