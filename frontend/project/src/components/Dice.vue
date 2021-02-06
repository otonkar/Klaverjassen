<template>
  <div class="Appdice">

    <div id="dice">
      <div class="side front">
        <div class="dot center"></div>
      </div>
      <div class="side front inner"></div>
      <div class="side top">
        <div class="dot dtop dleft"></div>
        <div class="dot dbottom dright"></div>
      </div>
      <div class="side top inner"></div>
      <div class="side right">
        <div class="dot dtop dleft"></div>
        <div class="dot center"></div>
        <div class="dot dbottom dright"></div>
      </div>
      <div class="side right inner"></div>
      <div class="side left">
        <div class="dot dtop dleft"></div>
        <div class="dot dtop dright"></div>
        <div class="dot dbottom dleft"></div>
        <div class="dot dbottom dright"></div>
      </div>
      <div class="side left inner"></div>
      <div class="side bottom">
        <div class="dot center"></div>
        <div class="dot dtop dleft"></div>
        <div class="dot dtop dright"></div>
        <div class="dot dbottom dleft"></div>
        <div class="dot dbottom dright"></div>
      </div>
      <div class="side bottom inner"></div>
      <div class="side back">
        <div class="dot dtop dleft"></div>
        <div class="dot dtop dright"></div>
        <div class="dot dbottom dleft"></div>
        <div class="dot dbottom dright"></div>
        <div class="dot center dleft"></div>
        <div class="dot center dright"></div>
      </div>
      <div class="side back inner"></div>
      <div class="side cover x"></div>
      <div class="side cover y"></div>
      <div class="side cover z"></div>
    </div>

  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Appdice',
  test: 0,
  data () {
    return {
      test: {},
    }
  },

  activated: async function () {

  },//END activated

  methods: {

    doSleep: async function (ms) {
          // To wait some time. Use in a async function
          return new Promise(resolve => setTimeout(resolve, ms));
        }, //END doSleep


  },  //END methods

}
</script>

<style scoped lang='scss'>

// #dice  {
//     position:absolute;
//     margin:0px 0 0 0px;
//     display: block;
//     font-size: 2.5em;
//     padding: 10px;
// }


#dice {
    // position: absolute;
    width: 200px;
    height: 200px;
    margin: 0px;
    padding: 0px;
    transform-style: preserve-3d;
		/* animation: spin 50s infinite linear; */
		/* transform: rotateX(-900deg) rotateZ(1080deg); */
		// transform: rotateX(0deg )rotateY(0deg) rotateZ(0deg) ;
		// transform: rotateX(-0deg) rotateY(0deg) rotateZ(0deg) scale3d(0.5, 0.5, 0.5) translate(-100px, -100px);
		// transition: transform 2s; 
    // transform-origin: -0px 0px;
}

.side {
    position: absolute;
    width: 200px;
    height: 200px;
    background: #fff;
    box-shadow:inset 0 0 40px #ccc;
    border-radius: 40px;
}
#dice .cover, #dice .inner {
    background: #e0e0e0;
    box-shadow: none;
}
#dice .cover {
    border-radius: 0;
    transform: translateZ(0px);
}
#dice .cover.x {
    transform: rotateY(90deg);
}
#dice .cover.z {
    transform: rotateX(90deg);
}
#dice .front  {
    transform: translateZ(100px);
}
#dice .front.inner  {
    transform: translateZ(98px);
}
#dice .back {
    transform: rotateX(-180deg) translateZ(100px);
}
#dice .back.inner {
    transform: rotateX(-180deg) translateZ(98px);
}
#dice .right {
    transform: rotateY(90deg) translateZ(100px);
}
#dice .right.inner {
    transform: rotateY(90deg) translateZ(98px);
}
#dice .left {
    transform: rotateY(-90deg) translateZ(100px);
}
#dice .left.inner {
    transform: rotateY(-90deg) translateZ(98px);
}
#dice .top {
    transform: rotateX(90deg) translateZ(100px);
}
#dice .top.inner {
    transform: rotateX(90deg) translateZ(98px);
}
#dice .bottom {
    transform: rotateX(-90deg) translateZ(100px);
}
#dice .bottom.inner {
    transform: rotateX(-90deg) translateZ(98px);
}
.dot {
    position:absolute;
    width:46px;
    height:46px;
    border-radius:23px;
    // background:#444;
    // box-shadow:inset 5px 0 10px #000;
    background: black;
	  background: radial-gradient(circle at 16px 16px, #5cabff, #000);
}
.dot.center {
    margin:77px 0 0 77px;
}
.dot.dtop {
    margin-top:20px;
}
.dot.dleft {
    margin-left:134px;
}
.dot.dright {
    margin-left:20px;
}
.dot.dbottom {
    margin-top:134px;
}
.dot.center.dleft {
    margin:77px 0 0 20px;
}
.dot.center.dright {
    margin:77px 0 0 134px;
}



</style>
