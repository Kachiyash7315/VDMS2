from django.http import HttpResponse
from django.shortcuts import render, redirect

from courses.models import Course, Video, Payment, UserCourse, CouponCode

from OTP_Verification import *
# Create your views here.
import razorpay

from OTP_Verification.settings import *
from time import time
from django.views.decorators.csrf import csrf_exempt

client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))


def checkout2(request, slug):
    print(request.user.is_authenticated)
    course = Course.objects.get(slug=slug)
    user = None
    if request.user.is_authenticated is False:
        return redirect('login')
    user = request.user
    action = request.GET.get('action')
    couponcode = request.GET.get('couponcode')
    couponcodeerror = None
    order = None
    payment = None
    error = None
    amount = None
    coupon = None
    try:
        user_course = UserCourse.objects.get(user=user, course=course)
        error = "You are Already enrolled in this course"
    except:
        pass
    if error is None:
        amount = int((course.price - (course.price * course.discount * 0.01)) * 100)
    if couponcode:
        try:
            coupon = CouponCode.objects.get(course=course, code=couponcode)
            amount = course.price - (course.price * coupon.discount * 0.01)
            amount = int(amount) * 100
        except:
            couponcodeerror = 'Invalid Coupon Code'
            print("Coupon Code Invalid")

    if amount == 0:
        userCourse = UserCourse(user=user, course=course)
        userCourse.save()
        return redirect('mycourses')
    if action == 'create_payment':
        currency = "INR"
        notes = {
            "email": user.email,
            "name": f'{user.first_name} {user.last_name}'
        }
        receipt = f"LinkCode-{int(time())}"
        order = client.order.create({'receipt': receipt, 'notes': notes, 'amount': amount, 'currency': currency})
        payment = Payment()
        payment.user = user
        payment.course = course
        payment.order_id = order.get('id')
        payment.save()

    return render(request, template_name='courses/check_out.html',
                  context={'course': course, 'order': order, 'payment': payment, 'user': user, 'error': error,
                           'couponcodeerror': couponcodeerror, 'coupon': coupon})


@csrf_exempt
def verifyPayment(request):
    if request.method == 'POST':
        data = request.POST
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']
            payment = Payment.objects.get(order_id=razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True;
            userCourse = UserCourse(user=payment.user, course=payment.course)
            userCourse.save()
            payment.user_course = userCourse
            payment.save()
            return redirect('mycourses')
        except:
            return HttpResponse("Invalid Payment Details")
