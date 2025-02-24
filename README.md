# ice_breaker

A repository for learning LangChain🦜🔗  by building a generative ai application.

This is a web application crawling Linkedin & Twitter data about a person and customizes an ice breaker with them.

![Ice Breaker Demo](https://raw.githubusercontent.com/TuyenTrungLe/ice_breaker/output-parsers-finish/static/img.jpg)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`

`SCRAPIN_API_KEY` 

`TAVILY_API_KEY`

`LANGCHAIN_TRACING_V2`  

`LANGCHAIN_API_KEY` 

`LANGCHAIN_PROJECT` # Optional


To run this project, you will need to add the following environment variables to your .env file:

> **Note**: This project uses paid API services:
> - [Scrapin.io](https://www.scrapin.io/?utm_campaign=influencer&utm_source=github&utm_medium=social&utm_content=edenmarco) for LinkedIn data scraping (20% discount available through this link, includes 20 free credits to start)

> **Important Note**: If you enable tracing by setting `LANGCHAIN_TRACING_V2=true`, you must have a valid LangSmith API key set in `LANGCHAIN_API_KEY`. Without a valid API key, the application will throw an error. If you don't need tracing, simply remove or comment out these environment variables.
## Run Locally

Clone the project

```bash
  https://github.com/TuyenTrungLe/ice_breaker
```

Go to the project directory

```bash
  cd ice_breaker
```

Install dependencies

```bash
  pipenv install
```

Start the flask server

```bash
  pipenv run app.py
```


## Running Tests

To run tests, run the following command

```bash
  pipenv run pytest .
```


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/eden-marco/)
