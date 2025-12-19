@echo off
echo Installing this_project_aims_to_develop_a_backend_api_for_the_hotel_booking_user_interface_designed_with_react_and_vite_as_the_frontend_stack. Backend Dependencies...
echo.
cd /d "%~dp0"
pip install -r requirements.txt
echo.
echo Dependencies installed successfully!
pause