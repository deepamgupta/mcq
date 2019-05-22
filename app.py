from Question import Question

question_prompts = [
    "What is the color of Banana?\na)Yellow\nb)Red\nc)Magenta",
    "What is the capital of India?\na)Lucknow\nb)Guna\nc)New Delhi",
    "What is the highest Mt. Peak in the world?\na)Mt.Everest\nb)Kunchenjunga\nc)Himalaya"
]

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'a')
]

def run_test():
    score = 0

    for question in questions:
        answer = input(question.prompt + "\n")
        if answer == question.answer:
            score += 1

    print("Score is ", score, "/", len(questions), " correct!")


run_test()