import openai


def openai_prompt(init_prompt, list_food_items):
    openai.api_key = "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"
    items = ""

    for i in list_food_items:
        items += i + ", "
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": init_prompt},
            {"role": "user", "content": items}
        ]
    )

    # response = openai.Completion.create(
    #     engine="text-embedding-ada-002",  # You can choose the appropriate engine
    #     prompt=question,
    #     max_tokens=16385  # Adjust this number to control the length of the response
    # )
    # generated_text = response.choices[0].text

    # arr = response["choices"][0]["text"]

    arr = response.choices[0].message.content

    return arr
