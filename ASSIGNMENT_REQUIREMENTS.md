# DSA 2020A: Multi-Agent AI System - Lab 2 Assignment Requirements

## 📋 Assignment Overview

**Course:** DSA 2020A: Artificial Intelligence  
**Assignment:** Lab 2 - Building a Multi-Agent AI System for Real-World Applications  
**Group Size:** Individual or Pairs (pairs strongly encouraged)  
**Estimated Time:** 2 lab sessions  
**Total Points:** 100

---

## 🎯 Learning Objectives

By completing this assignment, you will be able to:

1. ✅ Understand motivation, benefits, and challenges of multi-agent systems vs single-agent
2. ✅ Design specialized roles for multiple AI agents collaborating toward a shared goal
3. ✅ Implement multi-agent architecture using open-source frameworks
4. ✅ Handle inter-agent handoffs, shared memory/state, conflict resolution, termination
5. ✅ Integrate tools/APIs and incorporate human-in-the-loop oversight
6. ✅ Reflect on ethical considerations, reliability, and real-world applicability
7. ✅ Evaluate agent team performance and identify coordination bottlenecks

---

## 💡 Core Concept

Modern AI applications increasingly rely on **multi-agent systems (MAS)** - teams of specialized agents that:
- Divide labor efficiently
- Critique each other's outputs
- Iterate collaboratively
- Achieve more complex, reliable outcomes than a single generalist agent

This lab shifts from building ONE autonomous agent to designing an **agent team** that mirrors real organizational division of labor.

---

## 🏢 Use Case Options (Choose ONE)

You must select ONE domain and implement it as a **collaborative multi-agent workflow**.  
All options require **at least 3-5 specialized agents** working together under orchestration.

### Option 1: Customer Care Team ⭐ SELECTED IN YOUR PROJECT

**Goal:** Handle complex customer inquiries end-to-end (beyond simple Q&A)

**Typical Agents:**
- 🎯 Greeter / Intent Classifier
- 🔍 Researcher / Knowledge Retriever (searches company docs/FAQ/web)
- 💬 Empath / Tone Adapter
- ⚡ Resolver / Action Taker (e.g., refund via API, schedule callback)
- 🆘 Escalator / Human Handoff Coordinator
- ✅ Quality Reviewer (post-resolution critique)

**Your Implementation (USIU Student Support):**
- ✅ Query Router Agent (Intent Classifier)
- ✅ Knowledge Retriever Agent (Researcher)
- ✅ Response Generator Agent (Resolver)
- ✅ Supervisor Agent (Orchestrator + Quality Control)

---

### Option 2: Healthcare Advisory Team

**Goal:** Interactive symptom/discussion assistant (with strong disclaimers: not medical advice)

**Typical Agents:**
- Intake / History Collector
- Symptom Analyst / Differential Diagnoser
- Evidence Gatherer (searches reliable sources)
- Risk & Safety Checker (flags red flags, ensures disclaimers)
- Recommendation Formatter & Educator
- Follow-up Planner

---

### Option 3: Personalized Education / Tutoring Team

**Goal:** Adaptive tutor for a chosen subject (e.g., Python, algebra, history)

**Typical Agents:**
- Curriculum Planner
- Concept Explainer
- Quiz / Assessment Generator
- Feedback Analyzer & Misconception Detector
- Motivator / Engagement Booster
- Progress Tracker & Report Generator

---

### Option 4: Personal Finance Assistant Team

**Goal:** Help users create/manage budgets, analyze spending, suggest optimizations

**Typical Agents:**
- Data Ingestion / Categorizer (parses user input/transactions)
- Budget Forecaster / Calculator
- Expense Pattern Detector
- Savings & Investment Advisor
- Risk & Compliance Checker
- Summary & Visualization Generator

---

### Option 5: Entertainment Recommendation & Curation Team

**Goal:** Build rich, personalized entertainment plans (movies, series, music, books, games)

**Typical Agents:**
- Preference Profiler / Conversation Guide
- Content Researcher / Metadata Gatherer
- Taste Matcher / Similarity Engine
- Diversity & Serendipity Curator
- Schedule / Plan Builder
- Feedback Learner & Refiner

---

## 🔧 Required Technical Elements (ALL Options)

### Framework Selection (Pick ONE)

You **must use** one of these open-source multi-agent frameworks:

| Framework | Difficulty | Best For | Recommendation |
|-----------|------------|----------|----------------|
| **LangGraph** | Advanced | Hierarchical/supervisor pattern, excellent state control | Strongly recommended |
| **CrewAI** | Beginner | Role/task-centric workflows | Easiest for beginners ⭐ |
| **Microsoft AutoGen** | Medium | Conversational style | Good for dialogue |
| **OpenAI Swarm** | Beginner | Lightweight experimentation | Good for prototyping |

---

### Minimum Implementation Requirements

Your system **MUST** implement ALL of the following:

#### ✅ 1. Supervisor/Orchestrator Agent
- Decides which agent acts next
- Determines when to stop
- Decides when to ask human for input
- Coordinates overall workflow

#### ✅ 2. 3-5 Specialized Worker Agents
- Each with **distinct roles** and **specific prompts**
- Clear division of labor
- No overlap in responsibilities

#### ✅ 3. Shared State/Memory
Must track and maintain:
- Query history
- Findings from each agent
- User profile/context
- Intermediate results
- Conversation flow

#### ✅ 4. Tool Integration (Minimum 2-3 Tools)
Examples:
- Web search (Tavily, DuckDuckGo, Google)
- Calculator / Code execution
- File read/write
- Database queries
- API calls (calendar, email, etc.)
- JSON knowledge base (like your project)

#### ✅ 5. Human-in-the-Loop Capability
- Pause for approval on sensitive actions/plans
- Allow user intervention
- Request clarification when needed
- Feedback mechanisms (👍 👎)

#### ✅ 6. Reflection/Critique Loop
- At least ONE agent critiques outputs before final delivery
- Quality assurance step
- Error checking
- Validation logic

#### ✅ 7. Streaming of Agent Thoughts/Actions
- Visibility into what each agent is doing
- Real-time progress indicators
- Transparent decision-making process

#### ✅ 8. Termination Conditions
At least ONE of:
- Goal achieved
- Maximum turns reached
- User stop command
- Error threshold exceeded
- Confidence score met

---

## 📦 Deliverables

### 1. GitHub Repository (Primary Deliverable)

Your repository **MUST** contain:

#### Required Files:
```
your-project/
├── README.md                    # Comprehensive documentation
├── requirements.txt             # All dependencies with versions
├── main.py / notebook.ipynb     # Main implementation
├── agents/                      # Agent definitions (optional folder)
├── tools/                       # Custom tools (optional folder)
├── knowledge/                   # Knowledge base (if applicable)
├── .env.example                 # Environment variable template
└── screenshots/                 # Demo screenshots
```

#### README.md Must Include:

**a) Chosen Use Case & Rationale (1-2 paragraphs)**
- Why did you choose this domain?
- What real-world problem does it solve?
- Who are the target users?

**b) Agent Team Diagram**
- Text or image showing:
  - Each agent's role
  - Communication flow between agents
  - Decision points
  - Handoff logic

Example:
```
User Query
    ↓
Supervisor Agent
    ↓
  ┌─┴─┐
  ↓   ↓
Router  → Knowledge Retriever → Response Generator
  ↓                                      ↓
Back to Supervisor ← Quality Check ← Response
  ↓
User
```

**c) How to Run**
Step-by-step instructions including:
- Prerequisites (Python version, etc.)
- Installation commands
- Environment variable setup (LLM provider API keys)
- Execution commands
- Expected output

**d) 2-3 Example Interaction Transcripts**
Show actual conversations demonstrating:
- Agent collaboration
- Handoffs between agents
- Tool usage
- Final output quality

**e) Key Challenges & Solutions**
Document at least 3 challenges:
- **Coordination issues:** How agents worked together
- **Hallucinations:** If LLM generated incorrect info
- **Infinite loops:** If agents got stuck
- **Cost management:** API usage optimization
- **Your solutions:** How you solved each

---

### 2. Demo (Jupyter Notebook + Screenshots)

**Requirements:**
- Show the team handling a **realistic user scenario**
- Include screenshots of:
  - Agent interactions
  - Tool usage
  - Final outputs
- Demonstrate all agents working together
- Show at least one human-in-the-loop interaction

**Acceptable Formats:**
- Jupyter Notebook (.ipynb) with embedded outputs
- Streamlit app with screenshots
- Command-line demo with screenshots
- Video recording (optional but impressive)

---

### 3. Reflection Report (2-3 Paragraphs)

**Main Question:**
*"What advantages did the multi-agent approach provide vs. a hypothetical single agent?"*

**Your reflection should cover:**

**Paragraph 1: Advantages**
- What could multiple agents do that one agent couldn't?
- How did specialization help?
- What emergent behaviors did you observe?

**Paragraph 2: Challenges & Learnings**
- What was harder than expected?
- How did you debug multi-agent coordination?
- What would you do differently?

**Paragraph 3: Real-World Applicability**
- Could this system be deployed in production?
- What ethical considerations arose?
- What improvements would make it production-ready?

---

## 📊 Grading Rubric (100 Points Total)

### 🏆 Point Breakdown

| Criteria | Points | What We're Looking For |
|----------|--------|------------------------|
| **Clear role specialization & meaningful division of labor** | 20 | • Each agent has distinct, non-overlapping role<br>• Division of labor makes sense<br>• Not just one agent doing everything |
| **Effective orchestration / supervisor logic** | 20 | • Supervisor makes intelligent routing decisions<br>• Proper handoffs between agents<br>• Clear termination conditions<br>• Error handling |
| **Tool use & integration across agents** | 15 | • At least 2-3 tools integrated<br>• Tools actually used by agents<br>• Proper error handling for tool failures |
| **Shared state/memory & inter-agent coordination** | 15 | • Agents share context/findings<br>• Conversation history maintained<br>• No information loss between agents |
| **Human-in-the-loop & safety/reflection mechanisms** | 10 | • User can intervene when needed<br>• Quality checks before final output<br>• Safety guardrails (especially for sensitive domains) |
| **Code quality, structure, documentation** | 10 | • Clean, readable code<br>• Proper comments<br>• Good project structure<br>• Type hints (Python) |
| **Demo quality** | 5 | • Clear demonstration of system working<br>• Realistic scenario<br>• Shows all agents collaborating |
| **Depth of reflection & insight** | 5 | • Thoughtful analysis of multi-agent vs single-agent<br>• Honest about challenges<br>• Evidence of learning |

---

## ✅ Quality Checklist

Before submitting, verify:

### Code Quality
- [ ] All code runs without errors
- [ ] Dependencies listed in requirements.txt with versions
- [ ] No hardcoded API keys (use .env)
- [ ] Proper error handling
- [ ] Comments explain complex logic
- [ ] Type hints used (for Python)

### Multi-Agent Implementation
- [ ] At least 3-5 specialized agents
- [ ] Clear supervisor/orchestrator
- [ ] Agents have distinct roles
- [ ] Shared memory/state implemented
- [ ] At least 2-3 tools integrated
- [ ] Human-in-the-loop capability present
- [ ] Termination conditions defined

### Documentation
- [ ] README.md is comprehensive
- [ ] Agent diagram included
- [ ] How-to-run instructions clear
- [ ] Example interactions provided
- [ ] Challenges & solutions documented
- [ ] Reflection report complete (2-3 paragraphs)

### Demo
- [ ] Shows realistic user scenario
- [ ] All agents collaborate
- [ ] Tools are used
- [ ] Final output is high quality
- [ ] Screenshots/notebook included

---

## 🎓 Your Project Status

### ✅ What You Already Have (USIU Chatbot)

Your current implementation **already meets** most requirements:

| Requirement | Status | Implementation |
|-------------|--------|----------------|
| Use Case | ✅ Done | Customer Care Team (Student Support) |
| Framework | ✅ Done | Custom multi-agent (similar to CrewAI pattern) |
| Supervisor Agent | ✅ Done | SupervisorAgent class |
| 3-5 Worker Agents | ✅ Done | Router, Retriever, Generator (+ Supervisor = 4) |
| Shared State | ✅ Done | conversation_history in Supervisor |
| Tool Integration | ✅ Done | JSON knowledge base (8 files = 1 tool) |
| Human-in-the-Loop | ✅ Done | Feedback buttons (👍 👎) |
| Termination | ✅ Done | Single response per query |
| Code Quality | ✅ Done | Clean, documented, type hints |
| Demo | ✅ Done | Streamlit interface + demo.py |

---

### 🔧 What You Need to Add/Enhance

To achieve **100/100**, consider adding:

#### 1. More Tools (Currently 1/3 required)
Add 2 more tools:
- ✅ JSON knowledge base (done)
- ➕ Web search (for questions beyond knowledge base)
- ➕ Email/notification system (for complex queries)

**Quick wins:**
```python
# Add web search fallback
from tavily import TavilyClient

def search_web(query):
    client = TavilyClient(api_key="free_tier")
    return client.search(query)
```

#### 2. Enhanced Reflection/Critique Loop
Add explicit quality checking:
```python
class QualityReviewerAgent:
    def review(self, response):
        # Check for completeness
        # Verify contact info included
        # Flag if response too vague
        return score, feedback
```

#### 3. Stronger Agent Diagram
Create visual diagram showing:
```
┌─────────────┐
│   User      │
└──────┬──────┘
       ↓
┌──────────────────────┐
│  Supervisor Agent    │
│  (Orchestrator)      │
└──────┬───────────────┘
       ↓
   ┌───┴───┐
   ↓       ↓
┌──────┐ ┌─────────┐
│Router│→│Retriever│
└──────┘ └────┬────┘
              ↓
        ┌──────────┐
        │Generator │
        └────┬─────┘
             ↓
      ┌───────────┐
      │Quality    │
      │Reviewer   │
      └─────┬─────┘
            ↓
       Final Response
```

#### 4. Example Interaction Transcripts
Add to README:
```markdown
### Example 1: Fees Query

**User:** "What are the fees for nursing?"

**Agent Flow:**
1. Router: Categorized as "fees_financial"
2. Retriever: Found data in all_programs_fees_2025_2026.json
3. Generator: Formatted response with KES amounts
4. Supervisor: Validated completeness, returned to user

**Response:** [Full formatted response]
```

#### 5. Challenges & Solutions Section
Document real issues you faced:
```markdown
### Challenge 1: Knowledge File Loading
**Problem:** JSON files not loading on first run
**Solution:** Added existence check + error handling

### Challenge 2: Response Consistency  
**Problem:** Some queries returned generic responses
**Solution:** Enhanced category matching with weighted keywords
```

---

## 📚 Recommended Resources

### Multi-Agent Frameworks
- **LangGraph:** [Multi-agent tutorials](https://python.langchain.com/docs/langgraph)
- **CrewAI:** [Quickstart guide](https://docs.crewai.com)
- **AutoGen:** [Conversational notebooks](https://microsoft.github.io/autogen)
- **DeepLearning.AI:** "Multi AI Agent Systems with crewAI" (free course)

### Tools & APIs
- **Web Search:** Tavily, DuckDuckGo Search, Google Custom Search
- **Knowledge:** JSON, SQLite, ChromaDB, Pinecone
- **Code Execution:** Python REPL, Jupyter kernels
- **Communication:** Email APIs, SMS, Calendar

### Ethical AI Guidelines
- Transparency in AI decision-making
- Data privacy and security
- Bias detection and mitigation
- Clear disclaimers (especially for health/finance)
- Human oversight for critical decisions

---

## 🎯 Success Criteria

Your project is **ready to submit** when:

✅ All 8 minimum technical requirements implemented  
✅ Code runs without errors for others  
✅ README is comprehensive and clear  
✅ Agent roles are specialized and distinct  
✅ Demo shows realistic end-to-end workflow  
✅ Reflection shows depth of understanding  
✅ Repository is well-organized and professional  

---

## 💡 Pro Tips

### For Maximum Points:

1. **Make Agent Specialization Crystal Clear**
   - Each agent should have ONE job
   - No overlapping responsibilities
   - Document WHY each agent exists

2. **Show, Don't Tell**
   - Include actual transcripts
   - Add screenshots
   - Demonstrate agents collaborating

3. **Be Honest in Reflection**
   - Professors value honesty over perfection
   - Discuss what didn't work
   - Show what you learned

4. **Think Production-Ready**
   - Error handling everywhere
   - Graceful degradation
   - Security considerations

5. **Document Everything**
   - Why you made each design choice
   - How agents coordinate
   - What challenges you overcame

---

## 🆘 Common Pitfalls to Avoid

❌ **Fake Multi-Agent:** One agent doing everything, others are decorative  
✅ **Real Multi-Agent:** Clear handoffs, each agent adds unique value

❌ **No Shared State:** Agents can't access previous findings  
✅ **Proper Memory:** Agents build on each other's work

❌ **Infinite Loops:** Agents keep calling each other forever  
✅ **Clear Termination:** Max turns, goal achieved, confidence threshold

❌ **No Human Control:** System runs autonomously without oversight  
✅ **Human-in-Loop:** User can intervene, approve, or stop

❌ **Poor Documentation:** "Just run main.py"  
✅ **Clear Instructions:** Step-by-step with explanations

---

## 📅 Suggested Timeline (2 Lab Sessions)

### Session 1 (Week 1)
- [ ] Choose use case
- [ ] Design agent architecture
- [ ] Set up project structure
- [ ] Implement basic agents
- [ ] Test individual agents

### Session 2 (Week 2)
- [ ] Implement orchestration
- [ ] Add tools/APIs
- [ ] Test full system
- [ ] Create demo
- [ ] Write documentation
- [ ] Write reflection

---

## 🎓 Final Checklist

Before submission, confirm:

- [ ] GitHub repository is public (or accessible to instructor)
- [ ] README.md is complete with all sections
- [ ] requirements.txt has all dependencies
- [ ] Code runs on fresh Python environment
- [ ] Demo clearly shows multi-agent collaboration
- [ ] Reflection is thoughtful (2-3 paragraphs)
- [ ] Agent diagram is included
- [ ] Example transcripts are provided
- [ ] Challenges & solutions documented
- [ ] All agents have distinct roles
- [ ] Shared state/memory works
- [ ] At least 2-3 tools integrated
- [ ] Human-in-the-loop present
- [ ] Termination conditions clear

---

## 📞 Questions?

If anything is unclear:
1. Review the assignment PDF again
2. Check recommended resources
3. Look at example multi-agent repos on GitHub
4. Ask instructor during lab sessions

---

**Good luck! 🚀**

Remember: The goal is to understand multi-agent coordination, not to build perfect software. Show your learning, document your process, and reflect thoughtfully.

---

**Assignment:** DSA 2020A Lab 2  
**Topic:** Multi-Agent AI Systems  
**Due Date:**   
**Submission:** GitHub repository link  

---

*This document is based on the official DSA 2020A Lab 2 Assignment requirements.*
