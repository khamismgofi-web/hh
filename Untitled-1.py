class tv_types:
    def __init__ (self,brand,model,size,screen,resolution,price):
        self.brand = brand
        self.model = model
        self.size =  size
        self.screen = screen
        self.resolution = resolution
        self.price = price
        return model,size,screen,resolution,price 

    def tv_specfication(self):
        #print specification
        print("\n--these are our tv specification")
        print(f"brand{self.brand}")
        print(f"modal{self.model}")
        print(f"size{self.size}")
        print(f"screen{self.screen}")
        print(f"resolution{self.resolution}")
        print(f"price{self.price}")
        
    #tv_catalog list    
    tv_catalog = {}
    tv_catalog["samsung"] = ("samsung","QLED 4K","55 inch","1,200,000 Tsh")
    tv_catalog["LG"] = ("LG","OLED C1","65 inch","4k","2,500,000 Tsh")
    tv_catalog["Sony"] = ("Sony","Bravia XR","75inch ","LED","8k","5,000,000 Tsh")
    tv_catalog["qumatix"] = ("qumatix","quat1x","120 cm","gorilla",'2k',"7,000,000 Tsh")
    
def main():
        while True:
            brand = input("Enter your tv choice( or 'quit'): to exist:").strip().lower()
            if brand == "quit":
                break
            if brand in tv_catalog:
                tv_catalog[brand].tv_specification ()
            else:
                print(f"sorry no tv brand found '{brand}' available brands:")
                
if __name__=="__main__":
    main()
            