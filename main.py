from json import load,dumps
from requests import post
num=1
myheader={
    "accept": "application/json,application/x-www-form-urlencoded,text/plain,*/*",
    "accept-language": "vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9naXZlbm5hbWUiOiJBZG1pbiBUcuG6r2MgTmdoaeG7h20gVG_DoG4gRGnhu4duIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvc2lkIjoiMTU1NjkiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiYWRtaW50bnRkIiwiZXhwIjoxNzE2ODk0ODQ3LCJpc3MiOiJodHRwczovL3NpZXV0cmluaG9ob2NkdW9uZy5jb20iLCJhdWQiOiJodHRwczovL3NpZXV0cmluaG9ob2NkdW9uZy5jb20ifQ.qMd1d6ue-ZUxZzE01rKDXyFhtWND1c6xUiv_87KrIEg",
    "content-type": "application/json;charset=UTF-8",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"CocCoc\";v=\"100\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site"
  }
levels=['nhận biết','thông hiểu','vận dụng thấp','vận dụng cao']
answs=['A','B','C','D']
maindata=load(open('data.json'))
for data in maindata:
  print(num)
  num+=1
  data_json={'class_id': 5,
   'course_id': 152,
   'topics_id': 'TV02-025',
   'knowledge_topic_Id': 3393,
   'question': data['q']['Câu hỏi'],
   'point': 1,
   'level': 'level%s'%(levels.index(data['q']['Mức độ'].lower().strip())+1),
   'time_second': 60,
   'status': 1,
   'explain_the_answer': data['a']['Giải thích'],
   'listAnswer': [{'title': 'A',
   'answer_flag': False,
   'status': 1,
   'sort_order': 1,
   'answer': data['a']['A']},
   {'title': 'B',
   'answer_flag': False,
   'status': 1,
   'sort_order': 2,
   'answer': data['a']['B']},
   {'title': 'C',
   'answer_flag': False,
   'status': 1,
   'sort_order': 3,
   'answer': data['a']['C']},
   {'title': 'D',
   'answer_flag': False,
   'status': 1,
   'sort_order': 4,
   'answer': data['a']['D']}],
   'name_subject_topic': 'MRVT: Giao tiếp, kết nối',
   'name_topics': 'TV02-025',
   'name_class': 'Lớp 2',
   'name_course': 'Tiếng Việt',
   'user_created': 15569}
  data_json['listAnswer'][answs.index(data['a']['Đáp án đúng'].lstrip())]['answer_flag']=True
  postdata=dumps(data_json)
  res=post('https://apiptb.5phutthuocbai.com/api/ReviewAll/question/create',postdata,headers=myheader)
  # print(data_json)
  print(res,res.text)