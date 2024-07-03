from selenium.webdriver.common.by import By

class HomePageLocators:

    ORDER_HEADER = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']") #кнопка заказа в шапке лединга
    ORDER_PAGE = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']") #кнопка заказа в теле главной страницы
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]") #логотип "Яндекс" в шапке лединга
    LOGO_SAMOKAT = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]") #логотип "Самокат" в шапке лединга
    COOKIES_BUTTON = (By.ID, "rcc-confirm-button")  #кнопка "Да" в сообщении о куки
    QUESTION_LIST = (By.XPATH, "//div[@id = 'accordion__heading-{}']")  #вопросы выпадющего списка
    ANSWER_LIST = (By.XPATH, '//div[@id="accordion__panel-{}"]/p') #ответы выпадающего списка
    LAST_QUESTION = (By.XPATH, "(//div[contains(@id,'accordion__heading-')])[last()]") #последний вопрос

