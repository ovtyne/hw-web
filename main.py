from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


# Определяем настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
        Класс, который отвечает за обработку входящих запросов
    """
    def get_html_content(self):
        with open('0.html', encoding='utf-8') as page:
            content = page.read()
        return content

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        query_components = parse_qs(urlparse(self.path).query)
        page_content = self.get_html_content()
        print(query_components)
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа


if __name__ == "__main__":
    """
    Инициализация веб-сервера, который будет по заданным параметрам в сети 
    принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    """
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        """ Старт веб-сервера в бесконечном цикле прослушивания входящих запросов """
        webServer.serve_forever()
    except KeyboardInterrupt:
        """Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C"""
        pass

# Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, который занимал
webServer.server_close()
print("Server stopped.")
