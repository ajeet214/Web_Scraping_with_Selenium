from selenium.webdriver import ChromeOptions
options = ChromeOptions()

# maximized and disable forbar
options.add_argument("--start-maximized")
options.add_argument("--incognito")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extension")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")

options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("detach", True)

options.add_experimental_option(
    "prefs",
    {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
        # with 2 should disable/block notifications and 1 to allow
    },
)




