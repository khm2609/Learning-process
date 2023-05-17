from fastapi import FastAPI
from Scopus import ScopusScraper
import uvicorn

app = FastAPI(
    title="Scopus Scraper",
    description="description"
)


@app.get('/author/{scopus_id}')
def get_scopus_author_data(
    scopus_id: str,
    get_articles: bool = True
):
    parser = ScopusScraper()
    author_data = parser.parse(scopus_id)

    return author_data



if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)