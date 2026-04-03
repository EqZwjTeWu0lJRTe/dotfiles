---
name: obsidian-structure-manager
description: This skill assists in managing Obsidian vault file structures using Claude's reasoning capabilities and MCP tools for intelligent note classification, structural analysis, rule refinement, and folder optimization. The skill should be used when users need help organizing their Obsidian notes, analyzing folder structure health, extracting classification rules, cleaning inbox folders, or performing folder-level fine-grained operations.
---

# Obsidian Structure Manager

## Overview

This skill provides a comprehensive framework for managing Obsidian vault file structures through intelligent note classification, structural analysis, and folder optimization. It combines Claude's natural language understanding with MCP tools to create a dynamic entropy reduction system that maintains knowledge base structural health.

Based on the theoretical framework of "Intelligent Note Classification System", this skill implements a state-driven approach where the knowledge base state `K_t = (A_t, R_t, Θ_t)` is continuously optimized toward an "cognitively friendly" equilibrium state.

## Core Capabilities

### 1. Intelligent Classification Assistant
**Trigger phrase**: `/智能分类 [note path or content]`

**Function**: Analyzes specific notes and provides intelligent classification suggestions or automatically executes move operations.

**Processing workflow**:
1. **Note analysis**: Reads note content, extracts title, core themes, content type
2. **Semantic matching**: Calculates semantic similarity between note and existing folders
3. **Decision logic**:
   - If match degree >80% → Suggests movement and executes automatically (requires confirmation)
   - If all match degrees <30% → Suggests creating new folder
   - Otherwise → Provides candidate folder list for selection
4. **Rule update**: Automatically optimizes semantic rules for corresponding folders based on classification results

**MCP tools required**:
- `read_note`: Reads note content
- `list_notes`: Gets existing folder structure
- `move_note`: Executes note movement
- `create_note`: Creates new folder (if needed)

### 2. Structural Health Analysis
**Trigger phrase**: `/结构分析`

**Function**: Analyzes the health status of the entire Obsidian vault's folder structure.

**Evaluation metrics**:
1. **Folder size distribution**: Identifies folders that are too large (>50 notes) or too small (<5 notes)
2. **Naming clarity**: Evaluates semantic clarity of folder names
3. **Content overlap**: Calculates semantic similarity between folders to identify redundancy
4. **Classification ambiguity**: Statistics on proportion of ambiguously classified notes

**Optimization suggestions**:
- Split large folders
- Merge highly similar folders
- Rename ambiguous folders
- Redistribute notes to balance structure

**MCP tools required**:
- `list_notes`: Gets complete folder structure
- `read_multiple_notes`: Samples and reads folder content for analysis
- `search_vault`: Searches for related notes

### 3. Rule Extraction and Optimization
**Trigger phrase**: `/规则提炼 [folder path]`

**Function**: Analyzes specified folder content to extract classification rules and optimize them.

**Analysis dimensions**:
1. **Naming system analysis**: Evaluates folder naming and internal note naming patterns
2. **Content feature extraction**: Identifies core themes, high-frequency vocabulary, content type distribution
3. **Three-fold rule extraction**:
   - Inclusion rules: Content that should be placed in this folder
   - Exclusion rules: Content that should not be placed in this folder
   - Naming standards: Recommended note naming standards
4. **Boundary case identification**: Identifies characteristics of difficult-to-classify notes

**MCP tools required**:
- `read_note`: Reads notes within folder
- `list_notes`: Gets folder content list
- `update_note`: Updates folder documentation

### 4. Inbox Cleaning Assistant
**Trigger phrase**: `/清理inbox`

**Function**: Automatically processes unclassified notes in the inbox folder.

**Processing logic**:
1. Scans all notes in the inbox folder
2. Performs intelligent classification analysis on each note
3. Executes classification operations in batch
4. Generates cleaning report

**MCP tools required**:
- `list_notes`: Gets inbox content
- `read_note`: Reads note content
- `move_note`: Moves notes to target folders

### 5. Folder Fine-grained Operations
**Trigger phrase**: `/文件夹操作 [operation type] [parameters]`

**Function**: Executes fine-grained operations at folder level.

**Supported operations**:
1. **Split**: Divides large folders into multiple subfolders by theme
2. **Merge**: Combines multiple semantically similar folders
3. **Rename**: Optimizes folder names to improve clarity
4. **Hierarchy adjustment**: Optimizes folder hierarchy structure
5. **Create index**: Creates index notes for folders

**MCP tools required**:
- `manage_folder`: Creates, renames, moves folders
- `move_note`: Batch moves notes
- `create_note`: Creates index documents

### 6. System Status Monitoring
**Trigger phrase**: `/系统状态`

**Function**: Monitors knowledge base health indicators and provides system status reports.

**Monitoring metrics**:
- Overall knowledge base health `H(K_t)`
- Dimensional indicators: `φ_模糊`, `φ_重叠`, `φ_失衡`, `φ_僵化`
- System parameters `Θ_t` status
- Recent classification accuracy rate

## Implementation Workflow

### System State Definition
The skill operates based on the theoretical framework defined in "Intelligent Note Classification System":
- `K_t = (A_t, R_t, Θ_t)`: Complete state of knowledge base at time t
  - `A_t`: Note-folder membership matrix
  - `R_t`: Folder rule set (regular expressions defining semantic boundaries)
  - `Θ_t`: System dynamic parameter set (determines scoring and decision behavior)

### Core Mechanisms
- **Scoring function**: `S(N, F_i) = f(文本特征(N), 语义规则(R_i), 结构上下文(A_t); Θ_t)`
- **Health function**: `H(K_t) = g(φ_模糊, φ_重叠, φ_失衡, φ_僵化)`

### Decision Logic
1. **Automatic classification**: If `∃F_max` such that `s_max > θ_high`, execute `classify(N, F_max)`
2. **Suggest new folder**: If `∀F_i, s_i < θ_low`, execute `new_folder(F_new)` and `classify(N, F_new)`
3. **Suggest confirmation**: Otherwise, propose candidate set `C = {F_i | s_i ≥ θ_mid}` for user selection

## Practical Examples

### Example 1: New Note Classification
```
User: /智能分类 inbox/新项目想法.md
Claude:
1. Reads note content, analyzes theme as "机器学习项目规划"
2. Calculates match degree with existing folders:
   - 领域/AI/机器学习: 85%
   - 项目/进行中: 60%
   - 想法/技术灵感: 45%
3. Suggestion: Move to "领域/AI/机器学习"
4. Executes move operation and updates folder rules
```

### Example 2: Structural Optimization
```
User: /结构分析
Claude:
1. Analyzes full vault structure, discovers:
   - "领域/技术" folder is too large (120 notes)
   - "工具/软件" and "工具/应用" highly overlap (similarity 75%)
2. Suggestions:
   - Split "领域/技术" into subfolders
   - Merge "工具/软件" and "工具/应用"
3. Provides detailed operation steps
```

### Example 3: Rule Extraction
```
User: /规则提炼 领域/AI
Claude:
1. Analyzes "领域/AI" folder content (45 notes)
2. Extracts core themes: machine learning, deep learning, natural language processing, computer vision
3. Establishes rules:
   - Include: AI-related technologies, algorithms, application cases
   - Exclude: general programming, software engineering, hardware technology
4. Provides naming standard suggestions
```

## System Advantages

1. **Theory-guided practice**: Based on rigorous theoretical framework, ensuring system design rationality
2. **Intelligent self-adaptation**: Optimizes classification rules through feedback learning, adapting to user habits
3. **Automated operations**: Uses MCP tools to implement one-click file management
4. **Fine-grained control**: Supports folder-level fine-grained operations
5. **Health monitoring**: Continuously monitors knowledge base structure health, preventing structural deterioration
6. **Ease of use**: Completes complex operations through natural language commands

## Implementation Suggestions

### Short-term implementation (immediate start):
1. Implement basic classification functionality (Module A)
2. Implement Inbox cleaning functionality (Module D)
3. Create system status monitoring (Module F)

### Medium-term expansion (1-2 weeks):
1. Complete structural analysis functionality (Module B)
2. Implement rule extraction functionality (Module C)
3. Optimize user interaction experience

### Long-term optimization (1 month):
1. Implement folder fine-grained operations (Module E)
2. Integrate feedback learning mechanism
3. Develop advanced analysis functionality

---

**System Vision**: Builds an intelligent collaborative system that can understand user thinking habits, automatically maintain knowledge base structure, and continuously optimize classification rules, truly achieving the ideal knowledge management state of "unordered during creation, ordered during retrieval".