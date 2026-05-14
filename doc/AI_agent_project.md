## AI项目与传统项目最大的区别

**传统项目：**
```angular2html
输入 -> 固定逻辑 -> 输出
```

**AI项目：**

```angular2html
输入
 ↓
LLM推理
 ↓
动态规划
 ↓
工具选择
 ↓
上下文构建
 ↓
多轮推理
 ↓
输出
```

核心不再是：
```angular2html
类设计
CRUD
ORM
```

而是：
```angular2html
Context Engineering
Reasoning Flow
Agent State
Tool Ecosystem
Workflow Design
```

这是完全不同的开发哲学。

### Agent Runtime

Agent = LLM + State + Tools + Loop

**普通Chat:**
```angular2html
用户输入
  ↓
LLM
  ↓
输出
```

**Agent:**
```angular2html
用户输入
  ↓
LLM思考
  ↓
决定是否调用工具
  ↓
执行工具
  ↓
获得结果
  ↓
再次思考
  ↓
继续调用工具
  ↓
最终输出
```

## Workflow Orchestration —— LangGraph 的核心思想
初级的Demo中，往往会使用`while True:`循环，来完成一个任务。这种Agent Loop结构有一个很严重的问题就是不可控。另外真实的复杂任务很难用单循环完成。

在LangGraph升级中，引入了Multi-Agent架构，通过多个Agent协同工作，来完成复杂任务。每个Node(阶段)基本对应一个Agent，Agent会根据输入，进行思考，然后选择调用工具，然后调用工具，然后获得结果。

已经非常接近Multi-Agent Orchestrator的结构。但是当前的`state`是共享的，所有Agent使用的同一个state。这样会导致上下文混乱（`Context Pollution`）和内容量的增长。

因此需要进行上下文隔离（`Context Isolation`）。

想要让Agent更加智能，下一步引入`RAG`。

## RAG & Knowledge System Engineering

Agent 的外部认知系统

RAG不是简单的搜索，而是上下文构造

```python
results = await retriever.retrieve(
    query
)

context = "\n\n".join([
    chunk.content
    for _, chunk in results
])

prompt = f"""
Use the following context:

{context}

Question:
{query}
"""
```

## Memory System Engineering

**Agent 的认知架构核心**

Prompt： 决定当前行为

Memory： 决定长期认知

真正工业级 Agent：

必须能够：

 - 记住过去
 - 形成经验
 - 压缩知识
 - 检索历史
 - 建立长期状态

## Reflection & Self-Improvement Architecture

会反思的 Agent

## Observability & AI Runtime Monitoring —— AI 系统的可观测性工程

因为大模型本身是“黑盒”系统，所以需要引入可观测性。

## Reliability Engineering for AI Systems —— AI 系统稳定性工程

LLM本质是一个概率系统，相同的输入可能导致不同的输出，
这会导致：
|问题         |后果|
|---          |--|
|随机失败       |不可预测|
|Tool失败      |Workflow中断|
|输出漂移       |不稳定|
|超时          |Runtime阻塞|
|hallucination|错误结果|
|token暴涨     |成本失控|

因此AI系统相比较传统系统更加脆弱。

工业系统最重要的是：**可靠性**

可靠性不是指retry,失败了就多试几次。
而是包含多个维度：

| 维度             | 内容   |
| -------------- | ---- |
| Recovery       | 自动恢复 |
| Isolation      | 故障隔离 |
| Degradation    | 优雅退化 |
| Observability  | 可监控  |
| Predictability | 可预测  |
| Stability      | 长期稳定 |



构建基础版块：
Reliability Runtime V1
包括：
 - Retry Policy
 - Timeout
 - Fallback Model： 降级执行
 - Circuit Breaker： 熔断器。 失败太多-> 暂时禁止调用
 - Failure Recovery

## AI Middleware & Runtime Pipeline Architecture —— AI Runtime 中间件体系

随着模型的构建，Runtime会越来越大，越来越复杂：
```angular2html
trace
retry
timeout
reflection
memory
cache
guardrail
rate limit
cost control
```
如果全部放进`run()`函数，函数会非常臃肿，且不易扩展，需要升级成**Pipeline Architecture**

Pipeline本质是一组顺序执行的Runtime阶段,例如：
```angular2html
trace
 ↓
retry
 ↓
timeout
 ↓
reflection
 ↓
execute
```

## Durable Execution & Checkpoint Runtime —— 持久化 AI Runtime

AI Workflow越来越长周期，需要Durable(持久化)。

使得Runtime可以从崩溃中快速恢复。

现代工业中通过Temporal 、Airflow 、Dagster 、Ray解决。

Temporal的核心思想认为，Workflow是客回复状态机。
```angular2html
WorkflowGraph
    ↓
WorkflowExecutor
    ↓
DurableRuntime
    ↓
WorkerRuntime
```
