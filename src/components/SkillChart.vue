<template>
    <svg width="200" height="200">
        <g>
            <polygon :points="points"></polygon>
            <circle cx="100" cy="100" r="80"></circle>
            <skill-chart-label
                v-for="(stat, index) in stats"
                :stat="stat"
                :index="index"
                :total="stats.length">
            </skill-chart-label>
        </g>
    </svg>
</template>

 <script>
 import SkillChartLabel from './SkillChartLabel';

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
    props: ['character',],
    computed: {
        largestStat(){
            return Math.max(...[ this.character.strength,
                this.character.dexterity,
                this.character.constitution,
                this.character.intelligence,
                this.character.charisma,
                this.character.wisdom,
            ])
        },
        stats(){
            return [
                { label: 'Str', value: (this.character.strength / this.largestStat) * 100},
                { label: 'Dex', value: (this.character.dexterity / this.largestStat) * 100},
                { label: 'Con', value: (this.character.constitution / this.largestStat) * 100},
                { label: 'Int', value: (this.character.intelligence / this.largestStat) * 100},
                { label: 'Cha', value: (this.character.charisma / this.largestStat) * 100},
                { label: 'Wis', value: (this.character.wisdom / this.largestStat) * 100}
            ]
        },

        points(){
            let total = this.stats.length
            return this.stats.map(function (stat, i) {
                let point = valueToPoint(stat.value, i, total)
                return point.x + ',' + point.y
            }).join(' ')
        }
    },
    components: {
        SkillChartLabel,
    }
 }
 </script>

 <style lang="scss" scoped>
    @import '../variables';
     polygon {
         fill: $secondary-cool;
         opacity: .75;
     }

     circle {
         fill: transparent;
         stroke: #999;
     }

     text {
         font-family: Helvetica Neue, Arial, sans-serif;
         font-size: 10px;
         fill: #666;
     }

     label {
         display: inline-block;
         margin-left: 10px;
         width: 20px;
     }
 </style>
