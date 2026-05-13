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
