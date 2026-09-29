<template>
  <section class="page">
    <header class="page-head">
      <div>
        <h2>运营概览</h2>
        <p class="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
      </div>
    </header>
    <div class="stat-row">
      <article v-for="card in cards" :key="card.label" class="stat-card">
        <span class="stat-label">{{ card.label }}</span>
        <strong class="stat-value">{{ card.value }}</strong>
      </article>
    </div>
    <table class="data-table">
      <thead>
        <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
      </thead>
      <tbody>
        <tr v-for="row in moduleRows" :key="row.name">
          <td>{{ row.name }}</td>
          <td>{{ row.created }}</td>
          <td>{{ row.pending }}</td>
          <td>{{ row.abnormal }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const cards = ref<Overview['cards']>([])
const moduleRows = ref<Overview['modules']>([])

onMounted(async () => {
  try {
    const payload = await fetchJson<Overview>('/api/overview')
    cards.value = payload.cards
    moduleRows.value = payload.modules
  } catch {
    cards.value = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
    moduleRows.value = [{"name": "变电站管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "输电线路", "created": 0, "pending": 0, "abnormal": 0}, {"name": "线路巡检", "created": 0, "pending": 0, "abnormal": 0}, {"name": "停电计划", "created": 0, "pending": 0, "abnormal": 0}, {"name": "负荷监测", "created": 0, "pending": 0, "abnormal": 0}, {"name": "倒闸操作", "created": 0, "pending": 0, "abnormal": 0}, {"name": "事故预案", "created": 0, "pending": 0, "abnormal": 0}, {"name": "消缺管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "工作票管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "继电保护", "created": 0, "pending": 0, "abnormal": 0}, {"name": "直流电源", "created": 0, "pending": 0, "abnormal": 0}, {"name": "关口计量", "created": 0, "pending": 0, "abnormal": 0}, {"name": "调度日志", "created": 0, "pending": 0, "abnormal": 0}, {"name": "接地线管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "承载力管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "安全工器具", "created": 0, "pending": 0, "abnormal": 0}]
  }
})
</script>
