# https://stackoverflow.com/questions/36141681/does-anybody-know-how-to-identify-shadow-dom-web-elements-using-selenium-webdriv
# https://stackoverflow.com/questions/28911799/accessing-elements-in-the-shadow-dom
"""
<neon-animatable class="layout vertical iron-selected" page="start">
  #shadow-root (open)
  <div class="flex layout vertical center" style="margin:10px">
    <img src="https://ww....." style="max-width:100%">
    <div class="flex" style="max-width:400px">
      <div>.....</div>
"""
from selenium.webdriver import Chrome, ChromeOptions
driver = Chrome()

shadow_section = driver.execute_script('''return document.querySelector("neon-animatable").shadowRoot''')
shadow_section.find_element_by_css(".flex")
