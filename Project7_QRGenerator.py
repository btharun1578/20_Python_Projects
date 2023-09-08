import qrcode

class MyQRCode():
    def __init__(self, size, padding):
        self.qr=qrcode.QRCode(box_size=size,border=padding)
    
    def create_qr(self,file_name,fg,bg):
        user_input=input("Enter text:")

        try:
            self.qr.add_data(user_input)
            qr_image=self.qr.make_image(fill_color=fg,back_color=bg)
            qr_image.save(file_name)

        except Exception as e:
            print(f"error as {e}")
         
def main():
    myqr=MyQRCode(30,2)
    myqr.create_qr("sample.png","black","white")

if __name__=="__main__":
    main()
