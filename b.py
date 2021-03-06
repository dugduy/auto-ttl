from json import load
levels=['nhận biết','thông hiểu','vận dụng thấp','vận dụng cao']
answs=['A','B','C','D']
data=load(open('data.json'))[2]
data_json={'class_id': 5,
 'course_id': 152,
 'topics_id': 'TV02-025',
 'knowledge_topic_Id': 3290,
 'question': data['q']['Câu hỏi'],
 'point': 1,
 'level': 'level%s'%(levels.index(data['q']['Mức độ'].lower().lstrip())+1),
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
 'name_subject_topic': 'Từ ngữ và nội dung bài đọc theo chủ đề: Giao tiếp và kết nối',
 'name_topics': 'TV02-025',
 'name_class': 'Lớp 2',
 'name_course': 'Tiếng Việt',
 'user_created': 15569}
data_json['listAnswer'][answs.index(data['a']['Đáp án đúng'].lstrip())]['answer_flag']=True
print(data)
print(data_json)
