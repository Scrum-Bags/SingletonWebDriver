class SingletonWebDriver:

    _instance = None

    driverPath = path.join(
        "C:\\"
        "Program Files",
        "Selenium",
        "WebDrivers"
    )

    def __new__(
        cls, 
        driverObj: Union[WebDriver, str, None] = None,
        **kwargs
    ):
        if cls._instance is None:
            if driverObj == 'Chrome':
                cls._instance = webdriver.Chrome(
                    service=ChromeService(
                        executable_path=path.join(
                            cls.driverPath,
                            "chromedriver.exe"
                        )
                    ),
                    **kwargs
                )
            elif driverObj == 'Edge':
                cls._instance = webdriver.Edge(
                    service=EdgeService(
                        executable_path=path.join(
                            cls.driverPath,
                            "msedgedriver.exe"
                        )
                    ),
                    **kwargs
                )
            elif driverObj is None or driverObj == Firefox:
                cls._instance = webdriver.Firefox(
                    service=FirefoxService(
                        executable_path=path.join(
                            cls.driverPath,
                            "geckodriver.exe"
                        )
                    ),
                    **kwargs
                )
            else:
                cls._instance = driverObj
        return cls._instance
