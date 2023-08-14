<template>
  <div id="clock">
    <div class="px-3">
        <div class="clock-part">{{ day }}.</div>
        <div class="clock-part">{{ month }}.</div>
        <div class="clock-part">{{ year }}</div>
    </div>
    <div>
        <div class="clock-part">{{ hour }}:</div>
        <div class="clock-part">{{ minutes }}:</div>
        <div class="clock-part">{{ seconds }}</div>
    </div>
  </div>
</template>

<script>
export default {
    name: "Clock",
    data() {
        return {
            hour: 0,
            minutes: 0,
            seconds: 0,
            year: 0,
            month: 0,
            day: 0
        }
    },
    methods: {
        setClock() {
            const date = new Date()
            this.hour = this.renderTwoDigits(date.getHours())
            this.minutes = this.renderTwoDigits(date.getMinutes())
            this.seconds = this.renderTwoDigits(date.getSeconds())
            this.year = date.getFullYear()
            this.month = this.renderTwoDigits(date.getMonth() + 1)
            this.day = this.renderTwoDigits(date.getDate())
        },
        renderTwoDigits(digit) {
            return ( '0' + digit ).slice(-2)
        }
    },
    mounted() {
        this.setClock()
        setInterval(this.setClock, 1000)
    }
}
</script>

<style>
    #clock {
        margin: 5px;
        display: flex;
        justify-content: end;
        font-size: 1.5rem;
        font-weight: bold;
        color: rgb(220, 220, 220);
    }

    .clock-part {
        display: inline-block;
    }
</style>