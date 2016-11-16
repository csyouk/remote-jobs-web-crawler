- 문제의 핵심은 ajax 통신이 있는 web application 의 웹페이지를 
그대로 snap-shot을 해서 크롤링을 할 수 있느냐이다.
- [Quora에 올라온 글]을 보면 딱히 해결책이 있어보이진 않는다.(https://www.quora.com/How-do-I-crawl-a-website-that-loads-content-lazily)
- quora에 올라온 글에 따르면 selenium을 통해서 웹브라우저를 제어하는 형식으로 컨텐츠를 얻어오는 방식으로 해야할 것 같다.
- 하지만 [이 글] 에 적혀진 코드는 환경이 달라서인지, 작동하지 않는다.(http://www.tidbitsofprogramming.com/2014/02/crawling-website-that-loads-content.html)
- [Google 에서 작성한 글]도 Deprecated된 상태이다.(https://developers.google.com/webmasters/ajax-crawling/docs/getting-started)
- ajax application을 크롤링 할 수 있는 프로젝트들이 몇몇 개 보이긴 하지만, 문서화 상태가 영 좋지 않다. python을 쓰지 않는다.


## Dependencies
- selenium(using pip)
- webdriver(using brew)