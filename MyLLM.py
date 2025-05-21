from crewai import LLM

class MyLLM():
    GPT4o_mini    = LLM(model='gpt-4o-mini')
    GPT4o_mini_2024_07_18    = LLM(model='gpt-4o-mini-2024-07-18')
    GPT4o    = LLM(model='gpt-4o')
    GPT_o1    = LLM(model='01-preview')
    GEMMA2_9B    = LLM(model='groq/gemma2-9b-it')
    LLAMA3_70B    = LLM(model='llama3-70b-8192')
    GROQ_LLAMA   = LLM(model='groq/llama-3.3-70b-versatile')
