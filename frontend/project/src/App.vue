<template>
  <div id="app">
    <app-header></app-header>
    <!-- <router-view/> -->
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
  </div>
</template>


<script>
// import the components
import Appheader from './components/registration/Header.vue'

export default {
  name: 'app',
  components: {
    'app-header'    : Appheader
  },
  data () {
    return {
      title: 'Header'
    }
  },
  created() {
    this.getWindowSize()
    window.addEventListener("resize", this.getWindowSize);
  },
  methods: {
    getWindowSize: function () {
      this.window_size.width = window.innerWidth
      || document.documentElement.clientWidth
      || document.body.clientWidth;

      this.window_size.height = window.innerHeight
      || document.documentElement.clientHeight
      || document.body.clientHeight;

      // // console.log(this.window_size)

      this.$store.dispatch('updateWindow_size', this.window_size)

    },  //END GetWindowSize
  },
  // mounted: function () {
  //   // Force a full screen
  //   var elem = document.getElementById("app")
  //   if (elem.requestFullscreen) {
  //     elem.requestFullscreen();
  //   } else if (elem.mozRequestFullScreen) { /* Firefox */
  //     elem.mozRequestFullScreen();
  //   } else if (elem.webkitRequestFullscreen) { /* Chrome, Safari & Opera */
  //     elem.webkitRequestFullscreen();
  //   } else if (elem.msRequestFullscreen) { /* IE/Edge */
  //     elem.msRequestFullscreen();
  //   }
  // }
  computed: {
    window_size () {
      return this.$store.state.window_size
    }
  }
}
</script>

<style lang="scss">
body {
  background-color: rgb(173, 212, 183);
  // max-width: 900px;
  // margin: auto;
}
</style>
