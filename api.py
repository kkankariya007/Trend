from fastapi import FastAPI,File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pytrends.request import TrendReq

# requests_args = {
#     'headers': {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
#     }
# }

# Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq(retries=3)
# pytrend = TrendReq()
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangsolo.com",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

kw_list = ["Blockchain"]
pytrend.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
pytrend.interest_over_time()
