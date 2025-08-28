from django.shortcuts import render,redirect
from .import models,forms
from django.views.generic import ListView,UpdateView,DeleteView,CreateView   # ✅ Add this import
from django.urls import reverse_lazy
#messeage portion
from django.contrib import messages
from django.shortcuts import render, redirect

def create(request):  #function based view
    form = forms.StudentForm()  # প্রথমে খালি ফর্ম তৈরি করলাম
    
    if request.method == 'POST':  # ইউজার যদি POST রিকোয়েস্ট পাঠায় (মানে ডাটা সাবমিট করে)
        form = forms.StudentForm(request.POST, request.FILES)  # ফর্মে ইউজারের ইনপুট বসাচ্ছি
        if form.is_valid():  # ফর্মের ডাটা ঠিক আছে কিনা চেক করবো
            form.save()  # ডাটা ডাটাবেসে সেভ করলাম
            messages.add_message(request, messages.SUCCESS, 'profile create successfully.')  # সাকসেস মেসেজ দেখাচ্ছি
            return redirect('home')  # হোম পেজে রিডাইরেক্ট
    
    else:
        form = forms.StudentForm()  # GET রিকোয়েস্টে খালি ফর্ম দেখানো হবে
        return render(request, 'student/create_student.html', {'form': form})

    
    
class createStudent(CreateView):  # Django-এর বিল্ট-ইন CreateView ব্যবহার করছি  this is class based view
     form_class = forms.StudentForm  # কোন ফর্ম ইউজ করবে সেটা বলে দিচ্ছি
     template_name = 'student/create_student.html'  # কোন টেমপ্লেট শো করবে
     success_url = reverse_lazy('home')  # সাকসেস হলে কোথায় যাবে

     def form_valid(self, form):  # ফর্ম valid হলে কী করবে
        messages.add_message(self.request, messages.SUCCESS, 'profile create successfully.')  # সাকসেস মেসেজ
        return super().form_valid(form)  # parent class-এর form_valid কল করলাম (ডাটা সেভ করবে)

     
     
# def home (request):    #This function based view instade of class based view
#     students = models.student.objects.all()
#     return render(request,'student/index.html',{'students':students})        


class StudentLists(ListView): #this is class based views alternative of home
    model = models.student
    template_name = 'student/index.html'
    context_object_name = 'students'
    

    
    

# def update_student(request, id):  #function based view
#     student = models.student.objects.get(id=id)  # id দিয়ে student টা database থেকে বের করলাম
#     form = forms.StudentForm(instance=student)   # আগের ডেটা সহ form টা দেখাচ্ছি

#     if request.method == 'POST':   # যদি user ফর্ম সাবমিট করে
#         form = forms.StudentForm(request.POST, request.FILES, instance=student)  # ফর্মের ডেটা নিয়ে আপডেট করবো
#         if form.is_valid():   # ফর্ম ভ্যালিড হলে
#             form.save()  # ডেটা ডাটাবেজে সেভ করলাম
#             messages.add_message(request, messages.SUCCESS, 'Profile updated successfully.') # সাকসেস মেসেজ দেখালাম
#             return redirect('home')  # হোমপেজে রিডাইরেক্ট করলাম
    
#     return render(request, 'student/create_student.html', {'form': form, 'edit': True})  # ফর্ম আবার show করবো


class UpdateStudentData(UpdateView):  # class base view
    pk_url_kwarg = 'id'  # URL থেকে যে parameter আসবে সেটা হলো id
    form_class = forms.StudentForm  # কোন form ব্যবহার করবে
    model = models.student  # কোন model এর data update করবে
    template_name = 'student/create_student.html'  # কোন template show করবে
    success_url = reverse_lazy('home')  # সফল হলে কোথায় redirect করবে

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Profile updated successfully.')  # success message
        return super().form_valid(form)  # parent method কল করা হলো (update save হবে)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # default context আনলো
        context['edit'] = True  # template এ জানানো হলো update mode এ আছে
        return context

            
def delete_student(request, id):
    student = models.student.objects.get(id=id)  # id দিয়ে student অবজেক্ট বের করলাম
    student.delete()  # ডাটাবেজ থেকে ডিলিট করলাম
    messages.add_message(request, messages.SUCCESS, 'Profile deleted successfully.') # ডিলিট হওয়ার পর মেসেজ দেখাবে
    return redirect('home')  # হোম পেজে রিডাইরেক্ট করবে



class deleteStudent(DeleteView):
    model = models.student  # কোন model এর ডেটা ডিলিট হবে
    pk_url_kwarg = 'id'  # URL থেকে কোন parameter দিয়ে object খুঁজবে
    success_url = reverse_lazy('home')  # ডিলিট হওয়ার পর কোথায় যাবে
    template_name = 'student/conferm_delete.html'  # কনফার্ম ডিলিট পেজ দেখাবে

    def delete(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, 'Profile deleted successfully.') # মেসেজ দেখাবে
        return super().delete(request, *args, **kwargs)

    
# def create_student(request):
#     if request.method == 'POST':
#         name = request.POST.get('userName')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         checkbox = request.POST.get('checkboxs')
#         age = request.POST.get('age')
#         roll = request.POST.get('roll')
#         # photo = request.ImageField(upload_to = 'photo',null=True,blank=True)
#         photo = request.FILES.get('photo')
        
#         if checkbox == 'on':
#             checkbox = True
#         else:
#             checkbox = False
            
#         student = models.student(name=name,roll=roll,phone=phone,email=email,age=age,password=password,checkbox=checkbox,photo=photo)
#         student.save()
#         return HttpResponse('profile created successfully')
#     return render(request,'student/create_student.html')