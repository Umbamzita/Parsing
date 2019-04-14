from selenium import webdriver
import base64
import pytesseract
from PIL import Image


class Bot:
    def __init__(self):
        self.driver=webdriver.Firefox()
        self.navigate()
        
    def take_screenshot(self):
        self.driver.save_screenshot('avito_screen.png')
        
    def tel_recon(self):
        screen=Image.open('avito_screen2.png')
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text = pytesseract.image_to_string(screen)
        print(text)
      
        
            
    def navigate(self):
        self.driver.get('https://www.avito.ru/moskva/telefony/ayfon_7_32gb_1520254215')
        
        button=self.driver.find_element_by_class_name('item-phone')
        
        button.click()
        image = self.driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]/img')
        
        image_src=image.get_attribute('src').split(',')[1]
        
        img = base64.decodebytes(bytearray(image_src, 'utf-8'))
        
        with open("avito_screen2.png", "wb") as f:
            
            f.write(img)
        self.tel_recon()     
        
        #self.take_screenshot()


def main():
    b = Bot()


if __name__=='__main__':
    main()
