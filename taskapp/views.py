from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@method_decorator(csrf_exempt,name="dispatch")
class BMIview(View):
    def post(self, request):
        data = json.loads(request.body)
        h = data.get("height")
        w = data.get("weight")

        #convert height from cm to meter

        height = h/100

        #calculate BMI
        bmi = w / (height**2)

        result ={
            "height": h,
            "weight": w,
            "BMI" : round(bmi,2)       
            }
        return JsonResponse(result)



@method_decorator(csrf_exempt,name="dispatch")
class AgeView(View):
    def post(self, request):
        data = json.loads(request.body)
        b_y = data.get("birth_year")
        c_y = data.get("current_year")

        current_age = c_y - b_y

        result = {
            "Age": current_age
        }
        return JsonResponse(result)        


@method_decorator(csrf_exempt,name="dispatch")
class PercentageView(View):
    def post(self, request):
        data = json.loads(request.body)
        o_m = data.get("obtained_mark")
        t_m = data.get("total_mark")

        percentage = (o_m/t_m)*100

        result = {
            "Percentage":percentage
        }
        return JsonResponse(result)



@method_decorator(csrf_exempt,name="dispatch")
class IntrestView(View):
    def post(self, request):
        data = json.loads(request.body)
        p = data.get("principal")
        r = data.get("rate")
        t = data.get("time")

        SimpleIntrest = (p*r*t)/100

        result = {
            "principal": p,
            "rate": r,
            "time": t,
            "SimpleIntrest" : SimpleIntrest
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name="dispatch")
class ElectricityBill(View):
    def post(self, request):
        data = json.loads(request.body)
        u = data.get("unit")
        r = data.get("rate")

        Bill =  u*r

        result = {
             "unit": u,
             "rate": r,
             "Bill" : Bill
        }
        return JsonResponse(result)


@method_decorator(csrf_exempt,name="dispatch")
class DiscountView(View):
    def post(self, request):
        data = json.loads(request.body)
        p = data.get("price")
        d_p = data.get("discount_percentage")

        d_a =  (p*d_p)/100

        final_price = p - d_a

        result = {
            "price" : p,
            "discount percentage" : d_p,
            "Discount Amount" : d_a,
            "Final price" : final_price
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name="dispatch")
class SalaryView(View):
    def post(self, request):
        data = json.loads(request.body)
        b_s = data.get("basic_salary")
        b = data.get("bonus")
        d = data.get("deduction")

        net_salary = b_s + b - d

        result = { 
            "basic_salary": b_s,
            "bonus" : b,
            "deduction": d,
            "Net_Salary" : net_salary
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name="dispatch")
class ProfitView(View):
    def post(self, request):
        data = json.loads(request.body)
        c = data.get("cost_price")
        s = data.get("selling_price")

        profit = s - c

        result = {
            "cost_price": c,
            "selling_price": s,
            "Profit" : profit
        }
        return JsonResponse(result)


@method_decorator(csrf_exempt,name="dispatch")
class TimeView(View):
    def post(self, request):
        data = json.loads(request.body)
        hours =  data.get("hours")

        min = hours * 60
        sec = hours * 3600

        result = {
            "Hours" : hours,
            "Minutes" : min,
            "Seconds" : sec
        }
        return JsonResponse(result)


@method_decorator(csrf_exempt,name="dispatch")
class FuelCostView(View):
    def post(self, request):
        data = json.loads(request.body)
        d = data.get("distance")
        m = data.get("mileage")
        f = data.get("fuel_price")

        fuel = d/m
        Total_Cost = fuel * f 

        result = {
               "distance": d,
               "mileage": m,
               "fuel_price": f,
               "fuel_required": fuel,
                "total_cost": Total_Cost
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name="dispatch")
class ProdectProfit(View):
    def post(self, request):
        data = json.loads(request.body)
        cost = data.get("cost_price")
        sell = data.get("selling_price")
        q = data.get("quantity")

        Total_cost = cost * q
        Total_sales = sell * q
        Profit = Total_sales - Total_cost

        result = {
            "cost_price": cost,
             "selling_price": sell,
             "quantity": q,
             "total_cost": Total_cost,
             "total_sales": Total_sales,
             "profit": Profit
        }
        return JsonResponse(result)



@method_decorator(csrf_exempt,name="dispatch")
class WorkSalary(View):
    def post(self, request):
        data = json.loads(request.body)
        h_w = data.get("hours_worked")
        r_h = data.get("regular_hours")
        h_r = data.get("hourly_rate")
        o_r = data.get("overtime_rate")

        Regular_pay = r_h * h_r
        Overtime_hours = h_w - r_h
        Overtime_pay = Overtime_hours * o_r
        Total_salary = Regular_pay  + Overtime_pay

        result = {
            
 "hours_worked": h_w,
 "regular_hours": r_h,
 "hourly_rate": h_r,
 "overtime_rate": o_r,
 "regular_pay": Regular_pay,
 "overtime_hours": Overtime_hours,
 "overtime_pay": Overtime_pay,
 "total_salary": Total_salary

        }
        return JsonResponse(result)


@method_decorator(csrf_exempt,name="dispatch")
class AgeCalculate(View):
    def post(self, request):
        data = json.loads(request.body)
        age = data.get("age")

        Months = age * 12
        Weeks = age * 52
        Days = age * 365

        result = {
            "age": age,
 "months": Months,
 "weeks": Weeks,
 "days": Days
        }
        return JsonResponse(result)