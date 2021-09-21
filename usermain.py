from user import bank



michaelAccount= bank(12345, "Michael Miller",5000)
alvaroAccount= bank(22222, "Alvaro Sanchez",2000)
julieAccount= bank(54321, "Julie Sanders",6000)



michaelAccount.deposit(2000)
michaelAccount.deposit(1500)
michaelAccount.deposit(1000)

michaelAccount.withdrawal(500)


alvaroAccount.deposit(2000)
alvaroAccount.deposit(1500)


alvaroAccount.withdrawal(500)
alvaroAccount.withdrawal(500)





julieAccount.deposit(1500)

julieAccount.withdrawal(500)
julieAccount.withdrawal(300)
julieAccount.withdrawal(200)



michaelAccount.display_user_balance()
alvaroAccount.display_user_balance()
julieAccount.display_user_balance()