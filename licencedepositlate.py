from web3 import Web3
import json
from time import sleep
#import RPi.GPIO as GPIO

web_3=Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chainid=1377
address=input("Input your address: ")
private_key=input("Input your privatekey:0x")
host="0x97C7A1FEe860a8686cDd0A7F179F17AE36Df92cC"
private_key2="0x9551b3d6dcd1270b15b223204c8a3d3519ccbe31c8997a780549640e2a3fd430"
licence_check = input("Have driving licence? ,yes/no: ")

nonce=web_3.eth.getTransactionCount(address)
nonce2=web_3.eth.getTransactionCount(host)

if licence_check =="yes":
    deposit = input("After confirmation you will have to pay a deposit for 30 ETH, yes/no: ")
    if deposit =="yes":
        pay = {
            'nonce': nonce,
            'to': host,
            'value': web_3.toWei(30, 'ether'),
            'gas': 2000000,
            'gasPrice': web_3.toWei('50', 'gwei')
        }

        #sign the transaction
        signed_pay = web_3.eth.account.sign_transaction(pay, private_key)

        #send transaction
        pay_hash = web_3.eth.sendRawTransaction(signed_pay.rawTransaction)
        print("Deposition succeed")   
    
        day=input("How many days: ")
        if day == "1":
            pay = {
                'nonce': nonce+1,
                'to': host,
                'value': web_3.toWei(5, 'ether'),
                'gas': 2000000,
                'gasPrice': web_3.toWei('50', 'gwei')
            }

            #sign the transaction
            signed_pay = web_3.eth.account.sign_transaction(pay, private_key)

            #send transaction
            pay_hash = web_3.eth.sendRawTransaction(signed_pay.rawTransaction)
            print("You rent 1 day")

        if day == "3":
            pay = {
                'nonce': nonce+1,
                'to': host,
                'value': web_3.toWei(10, 'ether'),
                'gas': 2000000,
                'gasPrice': web_3.toWei('50', 'gwei')
            }

            #sign the transaction
            signed_pay = web_3.eth.account.sign_transaction(pay, private_key)

            #send transaction
            pay_hash = web_3.eth.sendRawTransaction(signed_pay.rawTransaction)
            print("You rent 3 days")
                
        if day == "7":
            pay = {
                'nonce': nonce+1,
                'to': host,
                'value': web_3.toWei(20, 'ether'),
                'gas': 2000000,
                'gasPrice': web_3.toWei('50', 'gwei')
            }

            #sign the transaction
            signed_pay = web_3.eth.account.sign_transaction(pay, private_key)

            #send transaction
            pay_hash = web_3.eth.sendRawTransaction(signed_pay.rawTransaction)
            print("You rent 7 days")
            
        late=input("Did you turn in late?, yes/no: ")
        if late == "yes":
            pay = {
                'nonce': nonce+2,
                'to': host,
                'value': web_3.toWei(5, 'ether'),
                'gas': 2000000,
                'gasPrice': web_3.toWei('50', 'gwei')
            }

            #sign the transaction
            signed_pay = web_3.eth.account.sign_transaction(pay, private_key)

            #send transaction
            pay_hash = web_3.eth.sendRawTransaction(signed_pay.rawTransaction)
            print("You have to pay 5 ETH for turn in late")
                        
        if late == "no":
            pay = {
                'nonce': nonce2,
                'to': address,
                'value': web_3.toWei(30, 'ether'),
                'gas': 2000000,
                'gasPrice': web_3.toWei('50', 'gwei')
            }

            #sign the transaction
            signed_pay = web_3.eth.account.sign_transaction(pay, private_key2)

            #send transaction
            pay_hash = web_3.eth.sendRawTransaction(signed_pay.rawTransaction)
            print("You recieved deposit back")
            
    if deposit =="no":
        print("Deposition failed")
if licence_check =="no":
    print("You don't have permission to drive")
