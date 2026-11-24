# 90-Day AI Engineering Learning Plan

Built from the [roadmap.sh AI Engineer roadmap](https://roadmap.sh/ai-engineer), following its order: introduction → pre-trained models → APIs → prompting → safety → open-source → embeddings → vector databases → RAG → agents → multimodal. Newer roadmap topics (context engineering, MCP, evals, observability) are added where they fit. Each day builds on the one before.

Status: ✅ published · ⏳ next · ⬜ planned

## Phase 1: Foundations (Introduction)
| Day | Topic | Level |
|---|---|---|
| 1 | What is an AI Engineer? ✅ | Beginner |
| 2 | AI Engineer vs ML Engineer ⏳ | Beginner |
| 3 | Roles, responsibilities & impact on product development | Beginner |
| 4 | What is a Large Language Model (LLM)? | Beginner |
| 5 | How LLMs work: next-token prediction & transformers (high level) | Beginner |
| 6 | Tokens & tokenization | Beginner |
| 7 | The context window | Beginner |
| 8 | Training vs inference | Beginner |
| 9 | Embeddings (intro) | Beginner |
| 10 | Vector databases (intro) | Beginner |
| 11 | RAG (intro) | Beginner |
| 12 | Prompt engineering (intro) | Beginner |
| 13 | AI agents (intro) | Beginner |
| 14 | AI vs AGI + common terminology recap | Beginner |

## Phase 2: Using Pre-trained Models
| Day | Topic | Level |
|---|---|---|
| 15 | Pre-trained models: benefits & limitations | Beginner |
| 16 | The model landscape: OpenAI, Claude, Gemini, Llama, Mistral, DeepSeek, Qwen | Beginner |
| 17 | Choosing the right model: capabilities, context length, knowledge cut-off, cost | Beginner |
| 18 | OpenAI-compatible APIs & OpenRouter | Beginner |

## Phase 3: Working with LLM APIs
| Day | Topic | Level |
|---|---|---|
| 19 | Your first API call: OpenAI Responses API | Beginner |
| 20 | Claude Messages API | Beginner |
| 21 | Google Gemini API | Beginner |
| 22 | Sampling parameters: temperature | Beginner |
| 23 | Top-p & top-k | Intermediate |
| 24 | Max tokens, stop sequences & repetition penalties | Intermediate |
| 25 | Token counting & pricing | Intermediate |
| 26 | Streaming responses | Intermediate |
| 27 | Structured output (JSON schemas) | Intermediate |
| 28 | Prompt caching | Intermediate |

## Phase 4: Prompt Engineering
| Day | Topic | Level |
|---|---|---|
| 29 | System prompts, roles & behavior | Beginner |
| 30 | Zero-shot vs few-shot prompting | Beginner |
| 31 | Chain-of-thought prompting | Intermediate |
| 32 | ReAct prompting | Intermediate |
| 33 | Robust prompts: constraining inputs & outputs | Intermediate |

## Phase 5: Context Engineering
| Day | Topic | Level |
|---|---|---|
| 34 | Prompt engineering vs context engineering | Intermediate |
| 35 | Context sources, state & conversation history | Intermediate |
| 36 | Context failure modes | Intermediate |
| 37 | Context compaction & long-context processing | Intermediate |
| 38 | Memory systems & external memory | Intermediate |

## Phase 6: AI Safety & Security
| Day | Topic | Level |
|---|---|---|
| 39 | Prompt injection attacks | Intermediate |
| 40 | Bias & fairness | Intermediate |
| 41 | Security & privacy concerns | Intermediate |
| 42 | Content moderation APIs & end-user IDs | Intermediate |
| 43 | Adversarial testing (red teaming) | Intermediate |

## Phase 7: Open-Source AI
| Day | Topic | Level |
|---|---|---|
| 44 | Open vs closed models + Hugging Face Hub, models & tasks | Intermediate |
| 45 | Hugging Face Inference SDK | Intermediate |
| 46 | Transformers.js: models in the browser | Intermediate |
| 47 | Running models locally: Ollama & LM Studio | Intermediate |
| 48 | Self-hosting & inference engineering basics | Advanced |

## Phase 8: Embeddings
| Day | Topic | Level |
|---|---|---|
| 49 | Embeddings deep dive | Intermediate |
| 50 | Semantic search | Intermediate |
| 51 | Recommendations, anomaly detection & classification with embeddings | Intermediate |
| 52 | Embedding APIs (OpenAI, Gemini, Cohere, Jina) | Intermediate |
| 53 | Open-source embeddings: Sentence Transformers | Intermediate |

## Phase 9: Vector Databases
| Day | Topic | Level |
|---|---|---|
| 54 | Vector databases: purpose & functionality | Intermediate |
| 55 | Indexing embeddings & similarity search | Intermediate |
| 56 | Hands-on with Chroma | Intermediate |
| 57 | Comparing Pinecone, Qdrant, Weaviate, FAISS, pgvector (Supabase) | Intermediate |

## Phase 10: RAG
| Day | Topic | Level |
|---|---|---|
| 58 | RAG use cases & RAG vs fine-tuning | Intermediate |
| 59 | Chunking strategies | Intermediate |
| 60 | The retrieval process | Intermediate |
| 61 | Generation, grounding & citations | Intermediate |
| 62 | RAG with dynamic filters | Advanced |
| 63 | Build RAG from scratch with SDKs | Advanced |
| 64 | RAG with LangChain | Advanced |
| 65 | RAG with LlamaIndex | Advanced |

## Phase 11: AI Agents
| Day | Topic | Level |
|---|---|---|
| 66 | Tools & function calling | Intermediate |
| 67 | Building an agent loop by hand | Advanced |
| 68 | Agent use cases & design patterns | Advanced |
| 69 | Agent SDKs: OpenAI Agents SDK, Claude Agent SDK, Google ADK | Advanced |
| 70 | Multi-agent systems & context isolation | Advanced |

## Phase 12: Model Context Protocol (MCP)
| Day | Topic | Level |
|---|---|---|
| 71 | What is MCP? Hosts, clients & servers | Intermediate |
| 72 | MCP transport layer & data layer | Advanced |
| 73 | Build an MCP server | Advanced |
| 74 | Build an MCP client | Advanced |

## Phase 13: Multimodal AI
| Day | Topic | Level |
|---|---|---|
| 75 | Image understanding (vision APIs) | Intermediate |
| 76 | Image generation | Intermediate |
| 77 | Speech-to-text & text-to-speech | Intermediate |
| 78 | Video understanding | Advanced |

## Phase 14: Evals & Observability
| Day | Topic | Level |
|---|---|---|
| 79 | Why LLM evaluations matter | Intermediate |
| 80 | Deterministic evals | Intermediate |
| 81 | Model-based evals (LLM-as-judge) | Advanced |
| 82 | Human evals & regression testing | Advanced |
| 83 | Eval tools: Ragas & DeepEval | Advanced |
| 84 | Tracing & logging: LangSmith, Langfuse, Helicone | Advanced |
| 85 | Cost, latency & production monitoring | Advanced |

## Phase 15: Fine-tuning, Tooling & Capstone
| Day | Topic | Level |
|---|---|---|
| 86 | Fine-tuning: when and how | Advanced |
| 87 | Harness engineering | Advanced |
| 88 | AI development tools: Claude Code, Cursor, Codex | Intermediate |
| 89 | Capstone: design an end-to-end AI app | Advanced |
| 90 | Capstone: ship it & retrospective | Advanced |
