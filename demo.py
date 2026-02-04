"""
Demo Script - Test USIU Chatbot Multi-Agent System
Run this to verify the system is working correctly
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from src.agents.multi_agent_system import SupervisorAgent

def print_separator():
    print("\n" + "="*70 + "\n")

def test_chatbot():
    """Test the chatbot with various queries"""
    
    print("🎓 USIU-Africa Student Support Chatbot - Demo")
    print_separator()
    
    # Initialize supervisor
    print("📋 Initializing Multi-Agent System...")
    supervisor = SupervisorAgent(knowledge_dir="knowledge")
    print("✅ System initialized successfully!")
    print(f"📚 Knowledge files loaded: {len(supervisor.retriever.cache)}")
    print_separator()
    
    # Test queries
    test_queries = [
        "What are the fees for nursing?",
        "How do I pay via M-Pesa?",
        "What is the minimum GPA required?",
        "Where is the library?",
        "What are the library hours?",
        "Tell me about scholarships",
        "What are the rules about alcohol?",
        "How do I contact the finance office?"
    ]
    
    print("🧪 Testing Multi-Agent System with Sample Queries\n")
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n{'─'*70}")
        print(f"Query {i}: {query}")
        print(f"{'─'*70}\n")
        
        try:
            # Process query
            result = supervisor.process_query(query)
            
            # Display results
            print(f"📂 Category: {result['category']}")
            print(f"📚 Sources: {', '.join(result['sources'][:3]) if result['sources'] else 'None'}")
            print(f"\n💬 Response:\n{result['response'][:500]}...")  # First 500 chars
            
        except Exception as e:
            print(f"❌ Error: {e}")
        
        if i < len(test_queries):
            input("\n⏎ Press Enter to continue to next query...")
    
    print_separator()
    print("✅ Demo completed successfully!")
    print("\n🚀 Next Steps:")
    print("  1. Start the backend: uvicorn backend.api:app --reload")
    print("  2. Start the frontend: streamlit run frontend/streamlit_app.py")
    print("  3. Open browser: http://localhost:8501")
    print_separator()

def test_knowledge_base():
    """Test knowledge base loading"""
    
    print("🔍 Testing Knowledge Base Loading")
    print_separator()
    
    from src.agents.multi_agent_system import KnowledgeRetrieverAgent
    
    retriever = KnowledgeRetrieverAgent(knowledge_dir="knowledge")
    
    print(f"✅ Loaded {len(retriever.cache)} knowledge files:\n")
    
    for filename, data in retriever.cache.items():
        if isinstance(data, dict):
            keys = list(data.keys())[:5]
            print(f"  📄 {filename}")
            print(f"     → Top-level keys: {', '.join(keys)}")
            print()
    
    print_separator()

def test_agents():
    """Test individual agents"""
    
    print("🤖 Testing Individual Agents")
    print_separator()
    
    from src.agents.multi_agent_system import (
        QueryRouterAgent,
        KnowledgeRetrieverAgent,
        ResponseGeneratorAgent
    )
    
    # Test Router
    print("1️⃣ Testing Query Router Agent")
    router = QueryRouterAgent()
    
    test_routing = [
        ("What are the fees?", "fees_financial"),
        ("Where is the library?", "facilities"),
        ("What is the GPA requirement?", "academic"),
        ("Tell me about counseling", "services")
    ]
    
    for query, expected in test_routing:
        category = router.route(query)
        status = "✅" if category == expected else "❌"
        print(f"  {status} '{query}' → {category}")
    
    print("\n2️⃣ Testing Knowledge Retriever Agent")
    retriever = KnowledgeRetrieverAgent(knowledge_dir="knowledge")
    results = retriever.retrieve("fees_financial", "nursing fees")
    print(f"  ✅ Retrieved {len(results)} relevant knowledge files")
    
    print("\n3️⃣ Testing Response Generator Agent")
    generator = ResponseGeneratorAgent()
    response = generator.generate(
        "What are the fees for nursing?",
        results,
        "fees_financial"
    )
    print(f"  ✅ Generated response (length: {len(response)} chars)")
    
    print_separator()

if __name__ == "__main__":
    print("\n" + "="*70)
    print(" "*15 + "🎓 USIU CHATBOT DEMO & TESTING")
    print("="*70 + "\n")
    
    try:
        # Run tests
        test_knowledge_base()
        test_agents()
        test_chatbot()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Demo interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Error running demo: {e}")
        import traceback
        traceback.print_exc()
