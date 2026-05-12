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