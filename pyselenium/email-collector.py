from time import sleep
from selenium import webdriver
# from selenium.webdriver.common.by import By

# reference
# https://nomade.kr/vod/crawling/57/

def main():
    text_file = open("emails.txt", "w")
    driver = webdriver.Chrome()
    for page in range(1000):
        print page
        driver.get("http://cafe.naver.com/sssw?iframe_url=/sssw/ArticleList.nhn%3Fsearch.clubid=10625158%26search.boardtype=L%26search.questionTab=A%26search.totalCount=151%26search.page=" + str(page))
        print("done!")
        sleep(5)

        driver.switch_to.frame('cafe_main')

        writers = driver.find_elements_by_tag_name('span')
        for writer in writers:
            # print "writer : ", writer
            if writer.get_attribute("id"):
                text_file.write(writer.get_attribute("id").split("_")[1] + "@naver.com" + "\n")



    text_file.close()


if __name__ == "__main__":
    main()
