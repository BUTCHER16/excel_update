# views.py
import pandas as pd
from django.shortcuts import render, redirect
from .forms import UploadExcelForm
from .models import MyModel

def upload_excel(request):
    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file,)

            print(df.head())

            # Process the DataFrame and save to the database
            for _, row in df.iterrows():
                # Create and save a model instance
                MyModel.objects.create(
                    name=row['NAME'],  # Adjust according to your DataFrame columns
                    dept=row['DEPT'],  # Adjust according to your DataFrame columns
                    model=row['MODEL'],
                    processor=row['PROCESSOR'],
                    ssd=row['SSD'],
                    hdd=row['HDD'],
                    gc=row['GRAPHICS CARD'],
                    ram=row['RAM'],
                    sn=row['SERIAL NUMBER'],
                )
            
            return redirect('success')  # Redirect to a success page or similar
    else:
        form = UploadExcelForm()

    return render(request, 'upload.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')