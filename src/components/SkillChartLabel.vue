<template>
      <text :x="point.x - 8" :y="point.y + 3">{{ stat.label }}</text>
</template>

 <script>

 function valueToPoint (value, index, total) {
     let x     = 0
     let y     = -value * 0.8
     let angle = Math.PI * 2 / total * index
     let cos   = Math.cos(angle)
     let sin   = Math.sin(angle)
     let tx    = x * cos - y * sin + 100
     let ty    = x * sin + y * cos + 100
     return {
         x: tx,
         y: ty
     }
 }

 export default {
     props: {
         stat: Object,
         index: Number,
         total: Number
     },
     computed: {
         point: function () {
             return valueToPoint(
                 +115,
                 this.index,
                 this.total
             )
         }
     }
 }
 </script>

 <style lang="scss" scoped>
    text {
        font-family: Helvetica Neue, Arial, sans-serif;
        font-size: 10px;
        fill: #666;
    }
 </style>
