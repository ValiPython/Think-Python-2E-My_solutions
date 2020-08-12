# "Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy.
#  What is the total wholesale cost for 60 copies?"

b_price = 24.95 #price of a book (the store has -40% discount)

tot_price_disc = (b_price - 2.495 * 4) * 60 #the total price of the books with the -40% discount (2.495 = 10% * 4 = 40% discount)

ship_1 = 3 #shipping cost for the 1st copy

ship_2 = 0.75 #shipping cost for each additional copy (59 copies have this discount)

tot_ship_disc = ship_2 * 59 + ship_1 #total discounted shipping price

total = tot_price_disc + tot_ship_disc #total price of the books (with discount) + total shipping price

print ('The total wholesale cost for 60 copies is:', total, '$') #Rounded is 945.45 $
