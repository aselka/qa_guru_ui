## Проект UI автотестов demoqa.com

<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="./attachments/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="./attachments/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="./attachments/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="./attachments/logo/selene.png"></code>
  <code><img width="5%" title="GitHub" src="./attachments/logo/github.png"></code>
  <code><img width="5%" title="Allure Report" src="./attachments/logo/allure_report.png"></code>
  <code><img width="5%" title="Jenkins" src="./attachments/logo/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="./attachments/logo/selenoid.png"></code> 
  <code><img width="5%" title="Telegram" src="./attachments/logo/tg.png"></code>
</p>

### Что выполняет тест:
- [x] Заполняет данные формы
- [x] Отправляет заполненные данные
- [x] Проверяет правильность заполненных данных

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="attachments/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/qa_guru_ui/)

##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение, через виртуальную машину при помощи Selenoid.
![This is an image](attachments/screenshots/jenkins.png)

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="attachments/logo/allure_report.png"> Allure report

##### После прохождения тестов, результаты автоматически сохраняются. Чтобы посмотреть Allure отчет нужно нажать на иконке allure report у сборки.
![This is an image](attachments/screenshots/allure.png)

##### Во вкладке Suites находятся подробные данные о прохождении теста с приложенными логами, скриншотами и видео о прохождении теста
![This is an image](attachments/screenshots/allure_suites.png)

##### Скриншот прохождение теста
![This is an image](attachments/screenshots/screen_tests.png)

##### Видео прохождение теста
![This is an image](attachments/video/tests_ui.gif)

<!-- Telegram -->

### <img width="3%" title="Telegram" src="attachments/logo/tg.png"> Telegram

##### Настроила телеграм-бота, после прохождения тестов в Jenkins присылает уведомление с отчетом в Телеграм

##### Скриншот отчета в телеграм
![This is an image](attachments/screenshots/telegram.png)
