## ChatGPT Prompt Enhancer

**Note**: This was going to be put on my site [AiShowcase.io](https://aishowcase.io) but I decided to just put it here for now. If you have some ideas on changing up the prompts, create a pull request or hit me up on twitter [@NetrDev](https://twitter.com/netrdev). Would love to figure out how to make this cheaper and run on gpt3.5-turbo with high accuracy.

---

A little experiment I was working on to see how well ChatGPT could improve prompts for you and teach you how to write better prompts at the same time.

### Example response:
```bash
Original prompt score: 6/10
Reason for score: The original prompt is clear in its intent but lacks a proper structure and format.
Enhanced prompt: As an expert language translator and editor, take the following sentence in a foreign language, detect the language, translate it into English, and then rephrase it using elegant and advanced English vocabulary while maintaining its original meaning: 'istanbulu cok seviyom burada olmak cok guzel'
List of enhancements:
1. Rephrased the prompt to focus on expertise in translation and editing
2. Clarified the task and expectations
3. Provided a clear structure and format

```

Currently it's only working reliably with GPT-4 to return the format in the correct way, every time. The primary motivation behind setting it up with formatted JSON, was to integrate it into the frontend of my website. It needs a consistent structure to work properly.

#### Thoughts
The system prompt is too big right now. It costs around $0.03 to ehance this prompt:
```
I want you to act as an English translator, spelling corrector and improver. I will speak to you in any language and you will detect the language, translate it and answer in the corrected and improved version of my text, in English. I want you to replace my simplified A0-level words and sentences with more beautiful and elegant, upper level English words and sentences. Keep the meaning same, but make them more literary. I want you to only reply the correction, the improvements and nothing else, do not write explanations. My first sentence is "istanbulu cok seviyom burada olmak cok guzel"
```

The original prompt above returns this:
```
Istanbul holds a deep affection in my heart, and the experience of being present in this place is truly delightful.
```

The enhanced prompt given was:
```
As a proficient language translator, I want you to detect the language spoken, translate it into English, and improve the text by replacing basic words and sentences with more sophisticated and elegant alternatives while maintaining the original meaning. Ensure that your response only contains the improved translation without any additional explanations. Here's the sentence to be translated and improved: 'istanbulu cok seviyom burada olmak cok guzel'
```

Which returned this response:
```
I hold an immense love for Istanbul, and being present in this city brings about a profound sense of beauty.
```

---

Very similar results but with less tokens. Being able to essentially achieve the same result with fairly different wording is very interesting. I definitely think with enough tweaking (to reduce cost but maintain reliability) and more playing around, this could really help you learn more about how GPT processes prompts. 


---

Feel free to play with it, fork it, use it yourself. Let me know what you find out. I'm always open to suggestions and improvements.