from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Launch the web browser
driver = webdriver.Chrome()  
driver.maximize_window()



#----------------TC-1

# Navigate to the URL
url = "https://rapsodo.com/"
driver.get(url)

# Wait until the URL matches the expected value
wait = WebDriverWait(driver, 3)  # Wait for a maximum of 3 seconds
expected_url = "https://rapsodo.com/"  # Expected URL

try:
    wait.until(ec.url_to_be(expected_url))
    print("User successfully navigated to", expected_url)
except:
    print("User failed to navigate to", expected_url)
 
# Verify the current URL
current_url = driver.current_url

if current_url == url:
    print("User successfully navigated to", url)
else:
    print("User failed to navigate to", url) 



#------------------TC-2

clickCart= driver.find_element(By.XPATH, "//*[@id='SiteHeader']/div[1]/div/div[3]/div/div/a[2]/span/img")
clickCart.click()
verifyMessage = driver.find_element(By.XPATH, "//*[@id='shopify-section-template--15875117514901__main']/div/header/div/p[1]")
verifyMessageResult= verifyMessage.text == "Your cart is currently empty."
print(f"VerifyCheck: {verifyMessageResult}")

#------------------TC-3
#shop dropdown menu appear
ShopIcon = driver.find_element(By.XPATH, "//*[@id='SiteHeader']/div[1]/div/div[2]/ul/li[5]/span")
ActionChain = ActionChains(driver) 
ActionChain.move_to_element(ShopIcon) 
#ActionChain.click() 
ActionChain.perform()
sleep(3)
#click Golf Button
GolfButton = driver.find_element(By.XPATH, "//*[@id='SiteHeader']/div[1]/div/div[2]/ul/li[5]/div/div[1]/a") 
GolfButton.click() 
scroll_unit = 500
driver.execute_script(f"window.scrollBy(0, {scroll_unit});") 
sleep(3)
#choose MLM
viewMLM = driver.find_element(By.XPATH, "//*[@id='CollectionAjaxContent']/div/div/div[2]/div/div/div[2]/div[2]") 
ActionChain = ActionChains(driver) 
ActionChain.move_to_element(viewMLM)
ActionChain.perform()
sleep(3)
#click view product
clickViewProduct= driver.find_element(By.XPATH, "//*[@id='CollectionAjaxContent']/div/div/div[2]/div/div/div[2]/div[2]/div/a")
clickViewProduct.click()
scroll_unit = 400
driver.execute_script(f"window.scrollBy(0, {scroll_unit});") 
screenPriceMLM= driver.find_element(By.CLASS_NAME, "R-MlmProStickyPriceText").text
#verifying title
sleep(3)
page_title = driver.title
expected_title = "Rapsodo® Mobile Launch Monitor | Golf MLM | Buy Online @ Rapsodo® Official Site" 
assert page_title == expected_title, f"Page title is not as expected. Actual: {page_title}, Expected: {expected_title}" 


#-----------------TC-4

clickAddToCart= driver.find_element(By.ID, "AddToCartNormal")
sleep(1)
clickAddToCart.click()


verifyMessage = driver.find_element(By.CLASS_NAME, "section-header__title")
verifyMessageResult= verifyMessage.text == "Cart"
print(f"VerifyCheck: {verifyMessageResult}")



priceMLM= driver.find_element(By.CLASS_NAME, "cart__price").text
assert screenPriceMLM == priceMLM, f"Values are not equal . ProductPrice: {priceMLM}, ScreenPrice: {screenPriceMLM}" 
sleep(2)

productTotal= driver.find_elements(By.TAG_NAME, "data-subtotal")

clickIncreaseButton= driver.find_element(By.XPATH, "//*[@aria-label='Increase item quantity by one']")
sleep(2)
clickIncreaseButton.click()


#----------------TC-5

#The user increases quantity ( quantity = 2 )
productQuantity= 2
productTotal= driver.find_elements(By.TAG_NAME, "data-subtotal")
for element in productTotal:
    print(element.text)
priceMLM=priceMLM.replace("$", "")
result= float(priceMLM)*productQuantity
assert productTotal == result, f"Values are not equal . ProductPrice: {productTotal}, ScreenPrice: {result}" 

sleep(2)

#The user verifies that there are two items
updated_price_element = wait.until(ec.text_to_be_present_in_element((By.TAG_NAME, "data-subtotal"), "Güncel Fiyat"))

updated_price = updated_price_element.text 
print(updated_price)


# close Selenium WebDriver
driver.quit()