import openai


def openai_prompt(init_prompt, items, key):
    openai.api_key = key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": init_prompt},
            {"role": "user", "content": items}
        ]
    )

    arr = response.choices[0].message.content

    return arr
