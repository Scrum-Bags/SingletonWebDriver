from typing import Union

from selenium.webdriver.remote.webdriver import WebDriver


class SingletonWebDriver:

    _instance = None

    def __new__(
        cls, 
        driverObj: Union[WebDriver, None] = None,
        **kwargs
    ):
        if cls._instance is None:
            if driverObj is None:
                raise ValueError("Need initializing webdriver object")
                return None
            else:
                cls._instance = driverObj
        elif driverObj is not None:
            raise ValueError("Singleton Web Driver already initialized!")
        return cls._instance
