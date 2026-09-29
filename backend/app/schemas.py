"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class SubstationEntry(BaseModel):
    """变电站明细结构。"""

    field_0: str | None = None  # 站号
    field_1: str | None = None  # 站名
    field_2: str | None = None  # 电压等级
    field_3: str | None = None  # 主变台数
    field_4: str | None = None  # 投运日期
    field_5: str | None = None  # 所属区域
    field_6: str | None = None  # 运维班组
    field_7: str | None = None  # 运行状态

class LineEntry(BaseModel):
    """输电线路明细结构。"""

    field_0: str | None = None  # 线路编号
    field_1: str | None = None  # 线路名称
    field_2: str | None = None  # 起点站
    field_3: str | None = None  # 终点站
    field_4: str | None = None  # 导线型号
    field_5: str | None = None  # 线路长度
    field_6: str | None = None  # 投运日期
    field_7: str | None = None  # 线路状态

class InspectionEntry(BaseModel):
    """巡检任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 巡检线路
    field_2: str | None = None  # 巡检方式
    field_3: str | None = None  # 巡检人员
    field_4: str | None = None  # 计划日期
    field_5: str | None = None  # 完成日期
    field_6: str | None = None  # 缺陷数量
    field_7: str | None = None  # 任务状态

class OutageEntry(BaseModel):
    """停电计划单明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 停电范围
    field_2: str | None = None  # 停电类型
    field_3: str | None = None  # 计划开始时间
    field_4: str | None = None  # 计划结束时间
    field_5: str | None = None  # 影响户数
    field_6: str | None = None  # 审批人
    field_7: str | None = None  # 计划状态

class LoadEntry(BaseModel):
    """负荷监测点明细结构。"""

    field_0: str | None = None  # 监测点编号
    field_1: str | None = None  # 所属变电站
    field_2: str | None = None  # 监测对象
    field_3: str | None = None  # 额定容量
    field_4: str | None = None  # 当前负荷
    field_5: str | None = None  # 负载率
    field_6: str | None = None  # 越限阈值
    field_7: str | None = None  # 监测状态

class SwitchopEntry(BaseModel):
    """操作票明细结构。"""

    field_0: str | None = None  # 操作票编号
    field_1: str | None = None  # 操作任务
    field_2: str | None = None  # 发令人
    field_3: str | None = None  # 操作人
    field_4: str | None = None  # 监护人
    field_5: str | None = None  # 操作开始时间
    field_6: str | None = None  # 操作结束时间
    field_7: str | None = None  # 操作状态

class EmergencyEntry(BaseModel):
    """应急预案明细结构。"""

    field_0: str | None = None  # 预案编号
    field_1: str | None = None  # 预案名称
    field_2: str | None = None  # 适用站线
    field_3: str | None = None  # 事故类型
    field_4: str | None = None  # 编制日期
    field_5: str | None = None  # 修订日期
    field_6: str | None = None  # 编制人
    field_7: str | None = None  # 预案状态

class RepairEntry(BaseModel):
    """缺陷记录明细结构。"""

    field_0: str | None = None  # 缺陷编号
    field_1: str | None = None  # 所属设备
    field_2: str | None = None  # 缺陷类别
    field_3: str | None = None  # 发现时间
    field_4: str | None = None  # 消缺时限
    field_5: str | None = None  # 消缺人员
    field_6: str | None = None  # 处理措施
    field_7: str | None = None  # 消缺状态

class WorkpermitEntry(BaseModel):
    """工作票明细结构。"""

    field_0: str | None = None  # 工作票编号
    field_1: str | None = None  # 工作内容
    field_2: str | None = None  # 工作班组
    field_3: str | None = None  # 许可人
    field_4: str | None = None  # 签发人
    field_5: str | None = None  # 许可时间
    field_6: str | None = None  # 终结时间
    field_7: str | None = None  # 工作状态

class ProtectEntry(BaseModel):
    """保护装置明细结构。"""

    field_0: str | None = None  # 装置编号
    field_1: str | None = None  # 装置型号
    field_2: str | None = None  # 所属间隔
    field_3: str | None = None  # 保护类型
    field_4: str | None = None  # 投运日期
    field_5: str | None = None  # 定值版本
    field_6: str | None = None  # 校验周期
    field_7: str | None = None  # 装置状态

class BatteryEntry(BaseModel):
    """直流系统明细结构。"""

    field_0: str | None = None  # 系统编号
    field_1: str | None = None  # 所属站
    field_2: str | None = None  # 蓄电池组型号
    field_3: str | None = None  # 电池节数
    field_4: str | None = None  # 浮充电压
    field_5: str | None = None  # 放电容量
    field_6: str | None = None  # 检验日期
    field_7: str | None = None  # 系统状态

class MeterEntry(BaseModel):
    """计量点明细结构。"""

    field_0: str | None = None  # 计量点编号
    field_1: str | None = None  # 所属线路
    field_2: str | None = None  # 电能表型号
    field_3: str | None = None  # 互感器变比
    field_4: str | None = None  # 上次校验日期
    field_5: str | None = None  # 计量方向
    field_6: str | None = None  # 管理人员
    field_7: str | None = None  # 计量状态

class DispatchlogEntry(BaseModel):
    """调度日志明细结构。"""

    field_0: str | None = None  # 日志编号
    field_1: str | None = None  # 值班人
    field_2: str | None = None  # 交接班时间
    field_3: str | None = None  # 当值期间操作摘要
    field_4: str | None = None  # 遗留问题
    field_5: str | None = None  # 气象条件
    field_6: str | None = None  # 接班人员
    field_7: str | None = None  # 记录状态

class GroundingEntry(BaseModel):
    """接地线明细结构。"""

    field_0: str | None = None  # 接地线编号
    field_1: str | None = None  # 适用电压等级
    field_2: str | None = None  # 存放位置
    field_3: str | None = None  # 检验日期
    field_4: str | None = None  # 下次检验日期
    field_5: str | None = None  # 领用人
    field_6: str | None = None  # 使用地点
    field_7: str | None = None  # 使用状态

class CapacityEntry(BaseModel):
    """承载力分析明细结构。"""

    field_0: str | None = None  # 分析编号
    field_1: str | None = None  # 分析时段
    field_2: str | None = None  # 分析区域
    field_3: str | None = None  # 同时最大负荷
    field_4: str | None = None  # 可开放容量
    field_5: str | None = None  # 受限设备
    field_6: str | None = None  # 分析人
    field_7: str | None = None  # 分析状态

class ToolEntry(BaseModel):
    """安全工器具明细结构。"""

    field_0: str | None = None  # 器具编号
    field_1: str | None = None  # 器具名称
    field_2: str | None = None  # 器具类别
    field_3: str | None = None  # 规格型号
    field_4: str | None = None  # 存放地点
    field_5: str | None = None  # 上次试验日期
    field_6: str | None = None  # 下次试验日期
    field_7: str | None = None  # 器具状态
