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
class PersentageView(View):
    def post(self, request):
        data = json.loads(request.body)
        o_m = data.get("obtained_mark")
        t_m = data.get("total_mark")

        persentage = (o_m/t_m)*100

        result = {
            "Persentage":persentage
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