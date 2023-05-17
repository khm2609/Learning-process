from fastapi import FastAPI
from ScopusCode import ScopusScraper, calculations
import uvicorn
import axios
from pydantic import BaseModel
from schemes import AuthorScopusInfo, AuthorArticle
from typing import List


app = FastAPI(
    title="Scopus Scraper",
    description="description",
    version="1.0.0"
)


@app.get('/author/{scopus_id}')
async def get_scopus_author_data(
    scopus_id: str,
    get_articles: bool = False
) -> AuthorScopusInfo:
    parser = ScopusScraper()
    author_data = parser.parse(scopus_id, get_articles)

    return AuthorScopusInfo(**author_data)


@app.post('/get_metrics')
def get_articles_metrics(
    articles: List[AuthorArticle]
):
    # for item in articles:
    #     print(item.Title)


    return calculations(articles)


    # return {
    #     'message': 'Ok'
    # }

# async def create_item(item: AuthorScopusInfo):
#     return item


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)