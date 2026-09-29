"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import substation as router_substation
from app.routers import line as router_line
from app.routers import inspection as router_inspection
from app.routers import outage as router_outage
from app.routers import load as router_load
from app.routers import switchop as router_switchop
from app.routers import emergency as router_emergency
from app.routers import repair as router_repair
from app.routers import workpermit as router_workpermit
from app.routers import protect as router_protect
from app.routers import battery as router_battery
from app.routers import meter as router_meter
from app.routers import dispatchlog as router_dispatchlog
from app.routers import grounding as router_grounding
from app.routers import capacity as router_capacity
from app.routers import tool as router_tool

ROUTERS = [router_substation, router_line, router_inspection, router_outage, router_load, router_switchop, router_emergency, router_repair, router_workpermit, router_protect, router_battery, router_meter, router_dispatchlog, router_grounding, router_capacity, router_tool]
