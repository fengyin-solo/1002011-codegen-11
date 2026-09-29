# 电网调度运行管理平台

面向变电站设备、线路巡检、停电计划、负荷监测、倒闸操作与事故预案的一体化电网调度运行管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 变电站管理 | `substation` | 变电站 | 站号、站名、电压等级 |
| 输电线路 | `line` | 输电线路 | 线路编号、线路名称、起点站 |
| 线路巡检 | `inspection` | 巡检任务 | 任务编号、巡检线路、巡检方式 |
| 停电计划 | `outage` | 停电计划单 | 计划编号、停电范围、停电类型 |
| 负荷监测 | `load` | 负荷监测点 | 监测点编号、所属变电站、监测对象 |
| 倒闸操作 | `switchop` | 操作票 | 操作票编号、操作任务、发令人 |
| 事故预案 | `emergency` | 应急预案 | 预案编号、预案名称、适用站线 |
| 消缺管理 | `repair` | 缺陷记录 | 缺陷编号、所属设备、缺陷类别 |
| 工作票管理 | `workpermit` | 工作票 | 工作票编号、工作内容、工作班组 |
| 继电保护 | `protect` | 保护装置 | 装置编号、装置型号、所属间隔 |
| 直流电源 | `battery` | 直流系统 | 系统编号、所属站、蓄电池组型号 |
| 关口计量 | `meter` | 计量点 | 计量点编号、所属线路、电能表型号 |
| 调度日志 | `dispatchlog` | 调度日志 | 日志编号、值班人、交接班时间 |
| 接地线管理 | `grounding` | 接地线 | 接地线编号、适用电压等级、存放位置 |
| 承载力管理 | `capacity` | 承载力分析 | 分析编号、分析时段、分析区域 |
| 安全工器具 | `tool` | 安全工器具 | 器具编号、器具名称、器具类别 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
