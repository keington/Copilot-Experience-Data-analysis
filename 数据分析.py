# 导入第三方库

# 引入json库
import json
# 引入pandas库
import pandas as pd
# 引入sqlalchemy库
import sqlalchemy
# 引入pymysql库
import pymysql


# 从excel中提取数据
excel_data = pd.read_excel('data.xlsx', sheet_name='Sheet1')
print(excel_data)

# 根据序号排序
excel_data = excel_data.sort_values(by='序号')
print(excel_data)

# 将已排序的数据转换为json格式
json_data = excel_data.to_json(orient='records')

# 格式化并美化输出json数据
print(json.dumps(json.loads(json_data), indent=4, ensure_ascii=False))

# 格式化后输出的json数据写入文件并保存
with open('data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(json.loads(json_data), indent=4, ensure_ascii=False))
