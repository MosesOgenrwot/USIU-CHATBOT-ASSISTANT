"""
FastAPI Backend for USIU-Africa Student Support Chatbot
Multi-agent system integration with free LLM support
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.agents.multi_agent_system import SupervisorAgent

# Initialize FastAPI app
app = FastAPI(
    title="USIU-Africa Student Support API",
    description="Multi-agent chatbot system for student support",
    version="1.0.0"
)

# CORS middleware for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize supervisor agent
try:
    supervisor = SupervisorAgent(knowledge_dir="knowledge")
    print("✅ Supervisor agent initialized successfully")
except Exception as e:
    print(f"❌ Error initializing supervisor: {e}")
    supervisor = None


class QueryRequest(BaseModel):
    """Request model for chat queries"""
    question: str
    conversation_id: Optional[str] = None


class QueryResponse(BaseModel):
    """Response model for chat queries"""
    answer: str
    category: str
    sources: List[str]
    confidence: str = "high"


@app.get("/")
def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "service": "USIU-Africa Student Support API",
        "version": "1.0.0",
        "agents_active": supervisor is not None
    }


@app.get("/health")
def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "supervisor_initialized": supervisor is not None,
        "knowledge_base_loaded": supervisor is not None and len(supervisor.retriever.cache) > 0,
        "available_knowledge_files": list(supervisor.retriever.cache.keys()) if supervisor else []
    }


@app.post("/chat", response_model=QueryResponse)
def chat(request: QueryRequest):
    """
    Main chat endpoint - processes user queries through multi-agent system
    """
    try:
        if supervisor is None:
            raise HTTPException(
                status_code=500,
                detail="Supervisor agent not initialized"
            )
        
        if not request.question or request.question.strip() == "":
            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty"
            )
        
        # Process query through multi-agent system
        result = supervisor.process_query(request.question)
        
        return QueryResponse(
            answer=result["response"],
            category=result["category"],
            sources=result["sources"],
            confidence="high"
        )
    
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error processing query: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing query: {str(e)}"
        )


@app.get("/history")
def get_history():
    """Get conversation history"""
    if supervisor is None:
        return {"history": []}
    
    return {
        "history": supervisor.conversation_history[-10:]  # Last 10 conversations
    }


@app.post("/feedback")
def submit_feedback(feedback: Dict[str, Any]):
    """Submit feedback on responses"""
    # In production, this would store feedback for improvement
    return {
        "status": "received",
        "message": "Thank you for your feedback!"
    }


@app.get("/categories")
def get_categories():
    """Get available query categories"""
    if supervisor is None:
        return {"categories": []}
    
    return {
        "categories": list(supervisor.router.CATEGORIES.keys())
    }


@app.get("/knowledge-stats")
def knowledge_stats():
    """Get knowledge base statistics"""
    if supervisor is None or supervisor.retriever is None:
        return {"stats": {}}
    
    stats = {}
    for filename, data in supervisor.retriever.cache.items():
        if isinstance(data, dict):
            stats[filename] = {
                "loaded": True,
                "top_level_keys": list(data.keys())[:5]
            }
    
    return {"stats": stats}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
