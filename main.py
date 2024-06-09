from serpapi import GoogleSearch
import re
from bs4 import BeautifulSoup
import requests
import openai
import tika
from tika import parser
import os
import json
import pychrome
import time
from parsel import Selector


def fetchResults(query):
    allResults = []
    for i in range(5):
        params = {
            "engine": "google_scholar",
            "q": query,
            "api_key": "7d3fd555b201b405e741d8cd7ba50c6fb865294d7835b5186ec235452699dd6b",
            "start": i * 20,
            "num": 20,
        }

        search = GoogleSearch(params)
        results = search.get_dict()["organic_results"]
        for result in results:
            if (
                "type" not in result
                or result["type"].lower() == "html"
                or result["type"].lower() == "pdf"
            ):
                if "type" not in result:
                    result["type"] = "none"
                    if "resources" in result:
                        if "file_format" in result["resources"]:
                            result["type"] = result["resources"]["file_format"].lower()

                allResults.append(
                    {
                        "title": result["title"],
                        "link": result["link"],
                        "snippet": result["snippet"],
                        "type": result["type"].lower(),
                        "score": GPT_Score(query, result["snippet"]),
                    }
                )
    with open("data.json", "w") as file:
        file.write(re.sub(r"[^\x00-\x7F]+", "", str(allResults)))
    return allResults


def GPT_Score(query, snippet):
    openai.api_key = "sk-proj-rz41fRHeworEqjeCCrvHT3BlbkFJCBSn8gHWikmJ6ykRAs3f"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Give A Score (Provide Only A One Score Out Of (0-100), No Analysis, No Other Characters Than The Number) Of Similarity Between A Topic And Of A Research Paper (From A Snippet), Based Of These Factors: Relevance to the Topic (Should Be In The Same Domain, Ex: Chemistry Topic And Chemistry Paper, Not CS Topic And Chemistry Paper), Specificity (e.g., inclusion of specific case studies), Presence of key terms from the search query in the paper",
            },
            {"role": "user", "content": f"Topic: {query}, Paper Snippet: {snippet}"},
        ],
    )
    score = str(response.choices[0].message.content)
    score = score.split()
    return int(score[-1])


def basicWebScrape(url):
    visistedAbsOrIntro = False
    extractedTexts = [["0. Abstract", ""]]
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all("p")
    paragraphsList = []
    for i in range(len(paragraphs)):
        if re.findall(r"^\d+\.\s+.*\d{4}.*$", paragraphs[i].text) != []:
            break
        if paragraphs[i].find("b") or paragraphs[i].find("strong"):
            if visistedAbsOrIntro:
                extractedTexts.append([" ", " "])
                extractedTexts[-1][0] = str(paragraphs[i].get_text())
            else:
                if (str(paragraphs[i].get_text()).lower()).strip() == "abstract" or (
                    str(paragraphs[i].get_text()).lower()
                ).strip() == "introduction":
                    visistedAbsOrIntro = True
        if re.findall(r"^\d+\.\s+[\w\s]+$", paragraphs[i].text) != []:
            extractedTexts.append([" ", " "])
            extractedTexts[-1][0] = re.findall(
                r"^\d+\.\s+[\w\s]+$", paragraphs[i].text
            )[0]
        paragraph = paragraphs[i].get_text()
        extractedTexts[-1][1] += paragraph
    return extractedTexts


# If We Had More Time, We Would Have Been Able To Use This To Scrape More Websites (Which Were Blocking BS4)
def complexWebScrape(url):
    browser = pychrome.Browser(url="http://127.0.0.1:9222")
    tab = browser.new_tab()

    try:
        tab.start()
        tab.Page.navigate(url=url, _timeout=5)
        time.sleep(5)
        html_content = tab.Runtime.evaluate(
            expression="document.documentElement.outerHTML"
        )
        html_content = str(html_content).replace("\u23fd", "")
        selector = Selector(text=html_content)
        paragraph_texts = selector.xpath("//body//p/text()").getall()
        joined_text = " ".join(paragraph_texts)
    finally:
        tab.stop()
        browser.close_tab(tab)
    return joined_text


def pdfScrape(pdf_url):
    tika.initVM()

    response = requests.get(pdf_url)
    pdf_file = "assets/document.pdf"

    with open(pdf_file, "wb") as file:
        file.write(response.content)

    parsed_pdf = parser.from_file("assets/document.pdf")
    data = parsed_pdf["content"]
    os.remove("assets/document.pdf")
    paragraphs = data.split("\n")

    extractedTexts = [["Abstract", ""]]
    visistedAbsOrIntro = False
    for i in range(len(paragraphs)):
        if re.findall(r"^\d+\.\s+.*\d{4}.*$", paragraphs[i]) != []:
            break
        if (
            re.findall(r"^\d+\.\s+[\w\s]+$", paragraphs[i]) != []
            and len(paragraphs) > 1500
        ):
            extractedTexts.append([" ", " "])
            extractedTexts[-1][0] = re.findall(r"^\d+\.\s+[\w\s]+$", paragraphs[i])[0]
            print(paragraphs[i])
        elif re.findall(r"^\d+\.\d+\s+[\w\s]+$", paragraphs[i]) != []:
            extractedTexts.append([" ", " "])
            extractedTexts[-1][0] = re.findall(r"^\d+\.\d+\s+[\w\s]+$", paragraphs[i])[
                0
            ]
            print(paragraphs[i])
        elif re.findall(r"^\d+\s+[A-Za-z\s]+$", paragraphs[i]) != []:
            extractedTexts.append([" ", " "])
            print(paragraphs[i])
            extractedTexts[-1][0] = re.findall(r"^\d+\s+[A-Za-z\s]+$", paragraphs[i])[0]
        paragraph = paragraphs[i]
        extractedTexts[-1][1] += paragraph
    return extractedTexts


def GPT_Summarizing(extractedText):
    summarizedText = []

    openai.api_key = "sk-proj-rz41fRHeworEqjeCCrvHT3BlbkFJCBSn8gHWikmJ6ykRAs3f"

    for i in range(len(extractedText)):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Summarize This Section Of A Research Paper, Create A Bullet Point Summary And Be Detailed (5 Bullet Point Cap). Focus Only On The Research Paper Content And Not On Other Features Of The Website",
                },
                {"role": "user", "content": extractedText[i][1]},
            ],
        )
        message = str(response.choices[0].message.content).split("- ")
        message = [x.strip() for x in message]
        summarizedText.append([extractedText[i][0], message])

    return summarizedText


def getReponse(title):
    try:
        title = title[:-1]
        type = ""
        link = ""
        text = ["", ""]
        with open("data.json", "r") as file:
            data = json.load(file)
        for entry in data:
            if entry["title"] == title:
                link = entry["link"]
                type = entry["type"]
        if type == "pdf":
            text = pdfScrape(link)
        if type == "html":
            text = basicWebScrape(link)
        if type == "none":
            text = basicWebScrape(link)
            if text[0][1] == "":
                text = pdfScrape(link)
            if text[0][1] == "":
                return "failure" + text
        response = GPT_Summarizing(text)
        return [title, link, type, response]
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")