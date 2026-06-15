conversation_scenarios = [

    {
        "prompt": "안녕하세요!",
        "translation": "Hello!",

        "choices": [
            "안녕하세요",
            "감사합니다",
            "미안합니다"
        ],

        "correct": 1,

        "explanation":
        "안녕하세요 is the standard greeting response."
    },

    {
        "prompt": "감사합니다.",
        "translation": "Thank you.",

        "choices": [
            "죄송합니다",
            "천만에요",
            "안녕히 가세요"
        ],

        "correct": 2,

        "explanation":
        "천만에요 means 'You're welcome.'"
    },

    {
        "prompt": "이름이 뭐예요?",
        "translation": "What is your name?",

        "choices": [
            "저는 학생입니다",
            "제 이름은 민수입니다",
            "배고파요"
        ],

        "correct": 2,

        "explanation":
        "제 이름은 ___ 입니다 means 'My name is ___."
    }

]