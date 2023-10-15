import openai


def openai_prompt(init_prompt, list_food_items, key):
    openai.api_key = key

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

    arr = response.choices[0].message.content

    return arr
