<template>
    <div class="chart-container">
        <h3>{{title}}</h3>
        <div class="chart-wrap">
            <Pie :data="chartData" :options="chartOptions" />
            <span class="flex flex-column gap">
              <article v-for="(item, index) in chartData.datasets[0].data" :key="item">
                <span class="flex gap">
                  <label>{{ chartData.labels[index] }}:</label>
                  <i>{{ item }} ({{ calculatePercentage(item) }}%)</i>
                </span>
              </article>
              <article class="total">
                <span class="flex gap">
                  <label>Total:</label>
                  <i>{{ getTotal() }}</i>
                </span>
              </article>
            </span>
        </div>
      </div>
</template>

<script>
import { Pie } from 'vue-chartjs'
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'

ChartJS.register(ArcElement, Tooltip, Legend)

export default {
  name: 'PieChart',
  components: { Pie },
  props: {
    title: {
      type: String,
      required: true,
      default: ''
    },
    chartData: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false
      }
    }
  }, 
  methods: {
        getTotal() {
            return this.chartData.datasets[0].data.reduce((a, b) => a + b, 0);
        },
        calculatePercentage(value) {
            const total = this.getTotal();
            return total > 0 ? ((value / total) * 100).toFixed(2) : 0;
        },
    },
}
</script>

<style scoped>

.chart-container {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
}

h3{
    font-size: 1.5em;
    margin-left: 4em;
    color: #333;
}

.chart-wrap {
    position: relative;
    height: 300px;
    width: 400px;
    display: flex;
}
.chart-wrap > span {
    flex-direction: column;
    min-width: 12em;
}

.total {
    margin-top: 1em;
    font-weight: bold;
    border-top: 1px solid #eee;
    padding-top: 0.5em;
  }

</style>