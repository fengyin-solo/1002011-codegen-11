<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">电网调度运行管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向变电站设备、线路巡检、停电计划、负荷监测、倒闸操作与事故预案的一体化电网调度运行管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "变电站管理", path: "/substation" }, { label: "输电线路", path: "/line" }, { label: "线路巡检", path: "/inspection" }, { label: "停电计划", path: "/outage" }, { label: "负荷监测", path: "/load" }, { label: "倒闸操作", path: "/switchop" }, { label: "事故预案", path: "/emergency" }, { label: "消缺管理", path: "/repair" }, { label: "工作票管理", path: "/workpermit" }, { label: "继电保护", path: "/protect" }, { label: "直流电源", path: "/battery" }, { label: "关口计量", path: "/meter" }, { label: "调度日志", path: "/dispatchlog" }, { label: "接地线管理", path: "/grounding" }, { label: "承载力管理", path: "/capacity" }, { label: "安全工器具", path: "/tool" }]
</script>
