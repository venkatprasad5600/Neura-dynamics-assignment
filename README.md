# Prompt Engineering & RAG Mini Project
AI Engineer Intern – Take-Home Assignment (Neura Dynamics)

## Overview
This project implements a **lightweight Retrieval-Augmented Generation (RAG) system** for answering questions grounded strictly in company policy documents (e.g., Refund, Cancellation, Shipping policies).

The focus of this assignment is **not model complexity**, but:
- Prompt quality and iteration
- Reliable retrieval and grounding
- Hallucination avoidance
- Clear reasoning and evaluation

The system is implemented as a **Python-based CLI/script**, intentionally kept simple to emphasize clarity and decision-making.

---

## Problem Statement
Given a set of company policy documents, build a question-answering assistant that:
- Retrieves relevant information from documents
- Generates accurate, grounded answers
- Avoids hallucinations
- Handles missing or out-of-scope questions gracefully

---

## Architecture Overview
User Query
↓
Text Embedding
↓
Vector Store (FAISS / Chroma)
↓
Top-k Semantic Retrieval
↓
Prompt + Retrieved Context
↓
LLM Response (Grounded Answer)


### Key Components
- **Embedding Model**: Sentence-level embeddings for semantic search
- **Vector Store**: FAISS / Chroma for fast similarity search
- **LLM**: OpenAI / open-source LLM for answer generation
- **Prompt Layer**: Carefully designed instructions to constrain behavior

---

## Data Preparation

### Document Loading
- Supported formats: PDF / TXT / Markdown
- Text extracted using standard Python loaders

### Chunking Strategy
- **Chunk size**: ~500 tokens  
- **Overlap**: ~50 tokens

**Reasoning**:
- Large enough to preserve policy context
- Small enough for precise retrieval
- Overlap helps avoid boundary information loss

---

## RAG Pipeline Implementation

1. Load and preprocess documents
2. Generate embeddings for each chunk
3. Store embeddings in a vector database
4. Retrieve top-k relevant chunks for a query
5. Inject retrieved context into the prompt
6. Generate an answer strictly from retrieved text

---

## Result 
**Question**  
What is the refund policy for cancelled orders?

**Retrieved Context (excerpt)**  
Customers are eligible for a full refund if the order is cancelled within 7 days of purchase and the item has not been shipped.

**Model Answer**
- Customers can receive a full refund if they cancel within 7 days of purchase.
- Refunds are not applicable once the item has been shipped.

**Evaluation**: ✅ Accurate and grounded

**Question**  
Does the company offer discounts for bulk purchases?

**Retrieved Context**  
No relevant policy information found.

**Model Answer**
The provided documents do not contain information related to bulk purchase discounts.

**Evaluation**: ✅ Correctly declined without hallucination
