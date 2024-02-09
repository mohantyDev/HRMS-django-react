from . import views
from django.urls import path
from .views import getAllEmployees,add_employee_view,update_user,add_holiday
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'api'

urlpatterns = [
    path('user/register/',views.RegisterView.as_view(),name="register"),
    path('user/login/',views.LoginAPIView.as_view(),name="login"),
    path('user/logout/', views.LogoutAPIView.as_view(), name="logout"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('send-otp/', views.send_otp, name='send-otp'),
    path('user/confirm-otp/', views.confirm_otp, name='confirm-otp'),
    path('user/reset-password/', views.reset_password_view, name='reset-password'),
    path('api/add-employee/', add_employee_view, name='add-employee'),
    path('api/add-designation/', views.addDesignation, name='addDesignation'),
    path('api/add-department/', views.addDepartment, name='addDepartment'),
    path('api/get_all_employees/',getAllEmployees, name = 'getAllEmployees'),
    path('api/update_user/',update_user, name="update_user"),
    path('api/deactivate_user/',views.deactivate_user, name="deactivate_user"),
    path('api/users/', views.user_detail_view, name='user-detail'),
    path('api/get_particular_employee_data/',views.get_particular_employee_data, name='get_particular_employee_data'),
    path('api/add_leave/', views.add_leave, name='add_leave'),
    path('api/get_all_designations/', views.getAllDesignations, name='getAllDesignations'),
    path('api/get_all_departments/', views.getAllDepartments, name='getAllDepartments'),
    path('api/update_designation/', views.updateDesignation, name='updateDesignation'),
    path('api/update_department/', views.updateDepartment, name='updateDepartment'),
    path('api/delete_designation/', views.deleteDesignation, name='deleteDesignation'),
    path('api/delete_department/', views.deleteDepartment, name='deleteDepartment'),
    path('api/process_leave/', views.process_leave, name='process_leave'),
    path('api/get_employee_leave_data/', views.get_employee_leave_data, name='get_employee_leave_data'),
    path('api/leave_history/', views.get_leave_history, name='leave_history'),
    path('api/add_holiday/', add_holiday, name='add-holiday'),
    path('api/get_holidays/', views.get_holidays, name='get-holidays'),
    path('api/punch-in/',views.punch_in_view, name = "punch_in"), # added by Nageswara and Saikiran
    path('api/punch-out/',views.punch_out_view,name= "punch_out"), # added by D Hari
    path('api/currentDayAttendanceActivity/', views.currentDayAttendanceActivity, name = "currentDayAttendanceActivity"),
    path('api/get_attendance_data/', views.get_attendance_data, name = "get_attendance_data"),
    path('api/upload_profilePic/',views.profilePicApi,name= "profilePicApi"),
    path('api/get_all_ReportingManagers/',views.get_all_ReportingManagers,name= "get_all_ReportingManagers"),
    path('api/currentLeaves/',views.currentLeaves,name= "currentLeaves"),
    path('api/generate_payslip/', views.generate_payslip, name = "generate_payslip"),
    path('api/bulk_payslip_generation/', views.bulkPayslipGeneration, name = "bulkPayslipGeneration")
]