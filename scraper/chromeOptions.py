from selenium.webdriver.chrome.options import Options
op = Options()
op.add_argument("disable-logging")
op.add_argument("log-level=3")
op.add_extension("scraper/chessKeyboardExtension.crx")

 

"""
The only reason this is here is because if you put anything after that op.add_extension 
vsCode says it's unreachable and grays everything out underneath but it's not and you can still run it and it looks disspleasing and it's annoying so it lives here
"""