# LangFuse for CICD in LLMOPs
* This repo goes over how to utilize LangFuse.
  * Link to Langfuse: https://langfuse.com/
  * Langfuse github: https://github.com/langfuse/langfuse



# What is Langfuse?
* Simply put, it is an **LLM engineering platform**. 
* Open sourced on github 
* Also available as paid cloud solution. 
* Can be utilized as SDK in Python or JavaScript. 
* Integrations with LangChain and Llama Index. 


# Why do we need a platform like Langfuse? 
* For a single LLM app in PRODUCTION, we often need to do the following:

1. Debug issues in production.
2. Analyze and iterate on multiple solutions. 
3. Monitor the performance in production. 
4. Continuously run tests and create new releases. 

* Multiple teams will need to research and collaborate on multiple projects. 
* Multiple LLM applications need to be released and maintained at the same time. 



# Langfuse Ecosystem
* There are 3 main parts: 

## 1. Development 
* Process of tracking all LLM calls and other app logic.
* Support APIs, SDK, and 3rd party libraries. 
* Langfuse UI: inspect and debug calls. 
* Prompt Engineering with playground. 
* Prompt Management

## 2. Monitoring
* Analytics dashboard to monitor: Cost, Latency, Quality of models
* Evaluations
  * Custom based LLM evals 
* Real user feedback with scores and comments. 
  * Can easily integrate feedback from the end users. 


## 3. Testing
* Langfuse Datasets 
    * Allows you to create datasets with input and outputs to benchmark performance of your LLM based application. 
* Track versions and releases in production. 


# Langfuse for Monitoring CI/CD Pipelines in Production
1. Langfuse for CI/CD
  * Multiple components of Langfuse can be used with CI/CD.
  * Langfuse seamlessly integrates with LangChain.
  * Default releases of your own app are versioned in Langfuse. 

2. Team and Data Management
   * Projects and Group Experiments
   * Users can safely use SSO (single sign on)
   * RBAC (Role based access support), various roles are supported including: 
       * Owner - all ownership
       * Admin - all owner features except project delete and transfer
       * Member - (write permissions)
       * Viewer - (read-only permissions)
    
   * Cloud based SaaS solution provided.
   * On-prem deployments are available.
   * ISO and SOC2 security certifications for Langfuse -- this is important for sensitive data!


# Tracing in Langfuse
* **Trace** Definition
  * "A single request or operation on your LLM based application."
* **Session** Definition
  * Grouping of multiple traces.
  * Can be based on: users, clients, etc..
 
* **Span** Definition
  * Unit of work within each trace.

* **Generation** Definition
  * Log generation of AI and LLM models.
  * Additional info on: prompts, models, completions. 
* Let's walk through what Tracing looks like in Lanfuse.

1. User interacts with application.
   * We have user metadata, ID, and more.
  
2. Tracing 
   * This is the result of the user's interaction with our application. 
   * The usual process is as follows but can vary based on application:
       * Trace function pinged -->
       * Generation embedding -->
       * SPAN vector store -->
       * SPAN prompt creation -->
       * GENERATION LLM call -->
       * Return output to final user.
    
3. A new Trace!
   * This can be from the same user or a new user. Anytime our application is interacted with it creates a new "Trace".
   * The same process above is then reproduced and logged in Langfuse as a separate Trace.  


# Coding Representation of Tracing
* The `@observe()` decorator can easily be applied to functions in an application that you want to trace.
* What this decorator/function does by default is capture:
  * timings/durations
  * function name
  * args and kwargs as input dict
  * returned values as output of function
  * additional tags, metadata, IDS can be added
  * support for callbacks in LangChain
 

# Langfuse for Prompt Management
* The main benefit? Team can easily track performance of prompt versions using Langfuse Tracing. 
* In production on an LLM application, engineers/managers/team can easily manage prompts live during production via cache intervals from the users.
* Can also setup default prompts.
* This allows an application to stay in production rather than having to shut down the application to change prompt configuration.
* Specific language used by Langfuse:
  * 1. **Decoupling**
       * This will deploy new prompts without have to takedown and re-deploy an application.
  * 2. **Prompt updates**
       * Langfuse allows non-technical users to create and update prompts via the Langfuse GUI console without having to dive into the codebase.
  * 3. **Rollbacks**
       * Langfuse enables you to quickly rollback your application during live production to a previous version prompts in order to fix specific prompts that are in production.
      

# Langfuse Scores and Evaluations
* Scores serve as an object to store evaluation metrics in Langfuse.
* We can easily monitor the LLM outputs via the scoring system.
* **Scoring Components**:
  * 1. Datatypes:
       * NUMERIC
       * CATEGORICAL
       * BOOLEAN
      
  * 2. Attributes:
       * name
       * value / stringValue
  * 3. Additional Metadata:
       * comment
       * source
       * various IDs


## Scores can be of various types:
* 1. Self-annotated in User Interface
      * Manual scores given by the team
* 2. User Feedback
      * Can be integrated in the UI and directly shown to the user.
      * Usually a thumbs up or thumbs down or other icons.
    
* 3. Model-based Evaluation:
     * We can use LLMs to score trace calls from our application based on varied criteria such as:
         * Toxicity
         * Hallucination
         * ...etc...
     * We can also create our own custom model evaluations.
         * These can be run automatically after EVERY trace based on certain filter criteria.
         * We can also fetch the runs and upload the computed scores to the user interface!
      

# Langfuse Datasets
* The datasets component of Langfuse is a collection of inputs (and expected outputs, e.g. "Golden Truth") of your LLM application.
* These are used to BENCHMARK new releases of your application prior to deployment in PRODUCTION.
* This is what the dataset utilization in Langfuse CI/CD pipeline looks like (source: Analytics Vidhya):

![image](https://github.com/user-attachments/assets/03327558-f991-4e8f-9127-a7b3592c2e76)

* Breakdown of the Dataset process above:
  * **NOTE: This part is within the application (e.g. SaaS or On-prem)**
 
 1. Engineer or any other team member can add the "Dataset" based on the expected input and outputs of the application. This may also include tests that need to be run on the application.
    * This is to ensure a baseline quality check prior to production deployment.
* **NOTE: This part is within the CI/CD pipeline**

2. Engineer Intervenes when changes need to be made
3. Fetch Code
4. Fetch Dataset
   * Dataset is fetched when changes need to be made and it can be brought into the CI/CD pipeline.
5. Evaluation
   * This can be done using the original Dataset created with benchmarks.
   * This allows easy comparison of the benchmarks with what the user is seeing in the production application.
6. Release
   * After evaluating, we can then make a decision if the output of the NEW changes give better evaluation scores.
      
7. Production App
   * App is re-deployed into production if the outputs are satisfactory.
      
8. **Traces, Evaluation, User Feedback
   * All end-user interaction with the application is stored in TRACES in the Langfuse ecosystem.
      
9. QA engineers can use the DATASET and TRACES to continually evaluate and update as needed. 


