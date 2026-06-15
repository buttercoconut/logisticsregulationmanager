<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script setup>
// No script needed for root
</script>

<style>
/* Global styles */
body {
  margin: 0;
  font-family: Arial, sans-serif;
}
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
</style>
