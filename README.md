# datathon-2023
Solution to the datathon fme 2023 challenge proposed by mango

# What have we done?
We opted for a LLM + VLM based approach for outfit generation. We thought it was the best option as it needs no training data (because we can use large models for the demo) and it can be easily scaled and optimized with fine-tunning and using OpenAI or other model providers.

Our solution consist of two main pipelines: the indexing pipeline and the generation pipeline.

## Indexing Pipeline
The main goal of the indexing pipeline is to add all the clothing items to a vectorstore (in this case Chroma) to be able to find which items have similar descriptions. In order to do that we need to be able to augment the data by analyzing the image provided as every detail of that image may affect on weather it is or not a good choice for the outfit.
To describe the image we used the 7 billion LLaVA model with the prompt included in the LLaVA.prompt file. Due to our lack of resources we were only able to describe 220 images, but with accelerators all of the images could be easily described in little time and with less than 2$.
With the description of the image an the data provided by MANGO we will further process the description of the object to make it detailed and rich.
Now we will index those items on the vectorstore (embedding on the last description). And thats it, ready for generation!

## Generation pipeline
Our approach is rather flexible on how to treat inference as you can adapt your LLM agent to perform outfit generation from a prompt, outfit completion or outfit validation. But the key idea to make this work is to make the agent describe in a very detailed way the peace of clothing it will add, then extract peaces that are similar to that description from the vectorstore and finally make the agent choose one.

# Limitations and further improvements
Due to low computational resources we were not able to perform fine-tunning of the LLaVA model for clothes description but we saw significantly good results for the small raw model. This makes us think that fine-tunning is not so necessary to improve performance, but using the larger 13B model might.
Using GPT-4 or GPT-3.5 as the language model for the agent instead of GPT-3 might be beneficial, but I believe that better prompting will be more influential on the results.