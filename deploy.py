from solcx import compile_standard, install_solc
import json
from web3 import Web3
import RPi.GPIO as GPIO
from time import sleep
import drivers



display = drivers.Lcd()

display.lcd_display_string("Waiting for", 1)
display.lcd_display_string("Transaction", 2)
#for connect ganache
w3=Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/06576ddc7bda463d9af9c93aa9148ab6")) #เชื่อมกับ http ของ rinkerby จากเว็บ infura โดยเราcreat project ขึ้นมาเอง
chain_id =4 #เลือกใช้ 4 เพราะเราเลือกใช้ rinkerby test net ซึ่งrinkerby มี chain id =4
my_address="0x7E69CD8E64cCaa37f44E89d84eCc5703D88214fc" #address ของ user ที่เราใช้ในการโอนเงิน
private_key="0x9df3327fb74a09982d4d0b2f3f37a55eab5ad4b730e81d3a64fc259c577f6d7c" #privatekeyของ Address ของคนที่จะส่งเงิน ต้องเพื่ม 0x ข้างหน้า
owner_address=input("Enter Owner Id: ")# ใส่ Address ของ ปลายทางผู้รับเงิน

password=input("Please enter your password:")
if password=="5555":
    print("Please wait transaction pending")
    display.lcd_clear()   
    display.lcd_display_string("Please wait", 1)
#สร้าง contract 

#get latestest transaction
    nonce=w3.eth.getTransactionCount(my_address)
#สร้่าง transaction


#use contract

    balance = w3.eth.getBalance(my_address);
    balance_currently=(int(balance)/(10**18))
    print("You balance=",balance_currently,"ETH")
    display.lcd_clear()   
    display.lcd_display_string("You balance=", 1)
    display.lcd_display_string(f"{round(balance_currently,2)}", 2)

    value=input("Please Enter Value in ETH unit (minimum is 1 ETH): ")
    if value=="1":
            
        ts = {
            'nonce': nonce,
            'to': owner_address,
            'value': w3.toWei(value, 'ether'),
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei')
        }

        #sign the transaction
        signed_ts = w3.eth.account.sign_transaction(ts, private_key)

        #send transaction
        ts_hash = w3.eth.sendRawTransaction(signed_ts.rawTransaction)

        #get transaction hash
        print("You Send",value,"ETH from",my_address,"to",owner_address)
        display.lcd_clear()   
        display.lcd_display_string(f"You send: {value}", 1)
        print("Use this hash to check on Etherscan.io :",w3.toHex(ts_hash))

        balance_to_eth=(int(balance)/(10**18))-float(value)
        print("Your Balance after transaction=",balance_to_eth,"ETH")
        display.lcd_clear()   
        display.lcd_display_string("Your Balance", 1)
        display.lcd_display_string(f"{balance_to_eth} ETH", 2)
        sleep(3)
        display.lcd_clear()   
        display.lcd_display_string("Thank you", 1)
        print("Thank you")
        sleep(5)
        display.lcd_clear()  

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        while (True):    
                
                
            GPIO.output(18, 1)
                
            sleep(1)
    else:
        print("You need to pay 1 ETH to unlock")
        display.lcd_clear()   
        display.lcd_display_string("You need to pay", 1)
        display.lcd_display_string("1 ETH to unlock", 2)
        sleep(5)
        display.lcd_clear()  

else:
    print("Wrong password")
    display.lcd_clear()   
    display.lcd_display_string("Wrong password", 1)
    sleep(5)
    display.lcd_clear()  
