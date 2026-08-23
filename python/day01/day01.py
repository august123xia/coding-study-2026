jobs = [
    {"company": "Google", "score": 85},
    {"company": "Amazon", "score": 72},
    {"company": "ali", "score":90}
]

for job in jobs:
    if job["score"] >= 80:
        print(job["company"])