import json
import openai


def enhance_prompt(key: str, prompt: str, model: str = "gpt-4", temperature: float = 0.5) -> dict:
    """
    Enhance a prompt using OpenAI's API.

    It's using a lot of examples right now to attempt to minimize the amount of tokens that it generates.
    It tries to replace the large text body with [content] and [summary] instead of spitting it back out again.
    It's working pretty well, but it's not perfect. Using gpt3.5-turbo gives wild results with a prompt this large.
    Would love to see what you can do with it!

    :param key: OpenAI API key
    :param prompt: Prompt to enhance
    :param model: OpenAI model to use (default: gpt-4)
    :param temperature: Temperature to use (default: 0.5)
    :return: Enhanced prompt as a json dictionary
    """
    openai.api_key = key

    system_prompt = """Act as a senior prompt engineer with years of experience creating prompts for GPT models. Your task is to take a prompt from a user and enhance it. Your internal scoring grade is a number between 0 and 10. Your response should aim to always achieve a 10/10 score.

Rules:
- When given a prompt asking to summarize large bodies of text, always reply with [summary] instead of the original summary.
- When given a prompt asking to explain large bodies of text, always reply with [content] instead of the original content.
- When given a prompt asking to format large bodies of text, always reply with [content] instead of the original content.
- Always utilize state-of-the-art tricks and tips to enhance the prompts. Example tricks: "Act as a", chain-of-thought, few shot prompts, tonality, length confinement, "explain your reasoning step by step"
- Assume the reader is not familiar with writing 10/10 prompts and list detailed explanations of the list of enhancements.
- Do not mention in the list of enhancements that you replaced the content with [content] or [summary]

Format in JSON:
{"original_prompt_score":#,"reason_for_score":"","enhanced_prompt":"","list_of_enhancements":[""]}

=====================
Examples:
User: ```Write a blog post about the dog training```
Enhanced: Write a 1500-word blog post that covers basic dog training techniques for young puppies. The post should also discuss different types of rewards and punishments that can be used in training. Detail how to train puppies to stop biting, barking, and potty training. Provide tips on how to make training fun and involve some case studies. 

User: ```Write me a summary for: The Twitter algorithm, and, as a matter of fact, any social media algorithm, is constantly learning. A part of the deep learning process is integration with NLP, which stands for natural language processing.```
Enhanced: As an expert in paraphrasing and AI, rewrite the following paragraph focusing on maintaining the original meaning while also demonstrating an engaging chain of thought and clear, concise language: [summary]

User: ```Example this code to me line by line:
<div className={'bg-white p-8 rounded-2xl mt-8'}>
<h2 className={'text-xl font-medium'}>Result</h2>
<p>Prompt Score: 5/10</p>
<p>Reason for score: 5/10</p>
<p className={'bg-gray-100 p-4 rounded-xl mt-2'}>Enhanced Prompt:</p>
<p>Changes made:</p>
</div>```
Enhanced: As a senior web developer, explain the functionality of the following React code snippet step by step, discussing each line of code and its purpose in creating a user interface component: [content]
"""

    final_result = []
    response = openai.ChatCompletion.create(
            model=model,
            temperature=temperature,
            max_tokens=512,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stream=True,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"```{prompt}```"}
            ])

    for chunk in response:
        if dict.get(chunk, "choices") is None:
            continue

        choice = chunk.choices[0]
        content = dict.get(choice.delta, "content")
        if content is None:
            continue

        final_result.append(content)
        print(content, end="", flush=True)

    print("\n")

    message = "".join(final_result).strip()
    json_response = json.loads(message)

    return json_response
