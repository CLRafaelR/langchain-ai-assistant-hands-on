import os

import streamlit as st
import openai
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.memory import (
    ConversationBufferMemory,
    StreamlitChatMessageHistory,
)
from langchain.prompts import MessagesPlaceholder
from PIL import Image

from customtools import (
    NoOpTool,
    ToogleRemoteLightTool,
    load_streamlit_image_tools,
    load_zapier_tools_for_openai_functions_agent,
)

import datetime

dt_now = datetime.datetime.now()


# エージェントが使用するツールを準備する関数
def setup_tools():
    tools = []

    # Step2: AI エージェントを動かしてみよう
    # ツールが何もないとうまく動作しないため、何もしないツールを用意
    tools.append(NoOpTool())

    # Step3: エージェントが Wikipedia を検索できるようにしてみよう（Stable Diffusionについて教えて）
    wikipedia_tools = load_tools(["wikipedia"])
    tools.extend(wikipedia_tools)

    terminal_tools = load_tools(["terminal"])
    tools.extend(terminal_tools)

    # Step4: Zapier NLA で Google カレンダーに予定を登録させてみよう（明日の13時に会議の予定を登録して）
    # zapier_tools = load_zapier_tools_for_openai_functions_agent()
    # tools.extend(zapier_tools)

    # Step5: Streamlit 上の部屋の電気・扇風機（の画像）を操作させよう
    streamlit_image_tools = load_streamlit_image_tools()
    tools.extend(streamlit_image_tools)

    # 講師用
    # remote_light_tool = ToogleRemoteLightTool(
    #     host="localhost",
    #     room_id="myroom",
    #     basic_auth_username="testuser",
    #     basic_auth_password="testpassword",
    # )
    # tools.append(remote_light_tool)

    return tools


# エージェントを作成する関数
def create_agent(history: StreamlitChatMessageHistory):
    # LLMの準備
    # llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, streaming=True)
    llm = ChatOpenAI(
        model_name="gpt-4-1106-preview",
        # model_name="gpt-4-32k-0613",
        temperature=0,
        streaming=True,
    )

    # 会話履歴を使う準備
    memory = ConversationBufferMemory(
        chat_memory=history, memory_key="memory", return_messages=True
    )

    # エージェントが使用するツールを準備
    tools = setup_tools()

    # エージェントを初期化
    return initialize_agent(
        tools=tools,
        llm=llm,
        memory=memory,
        agent=AgentType.OPENAI_FUNCTIONS,
        agent_kwargs={
            "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
        },
    )


models = dict(openai.Model.list())
for i in models["data"]:
    if i["id"].startswith("gpt"):
        print(i["id"])

# Streamlitのセッションに保存するデータ
if "is_light_on" not in st.session_state:
    st.session_state.is_light_on = False

if "is_fan_on" not in st.session_state:
    st.session_state.is_fan_on = False

# Streamlitのセッションに自動で会話履歴が保存されるよう準備
history = StreamlitChatMessageHistory()

# CSSを適用
with open("assets\style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True,
    )

# タイトルを表示
st.title("My AI Assistant")

# チャット履歴を表示
for message in history.messages:
    with st.chat_message(message.type):
        st.write(message.content)

# 入力を受け付け
prompt = st.chat_input("What is up?")

# 入力があった場合、エージェントを実行
if prompt:
    with st.chat_message("human"):
        st.write(prompt)

    with st.chat_message("ai"):
        agent_chain = create_agent(history)
        callback = StreamlitCallbackHandler(st.container())

        response = agent_chain.run(prompt, callbacks=[callback])
        st.write(response)

        now = dt_now.strftime("%Y%m%d_%H%M_%S")

        print(
            "# ユーザープロンプト",
            prompt,
            "# LLMの出力結果",
            response,
            "-" * 3,
            sep="\n\n",
        )

        with open(
            f"../log/inputs/{now}.md",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(prompt)

        with open(
            f"../log/outputs/{now}.md",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(response)

        with open(
            f"../log/threads/{now}.md",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(
                f"""# ユーザープロンプト

{prompt}

# LLMの出力結果

{response}"""
            )


# サイドバー
with st.sidebar:
    # APIキーの入力欄を表示
    # print(os.getenv("OPENAI_API_KEY"))
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    # os.environ["OPENAI_API_KEY"] = st.text_input("OpenAI API キー", type="password")
    # os.environ["ZAPIER_NLA_API_KEY"] = st.text_input(
    # "Zapier NLA API キー", type="password"
    # )

    # 画像を表示
    if st.session_state.is_light_on:
        light_on_off = "on"
    else:
        light_on_off = "off"

    if st.session_state.is_fan_on:
        fan_on_off = "on"
    else:
        fan_on_off = "off"

    st.image(Image.open(f"assets/light-{light_on_off}-fan-{fan_on_off}.png"))
