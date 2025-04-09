from crewai import LLM

class MyLLM():
    GPT4o_mini    = LLM(model='gpt-4o-mini')
    GPT4o_mini_2024_07_18    = LLM(model='gpt-4o-mini-2024-07-18')
    GPT4o    = LLM(model='gpt-4o')
    GPT_o1    = LLM(model='01-preview')
    GEMMA2_9B    = LLM(model='groq/gemma2-9b-it')
    LLAMA3_70B    = LLM(model='llama3-70b-8192')
    QWEN    = LLM(model='groq/qwen-qwq-32b')
    GROQ_MIXTRAL    = LLM(model='groq/mixtral-8x7b-32768')
    GROQ_LLAMA2    = LLM(model='groq/llama-3.2-11b-vision-preview')
    GROQ_DEEPSEEK    = LLM(model='groq/deepseek-r1-distill-qwen-32b')
