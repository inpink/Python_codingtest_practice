import random
import datetime

ids = [1, 2] + list(range(420, 2501))

def generate_user_id():
  return random.choice(ids)

def generate_random_datetime():
  return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

def generate_template_sql(template_id, prompt_id):
  user_id = generate_user_id()
  created_at = generate_random_datetime()
  updated_at = created_at

  title = f"Template Title {template_id}"
  description = f"Description for template {template_id}"
  editor = f"Editor content for template {template_id}"
  file_url = "NULL"
  visible = "TRUE" if random.random() > 0.5 else "FALSE"

  return f"INSERT INTO templates (id, user_id, title, description, likes, purchaseCount, editor, fileUrl, prompt_id, visible, createdAt, updatedAt) VALUES ({template_id}, {user_id}, '{title}', '{description}', 0, 0, '{editor}', {file_url}, {prompt_id}, {visible}, '{created_at}', '{updated_at}');"

def generate_prompt_sql(prompt_id):
  created_at = generate_random_datetime()
  updated_at = created_at

  # 더미 데이터 생성
  purpose = f"Purpose for prompt {prompt_id}"
  color = random.choice(["Red", "Blue", "Green", "Yellow"])
  model = random.choice(["MODEL_A", "MODEL_B", "MODEL_C"])

  return f"INSERT INTO prompts (id, purpose, color, model, createdAt, updatedAt) VALUES ({prompt_id}, '{purpose}', '{color}', '{model}', '{created_at}', '{updated_at}');"

def main():
  num_records = 100000000  # 1억 개의 데이터
  batch_size = 1000  # 한 번에 1000개의 INSERT 문 생성
  template_sql_file = "insert_templates.sql"
  prompt_sql_file = "insert_prompts.sql"

  # templates와 prompts SQL 파일 생성
  with open(template_sql_file, "w") as template_file, open(prompt_sql_file, "w") as prompt_file:
    for i in range(1, num_records + 1):
      prompt_sql = generate_prompt_sql(i)
      prompt_file.write(prompt_sql + "\n")

      template_sql = generate_template_sql(i, i)
      template_file.write(template_sql + "\n")

      # 배치로 파일에 쓰기
      if i % batch_size == 0:
        print(f"{i} records processed")

  print("SQL file generation completed.")

if __name__ == "__main__":
  main()