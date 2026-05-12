# InvestmentAgent
An investment agent for the OpenAI Gym.

技术路线采用 Python + LangGraph

## 第一阶段： Agent基础设施
### 1. LLM Client层
LLM Client层，基于LLM的API，提供LLM的调用接口。

### 2. Prompt Engineering
 - System Prompt设计
 - Tool Prompt
 - ReAct
 - Reflection
 - Self Critique
 - Planning Prompt

### 3. Tool Calling
**Agent系统的核心**

### 4. Agent Runtime
**AI系统的核心**
提供Agent运行时环境,标准化输入输出，控制Agent运行流程
包括：
 - State
 - Message
 - Memory
 - Event
 - Workflow
 - Retry
 - Streaming Event

#### Context Engineering
Agent的推理和思考能力依赖于上下文质量。上下文时一种有限的资源，且边际效应递减。
工业级的Context System结构如下：
```angular2html
┌─────────────────────┐
│ System Prompt       │
├─────────────────────┤
│ Short-term Memory   │
├─────────────────────┤
│ Long-term Memory    │
├─────────────────────┤
│ Retrieved Context   │
├─────────────────────┤
│ Recent Messages     │
├─────────────────────┤
│ Current User Input  │
└─────────────────────┘
```

`core/memory.py`中通过给消息评分，然后根据分数获取最重要的消息。这已经接近`RAG`的本质了。`RAG`的本质不是**向量数据库**，而是**从大量信息中选择最相关上下文**。
向量数据库是一种相关度查询的方式。


### 5. Memory系统

 - 短期记忆
 - 长期记忆
 - 向量记忆
 - 用户画像
 - Session State
