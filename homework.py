rice_price=15
milk_price=20
fruit_price=10
number_of_baskets=3
family_members=5
basket_cost_per_person=(rice_price+milk_price+fruit_price)*number_of_baskets/family_members
print("this weeks shop costs per person:",basket_cost_per_person)

total_items=int(input("enter the total number of grocery items"))
people=int(input("enter the number of people sharing them"))
if people==0:
    print("you cannot share items between nobody")
else:
    #the divisibility check moves on
    if total_items%people==0:
        print(total_items,"items divide equally among",people,"people-",total_items//people,"each")
    else:
        print(total_items,"items do not divide equally among",people,"people-",total_items%people,"left over")


recorded_average=65
total_weeks=4
wrong_week_cost=50
correct_week_cost=80
recorded_total=recorded_average*total_weeks
corrected_total=recorded_total-wrong_week_cost+correct_week_cost
corrected_average=corrected_total/total_weeks
print("the corrected total is:",corrected_total)
print("the correced average is:",corrected_average)

store_a_average=70
store_b_average=75
store_c_average=80
if corrected_average<store_a_average and corrected_average<store_b_average and corrected_average< store_c_average:
    verdect="cheaper than all 3 stores"
elif corrected_average>store_a_average and corrected_average>store_b_average and corrected_average>store_c_average:
    verdect="more expensive than all 3 stores"
else:
    verdect="somewhere in between the 3 stores"

print("\n ===summary===")
print("cost per person this week:",basket_cost_per_person)
print("corrected weekly average:",corrected_average)
print("verdict",verdect)
