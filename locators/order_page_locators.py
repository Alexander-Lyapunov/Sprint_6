from selenium.webdriver.common.by import By

class OrderPageLocators:
    FIELD_NAME = (By.XPATH, "//input[@placeholder='* Имя']") #поле "Имя" в форме "Для кого самокат"
    FIELD_LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']") #поле "Фамилия" в форме "Для кого самокат"
    FIELD_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") #поле "Адрес:куда привезти заказ" в форме "Для кого самокат"
    FIELD_METRO = (By.XPATH, '//input[@placeholder="* Станция метро"]') #поле "Станция метро" в форме "Для кого самокат"
    FIELD_PHONE = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']") #поле "Телефон: на него позвонит курьер" в форме "Для кого самокат"
    BUTTON_NEXT_ORDER = (By.XPATH, "//button[text()='Далее']") #кнопка "Далее" в форме "Для кого самокат"
    FIELD_DATE = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']") #поле "Когда привезти самокат" в форме "Про аренду"
    FIELD_PERIOD_RENT = (By.XPATH, "//div[text()='* Срок аренды']") #поле "Срок аренды" в форме "Про аренду"
    RENT_PERIOD_DAY = (By.XPATH, '//div[text()="сутки"]')  # минимальный срок аренды (сутки) в поле "Срок аренды" в форме "Про аренду"
    BLACK_SAMOKAT = (By.ID, "black") #выбор чёрного цвета самоката в форме "Про аренду"
    FIELD_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") #поле "Комментарий для курьера" в форме "Про аренду"
    BUTTON_ORDER = (By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]') #кнопка "Заказать" в форме "Про аренду"
    BUTTON_YES = (By.XPATH, "//button[text()='Да']") #кнопка "Да" в всплывающем окне "Хотите оформить заказ?"
    ORDER_SUCCESS = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]") #окно успешного заказа
