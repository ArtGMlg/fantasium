<template>
  <div class="sider-btn">
    <div class="sider-btn__icon">
      <img :src="iconPath" alt="si">
    </div>
    <span :class="[
      'additional-text',
      {
        'additional-text__show': siderHovered
      }
    ]"
    >
      {{ text }}
    </span>
    <div class="layer"></div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  siderHovered: boolean,
  iconPath: string,
  text?: string
}>()
</script>

<style scoped lang="scss">
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
  }

  &:hover {
    cursor: pointer;

    .layer {
      width: 336px;
    }
  }
}

.additional-text {
  color: black;
  font-size: 24px;
  margin-left: 38px;
  display: none;

  &__show {
    display: initial;
  }
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
