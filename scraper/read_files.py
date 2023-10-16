def read_job():
    with open('./recent_job.txt', 'r', encoding='utf-8') as file:
        join_text = [line for line in file]
        print(join_text)
    return join_text
