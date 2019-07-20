from django.shortcuts import render
from django.http import HttpResponse

from .models import Matkul
from .models import Matkur
from .models import Profesi
from .models import Profesi_Matkul
from .models import Profesi_Matkur

import csv

def index(request):
    matkul = Matkul.objects.all()
    profesi = Profesi.objects.all()
    matkur = Matkur.objects.all()

    context = {
        'judul':'TEKNIK INFORMATIKA',
        'Matkuls':matkul,
        'Matkurs':matkur,
        'Profesis':profesi,
    }

    if request.method == 'POST':
        context['nama_profesi'] = request.POST['name_profesi']

        data_profesi = {
            'DATA MODEL ADMINISTRATOR':'data/uk_dma.csv'
        }
        data_rps = {
            'data/sap_ak.csv':('AK045203','ARSITEKTUR KOMPUTER','2'),
            'data/sap_ap1.csv':('IT045201','ALGORITMA DAN PEMROGRAMAN 1','2')
        }

        for profesi1, dataset_profesi in data_profesi.items():
            if request.POST.get('name_profesi') == profesi1:
                with open (dataset_profesi,'r', encoding = "utf-8")as csv_file:
                    csv_reader = csv.reader(csv_file)
                    next(csv_reader)
                    list_kw_profesi = []
                    for row in csv_file:
                        usenorm = normalize()
                        text_norm = usenorm.tokenize(row)
                        list_kw_profesi.extend(text_norm)
                    keyword_profesi = Counter(list_kw_profesi)

        profesi_matkul = [ ]
        for dataset_rps, matkul1 in data_rps.items():
            with open(dataset_rps, 'r', encoding = "utf-8") as csv_file:
                csv_reader = csv_reader(csv_file)
                next(csv_reader)

                list_kw_rps = []
                for row in csv_file:
                    usenorm = normalize()
                    text_norm = usenorm.tokenize(row)
                    list_kw_rps.extend(text_norm)
                keyword_rps = Counter(list_kw_rps)

                def jaccard_similarity(x,y):
                    intersection_cardinality = len(set.intersection(*[set(x)]))
                    union_cardinality = len(set.union(*[set(x), set(y)]))
                    return intersection_cardinality/float(union_cardinality)
                hasil = jaccard_similarity(list_kw_profesi, list_kw_rps)
                hasil_percen = '{0:.0%}'.format(hasil)
                kata_sama = set.intersection(*[set(list_kw_profesi), set(list_kw_rps)])

                print ('Hasil Similarity Profesi'+request.POST.get('name_profesi')+ ' dan matkul' +matkul1[1]+ 'adalah ...')
                print ('  ' +hasil_percen+ '\n')

            if hasil > 0:
                profesi_matkul.append(matkul1)
                print('daftar kata penting untuk profesi '+request.POST.get('name_profesi') + '\n')
                print(str (list_kw_profesi)+ '\n\n')
                print('daftar kata penting mata kuliah '+matkul1[1]+ '\n')
                print(str(list_kw_rps)+ '\n\n')
                print('jumlah masing masing kata penting profesi' +request.POST.get('name_profesi')+ '\n')
                print(str(len(keyword_profesi))+ '\n\n')
                print('jumlah masing masing kata di sap matakuliah' +matkul1[1]+'\n')
                print(str(len(keyword_rps))+ '\n\n')
                print('Hasil Similarity Profesi' + request.POST.get('name_profesi') + 'dan sap matakuliah' +matkul1[1]+ 'adalah \n')
                print('('+str(len(kata_sama))+' / (' +str(len(keyword_rps))+' + ' +str(len(keyword_profesi))+ ' - '+str(len(kata_sama))+ '))*100% = '+hasil_percen+ '\n\n')
                print('kode unit yang sama di profesi '+request.POST.get('name_profesi')+ 'dan sap matkul' +matkul1[1]+ ': \n')
                print(str(kata_sama)+ '\n\n')
                print('###\n\n')

        #insert matkul ke tabel Profesi_Matkul       
        for i in profesi_matkul:
            insert_table = Profesi_Matkul(kdmk = i[0], matkul= i[1], sks = i[2])
            insert_table.save()


        # return render(request, 'sistem/profesi.html', context)
    return render(request, 'sistem/index.html', context)

def profesi(request):
    profesi_matkul = Profesi_Matkul.objects.all()
    profesi_matkur = Profesi_Matkur.objects.all()
    context = {
        'Profesi_Matkuls' :profesi_matkul,
        'Profesi_Matkurs' :profesi_matkur,
    }
    return render(request, 'sistem/profesi.html', context)
