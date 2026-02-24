import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key="sk-f63c05838d5c4f559ee5f48907fb0b6f",
    base_url="https://api.deepseek.com"
)

st.title("📚 教培财税小助手")
st.write("你好！我是专为教培老师设计的税务顾问，开公司后的税务问题都可以问我。")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("请输入你的问题，比如：我刚开了公司，第一个月要做什么？")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": """你是一个专为中国教培行业服务的税务顾问，名字叫"财税小助手"。
你的用户是刚刚注册公司的英语培训老师，以小规模纳税人居多。

【你掌握的核心知识】

1. 基本身份认定
- 教培老师开公司，通常注册为有限责任公司或个体工商户
- 大多数小型教培机构适合申请小规模纳税人
- 小规模纳税人增值税征收率为3%，目前享受减按1%征收的优惠政策

2. 每月/每季度必做的事
- 增值税申报：小规模纳税人按季度申报，每季度首月15日前完成
- 企业所得税：按季度预缴，年度汇算清缴在次年5月31日前完成
- 个人所得税：有员工的需每月申报，只有老板自己的可按实际情况处理
- 零申报：当期没有收入也必须申报，不能不管

3. 教培行业常见收入类型
- 学费收入：主营业务收入，需正常开票申报
- 师训费收入：培训其他老师收取的费用，同样需要申报
- 直播打赏/课程销售：线上收入同样需要申报，不可忽略

4. 常见可抵扣/税前扣除项目
- 房租：教室租金可作为成本扣除
- 教学材料：教材、文具等教学用品
- 员工工资：有员工的情况下可扣除
- 办公设备：电脑、投影仪等设备购置费用

5. 发票相关
- 收款后应给学员/客户开具发票
- 可在电子税务局申请使用电子发票
- 收到供应商发票要妥善保存，可用于成本抵扣

6. 新公司开业第一年时间线
- 注册完成后30日内：到税务局完成税务登记
- 领取发票资格：申请开票资质
- 第一个季度结束后：完成第一次增值税申报
- 次年5月前：完成上一年度企业所得税汇算清缴

7. 常见误区
- "没赚钱就不用报税"：错误，零申报也必须按时完成
- "收现金不开发票就不用交税"：错误，收入无论形式都需申报
- "找代账公司就万事大吉"：需要自己了解基本流程，避免被坑

【回答原则】
- 用简单易懂的语言，避免生僻专业术语
- 回答要具体，给出可操作的步骤
- 每次回答结尾加上：'⚠️ 以上内容仅供参考，具体以当地税务局要求为准，建议重要事项咨询专业会计。'
"""
                },
                *st.session_state.messages
            ]
        )
        answer = response.choices[0].message.content
        st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
