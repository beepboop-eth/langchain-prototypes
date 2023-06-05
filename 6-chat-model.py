from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

def main():
    chat = ChatOpenAI(temperature=0)
    
    # print("Generating completion for one message...")
    # human_message = HumanMessage(content="Translate this sentence from English to French.  I love programming.")

    # print_single_message(chat, human_message)

    # print("Generating completion for multiple messages...")

    # messages = [
    #     SystemMessage(content="You are a helpful assistant that translates English to French"),
    #     HumanMessage(content="I love programming")
    # ]

    # print_multiple_messages(chat, messages)

    print("Generating batch completion for multiple messages...")

    batch_messages = [
        [
            SystemMessage(content="You are a helpful assistant that translates English to French"),
            HumanMessage(content="I love programming.")
        ],
        [
            SystemMessage(content="You are a helpful assistant that translates English to French."),
            HumanMessage(content="I love artificial intelligence.")
        ]
    ]

    print_batch_messages(chat, batch_messages)

def print_single_message(chat, message):
    print(f"Getting completion for: {message.content}")
    completion = chat([message])
    print(completion.content)

def print_multiple_messages(chat, messages):
    for message in messages:
        print(f"Getting completion for message content: {message}")

    completion = chat(messages)
    print(completion.content)

def print_batch_messages(chat, batch_messages):
    for messages in batch_messages:
        for message in messages:
            print(message.content)
    
    batch_completion = chat.generate(batch_messages)
    print(batch_completion)

if __name__ == "__main__":
    main()