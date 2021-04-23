import requests

for i in range(100):
    url = f'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1606402827543&countryId=&cityId=1&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=%25E5%2590%258E%25E5%258F%25B0&pageIndex={i}&pageSize=10&language=zh-cn&area=cn'
    data = requests.get(url)
    # print(data.status_code)
    jobs = data.json()['Data']['Posts']
    for j in jobs:
        url_detail = f"https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1606403635632&postId={j['PostId']}&language=zh-cn"
        data_detail = requests.get(url_detail).json()
        for k, v in data_detail['Data'].items():
            if isinstance(v, str) and (('python' in v) or ('Python' in v) or ('PYTHON' in v)):
                print(data_detail['Data']['RecruitPostName'])
                print(data_detail['Data']['Requirement'])
                print(data_detail['Data']['Responsibility'])
                print(url_detail)
                print('\n')
print()
