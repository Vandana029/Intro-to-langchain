# RunnableSequence
RunnableSequence is a sequential chain of runnables in LanggCChain that executtes each step one after another, passing the output of one step as a input to the next.

It is useful when you need to compose multiple runnables together in structured workflow. 

# RunnableParalle
RunnableParallel is a runnable primitive that allows multiple runnables to execute in parallel.

Each runnable receives the same input and processes it independently, producing a dictionary of outputs.

# RunnablePassthrough
RunnablePassthrough is a special Runnable primitive that simply returns the input as output without modifying it.

# RunnableLambda
RunnableLambda is a runnable primitive that allows you to apply custom Python functions within an AI pipeline.

It acts as a middleware between different AI components, enabling preprocessing, transformation, API calls, filtering, and post-processing in a LangChain workflow.

# RunnableBranch
RunnableBranch is a control flow component in LangChain that allows you to conditionally route input data to different chains or runnables based on custom logic.

It functions like an if/elif/else block for chains — where you define a set of condition functions, each associated with a runnable (eg., LLM call, prompt chain, or tool). 

The first matching condition is executed. If no condition matches, a default runnable is used (if provided).

# LCEL - Langchain Expression Language. 
It is a way to define the logic of the runnable branch in sequence. foe example r1 | r2 | r3
